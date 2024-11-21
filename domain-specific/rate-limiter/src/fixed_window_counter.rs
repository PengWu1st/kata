use redis::Commands;
use std::time::{Duration, Instant};

pub struct FixedWindowCounter {
    limit: u32,
    window_size: Duration,
    count: u32,
    window_start: Instant,
    redis_client: redis::Client,
}

impl FixedWindowCounter {
    pub fn new(limit: u32, window_size: Duration, redis_url: &str) -> Self {
        let client = redis::Client::open(redis_url).expect("Invalid Redis URL");
        FixedWindowCounter {
            limit,
            window_size,
            count: 0,
            window_start: Instant::now(),
            redis_client: client,
        }
    }

    pub fn allow(&mut self) -> bool {
        self.reset_if_needed();
        if self.count < self.limit {
            self.count += 1;
            self.save_state();
            true
        } else {
            false
        }
    }

    fn reset_if_needed(&mut self) {
        let now = Instant::now();
        if now.duration_since(self.window_start) >= self.window_size {
            self.count = 0;
            self.window_start = now;
        }
    }

    fn save_state(&self) {
        let mut con = self
            .redis_client
            .get_connection()
            .expect("Failed to connect to Redis");
        let _: () = con
            .set("count", self.count)
            .expect("Failed to save count to Redis");
        let _: () = con
            .set("window_start", self.window_start.elapsed().as_secs())
            .expect("Failed to save window_start to Redis");
    }

    fn load_state(&mut self) {
        let mut con = self
            .redis_client
            .get_connection()
            .expect("Failed to connect to Redis");
        self.count = con.get("count").unwrap_or(0);
        let window_start_secs: u64 = con.get("window_start").unwrap_or(0);
        self.window_start = Instant::now() - Duration::from_secs(window_start_secs);
    }
}
