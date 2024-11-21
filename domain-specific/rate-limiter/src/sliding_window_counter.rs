use redis::Commands;
use std::time::{Duration, Instant};

pub struct SlidingWindowCounter {
    limit: u32,
    window_size: Duration,
    bucket_count: u32,
    redis_client: redis::Client,
}

impl SlidingWindowCounter {
    pub fn new(limit: u32, window_size: Duration, bucket_count: u32, redis_url: &str) -> Self {
        let client = redis::Client::open(redis_url).expect("Invalid Redis URL");
        SlidingWindowCounter {
            limit,
            window_size,
            bucket_count,
            redis_client: client,
        }
    }

    pub fn allow(&self) -> bool {
        let now = Instant::now();
        let bucket_duration = self.window_size / self.bucket_count;
        let current_bucket = now
            .duration_since(Instant::now() - bucket_duration)
            .as_secs()
            / bucket_duration.as_secs();

        let mut con = self
            .redis_client
            .get_connection()
            .expect("Failed to connect to Redis");

        let key = "request_buckets";
        let _: () = con
            .hincr(key, current_bucket, 1)
            .expect("Failed to increment bucket count");

        let mut total_count = 0;
        for i in 0..self.bucket_count {
            let bucket = (current_bucket + i) % self.bucket_count;
            let count: isize = con.hget(key, bucket).unwrap_or(0);
            total_count += count;
        }

        if total_count < self.limit as isize {
            true
        } else {
            let _: () = con
                .hincr(key, current_bucket, -1)
                .expect("Failed to decrement bucket count");
            false
        }
    }
}
