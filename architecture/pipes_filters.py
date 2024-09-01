import threading
import queue
import time

# 定义过滤器函数


def filter1(input_queue, output_queue):
    while True:
        item = input_queue.get()
        if item is None:
            break

        print(f'filter1: processing {item=}')
        time.sleep(1)
        # 处理数据
        processed_item = item * 2

        output_queue.put(processed_item)
        input_queue.task_done()


def filter2(input_queue, output_queue):
    while True:
        item = input_queue.get()
        if item is None:
            break

        print(f'filter2: processing {item=}')
        time.sleep(1)
        # 处理数据
        processed_item = item + 1
        output_queue.put(processed_item)
        input_queue.task_done()


def filter3(input_queue, output_queue):
    while True:
        item = input_queue.get()
        if item is None:
            break
        print(f'filter3: processing {item=}')
        time.sleep(1)
        # 处理数据
        processed_item = item ** 2
        if out_queue is not None:
            output_queue.put(processed_item)
        input_queue.task_done()


# 创建队列
pipe1 = queue.Queue()
pipe2 = queue.Queue()
pipe3 = queue.Queue()

start = time.time()
# 创建并启动线程
threads = []
for filter_func, in_queue, out_queue in [
    (filter1, pipe1, pipe2),
    (filter2, pipe2, pipe3),
    (filter3, pipe3, None)
]:
    thread = threading.Thread(target=filter_func, args=(
        in_queue, out_queue), daemon=True)
    thread.start()
    threads.append(thread)

# 向第一个队列中添加数据
for item in range(10):
    pipe1.put(item)

pipe1.join()
pipe2.join()
pipe3.join()
# 向队列中添加 None 以指示结束
for pipe in [pipe1, pipe2, pipe3]:
    pipe.put(None)

# 等待所有线程完成
for thread in threads:
    thread.join()

# 从最后一个队列中获取结果
while not pipe3.empty():
    print(pipe3.get())

print(f'Elapsed time: {time.time() - start:.2f} seconds')
