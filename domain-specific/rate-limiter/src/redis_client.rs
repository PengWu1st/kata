use redis::Commands;

pub struct RedisClient {
    client: redis::Client,
}

impl RedisClient {
    pub fn new(redis_url: &str) -> Self {
        let client = redis::Client::open(redis_url).expect("Invalid Redis URL");
        RedisClient { client }
    }

    pub fn get_connection(&self) -> redis::Connection {
        self.client
            .get_connection()
            .expect("Failed to connect to Redis")
    }

    pub fn set_value<T: redis::ToRedisArgs>(&self, key: &str, value: T) {
        let mut con = self.get_connection();
        let _: () = con.set(key, value).expect("Failed to set value in Redis");
    }

    pub fn get_value<T: redis::FromRedisValue>(&self, key: &str) -> Option<T> {
        let mut con = self.get_connection();
        con.get(key).ok()
    }
}
