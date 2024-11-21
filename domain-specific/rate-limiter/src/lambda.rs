use lambda_runtime::{handler_fn, Context, Error};
use serde_json::{json, Value};
use crate::{TokenBucket, LeakingBucket, FixedWindowCounter, SlidingWindowLog, SlidingWindowCounter};

pub struct LambdaHandler;

impl LambdaHandler {
    pub async fn run() -> Result<(), Error> {
        let func = handler_fn(Self::handle_request);
        lambda_runtime::run(func).await?;
        Ok(())
    }

    async fn handle_request(event: Value, _: Context) -> Result<Value, Error> {
        // 根据event中的信息选择相应的Rate Limiter算法
        // ...existing code...
        let response = json!({
            "statusCode": 200,
            "body": "请求被允许"
        });
        Ok(response)
    }
}
