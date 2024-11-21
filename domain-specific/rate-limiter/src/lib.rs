mod fixed_window_counter;
mod lambda;
mod leaking_bucket;
mod python;
mod redis_client;
mod sliding_window_counter;
mod sliding_window_log;
mod token_bucket;

pub use fixed_window_counter::FixedWindowCounter;
pub use lambda::LambdaHandler;
pub use leaking_bucket::LeakingBucket;
pub use python::PyRateLimiter;
pub use redis_client::RedisClient;
pub use sliding_window_counter::SlidingWindowCounter;
pub use sliding_window_log::SlidingWindowLog;
pub use token_bucket::TokenBucket;

pub struct RateLimiter {
    // 通用的Rate Limiter逻辑和接口
    // ...existing code...
}

impl RateLimiter {
    // 通用的Rate Limiter方法
    // ...existing code...
}
