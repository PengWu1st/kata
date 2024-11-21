use redis::Commands;
use std::time::{Duration, Instant};

pub struct LeakingBucket {
    capacity: u32,
    water: u32,
    leak_rate: u32,
    last_leak: Instant,
    redis_client: redis::Client,
}

impl LeakingBucket {
    pub fn new(capacity: u32, leak_rate: u32, redis_url: &str) -> Self {
        let client = redis::Client::open(redis_url).expect("Invalid Redis URL");
        LeakingBucket {
            capacity,
            water: 0,
            leak_rate,
            last_leak: Instant::now(),
            redis_client: client,
        }
    }

    pub fn allow(&mut self) -> bool {
        self.leak();
        if self.water < self.capacity {
            self.water += 1;
            self.save_state();
            true
        } else {
            false
        }
    }

    fn leak(&mut self) {
        let now = Instant::now();
        let elapsed = now.duration_since(self.last_leak);
        let leaked_water = (elapsed.as_secs() * self.leak_rate as u64) as u32;
        if leaked_water > 0 {
            self.water = self.water.saturating_sub(leaked_water);
            self.last_leak = now;
        }
    }

    fn save_state(&self) {
        let mut con = self
            .redis_client
            .get_connection()
            .expect("Failed to connect to Redis");
        let _: () = con
            .set("water", self.water)
            .expect("Failed to save water to Redis");
        let _: () = con
            .set("last_leak", self.last_leak.elapsed().as_secs())
            .expect("Failed to save last_leak to Redis");
    }

    fn load_state(&mut self) {
        let mut con = self
            .redis_client
            .get_connection()
            .expect("Failed to connect to Redis");
        self.water = con.get("water").unwrap_or(0);
        let last_leak_secs: u64 = con.get("last_leak").unwrap_or(0);
        self.last_leak = Instant::now() - Duration::from_secs(last_leak_secs);
    }
}
