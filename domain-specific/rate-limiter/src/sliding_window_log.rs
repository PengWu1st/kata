use redis::Commands;
use std::time::{Duration, Instant};

pub struct SlidingWindowLog {
    limit: u32,
    window_size: Duration,
    redis_client: redis::Client,
}

impl SlidingWindowLog {
    pub fn new(limit: u32, window_size: Duration, redis_url: &str) -> Self {
        let client = redis::Client::open(redis_url).expect("Invalid Redis URL");
        SlidingWindowLog {
            limit,
            window_size,
            redis_client: client,
        }
    }

    pub fn allow(&self) -> bool {
        let now = Instant::now();
        let mut con = self
            .redis_client
            .get_connection()
            .expect("Failed to connect to Redis");

        let key = "request_timestamps";
        let _: () = con
            .zrembyscore(
                key,
                0,
                now.duration_since(Instant::now() - self.window_size)
                    .as_secs() as isize,
            )
            .expect("Failed to remove old timestamps");

        let request_count: isize = con.zcard(key).expect("Failed to get request count");
        if request_count < self.limit as isize {
            let _: () = con
                .zadd(key, now.elapsed().as_secs(), now.elapsed().as_secs())
                .expect("Failed to add new timestamp");
            true
        } else {
            false
        }
    }
}
