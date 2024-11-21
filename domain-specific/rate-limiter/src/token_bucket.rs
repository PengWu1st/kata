use redis::Commands;
use std::time::{Duration, Instant};

pub struct TokenBucket {
    capacity: u32,
    tokens: u32,
    refill_rate: u32,
    last_refill: Instant,
    redis_client: redis::Client,
}

impl TokenBucket {
    pub fn new(capacity: u32, refill_rate: u32, redis_url: &str) -> Self {
        let client = redis::Client::open(redis_url).expect("Invalid Redis URL");
        TokenBucket {
            capacity,
            tokens: capacity,
            refill_rate,
            last_refill: Instant::now(),
            redis_client: client,
        }
    }

    pub fn allow(&mut self) -> bool {
        self.refill();
        if self.tokens > 0 {
            self.tokens -= 1;
            self.save_state();
            true
        } else {
            false
        }
    }

    fn refill(&mut self) {
        let now = Instant::now();
        let elapsed = now.duration_since(self.last_refill);
        let new_tokens = (elapsed.as_secs() * self.refill_rate as u64) as u32;
        if new_tokens > 0 {
            self.tokens = std::cmp::min(self.capacity, self.tokens + new_tokens);
            self.last_refill = now;
        }
    }

    fn save_state(&self) {
        let mut con = self
            .redis_client
            .get_connection()
            .expect("Failed to connect to Redis");
        let _: () = con
            .set("tokens", self.tokens)
            .expect("Failed to save tokens to Redis");
        let _: () = con
            .set("last_refill", self.last_refill.elapsed().as_secs())
            .expect("Failed to save last_refill to Redis");
    }

    fn load_state(&mut self) {
        let mut con = self
            .redis_client
            .get_connection()
            .expect("Failed to connect to Redis");
        self.tokens = con.get("tokens").unwrap_or(self.capacity);
        let last_refill_secs: u64 = con.get("last_refill").unwrap_or(0);
        self.last_refill = Instant::now() - Duration::from_secs(last_refill_secs);
    }
}
