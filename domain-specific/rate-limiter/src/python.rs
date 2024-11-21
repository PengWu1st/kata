use crate::{
    FixedWindowCounter, LeakingBucket, SlidingWindowCounter, SlidingWindowLog, TokenBucket,
};
use pyo3::prelude::*;

#[pyclass]
pub struct PyRateLimiter {
    // ...existing code...
}

#[pymethods]
impl PyRateLimiter {
    #[new]
    pub fn new() -> Self {
        PyRateLimiter {
            // ...existing code...
        }
    }

    pub fn create_token_bucket(
        &self,
        capacity: u32,
        refill_rate: u32,
        redis_url: &str,
    ) -> TokenBucket {
        TokenBucket::new(capacity, refill_rate, redis_url)
    }

    pub fn create_leaking_bucket(
        &self,
        capacity: u32,
        leak_rate: u32,
        redis_url: &str,
    ) -> LeakingBucket {
        LeakingBucket::new(capacity, leak_rate, redis_url)
    }

    pub fn create_fixed_window_counter(
        &self,
        limit: u32,
        window_size: u64,
        redis_url: &str,
    ) -> FixedWindowCounter {
        FixedWindowCounter::new(limit, Duration::from_secs(window_size), redis_url)
    }

    pub fn create_sliding_window_log(
        &self,
        limit: u32,
        window_size: u64,
        redis_url: &str,
    ) -> SlidingWindowLog {
        SlidingWindowLog::new(limit, Duration::from_secs(window_size), redis_url)
    }

    pub fn create_sliding_window_counter(
        &self,
        limit: u32,
        window_size: u64,
        bucket_count: u32,
        redis_url: &str,
    ) -> SlidingWindowCounter {
        SlidingWindowCounter::new(
            limit,
            Duration::from_secs(window_size),
            bucket_count,
            redis_url,
        )
    }
}

#[pymodule]
fn rate_limiter(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<PyRateLimiter>()?;
    Ok(())
}
