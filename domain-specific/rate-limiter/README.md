# Rate Limiter 设计文档

## 简介
本项目实现了一个基于Rust的Rate Limiter，支持以下五种算法，并使用Redis作为存储后端：
- Token Bucket
- Leaking Bucket
- Fixed Window Counter
- Sliding Window Log
- Sliding Window Counter

该模块可以通过pyO3供Python代码调用，也可以单独部署为一个AWS Lambda函数供AWS API Gateway调用。

## 算法设计

### Token Bucket
Token Bucket算法通过在固定时间间隔内向桶中添加令牌来控制请求速率。每个请求消耗一个令牌，如果桶中没有令牌则拒绝请求。

### Leaking Bucket
Leaking Bucket算法将请求放入一个固定容量的桶中，并以固定速率从桶中移除请求。如果桶满则拒绝请求。

### Fixed Window Counter
Fixed Window Counter算法在固定时间窗口内计数请求数量，如果请求数量超过限制则拒绝请求��

### Sliding Window Log
Sliding Window Log算法记录每个请求的时间戳，并在滑动窗口内统计请求数量，如果请求数量超过限制则拒绝请求。

### Sliding Window Counter
Sliding Window Counter算法将时间窗口分为多个小窗口，并在每个小窗口内计数请求数量，通过滑动窗口内的计数总和来控制请求速率。

## 使用Redis作为存储
Redis作为高性能的内存数据库，非常适合用于存储Rate Limiter的状态信息。每种算法的状态信息将存储在Redis中，以确保分布式环境下的高效和一致性。

## 代码结构
- `src/`
  - `lib.rs`: 包含Rate Limiter的主要逻辑
  - `token_bucket.rs`: Token Bucket算法的实现
  - `leaking_bucket.rs`: Leaking Bucket算法的实现
  - `fixed_window_counter.rs`: Fixed Window Counter算法的实现
  - `sliding_window_log.rs`: Sliding Window Log算法的实现
  - `sliding_window_counter.rs`: Sliding Window Counter算法的实现
  - `redis_client.rs`: Redis客户端的封装
  - `lambda.rs`: AWS Lambda函数的实现
  - `python.rs`: pyO3接口的实现

## 安装和运行
1. 安装Rust和Cargo
2. 克隆本仓库
```sh
git clone https://github.com/yourusername/rate-limiter.git
cd rate-limiter
```
3. 配置Redis服务器
4. 运行项目

```shell
cargo run
```


## 示例
使用pyO3调用
以下是一个使用Token Bucket算法的Python示例：
```shell
import rate_limiter

limiter = rate_limiter.TokenBucket(10, 1)  # 每秒添加1个令牌，最大容量为10
if limiter.allow():
    print("请求被允许")
else:
    print("请求被拒绝")
```

部署为AWS Lambda函数
1. 构建Lambda函数
```shell
cargo build --release --target x86_64-unknown-linux-musl
```
1. 将生成的二进制文件上传到AWS Lambda
2. 配置AWS API Gateway以调用Lambda函数

## 模块设计

### 模块列表
1. `lib.rs`: 主模块，包含Rate Limiter的主要逻辑。
2. `token_bucket.rs`: 实现Token Bucket算法。
3. `leaking_bucket.rs`: 实现Leaking Bucket算法。
4. `fixed_window_counter.rs`: 实现Fixed Window Counter算法。
5. `sliding_window_log.rs`: 实现Sliding Window Log算法。
6. `sliding_window_counter.rs`: 实现Sliding Window Counter算法。
7. `redis_client.rs`: 封装Redis客户端，用于存储和检索Rate Limiter的状态信息。
8. `lambda.rs`: 实现AWS Lambda函数的逻辑。
9. `python.rs`: 实现pyO3接口，使Rate Limiter可以被Python代码调用。

### 类设计

#### `lib.rs`
- `RateLimiter`: 主要的Rate Limiter类，包含通用的逻辑和接口。

#### `token_bucket.rs`
- `TokenBucket`: 实现Token Bucket算法的类。

#### `leaking_bucket.rs`
- `LeakingBucket`: 实现Leaking Bucket算法的类。

#### `fixed_window_counter.rs`
- `FixedWindowCounter`: 实现Fixed Window Counter算法的类。

#### `sliding_window_log.rs`
- `SlidingWindowLog`: 实现Sliding Window Log算法的类。

#### `sliding_window_counter.rs`
- `SlidingWindowCounter`: 实现Sliding Window Counter算法的类。

#### `redis_client.rs`
- `RedisClient`: 封装Redis操作的类，提供存储和检索Rate Limiter状态信息的接口。

#### `lambda.rs`
- `LambdaHandler`: 处理AWS Lambda请求的类。

#### `python.rs`
- `PyRateLimiter`: 提供给Python调用的Rate Limiter接口类。



贡献
欢迎提交Issue和Pull Request来贡献代码。

许可证
本项目基于MIT许可证开源。