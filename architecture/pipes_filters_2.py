from abc import ABC, abstractmethod
from multiprocessing.dummy import freeze_support
import queue
import threading
import multiprocessing
import asyncio
import rx
from rx import operators as ops


class Pipe(ABC):
    @abstractmethod
    def put(self, item):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def join(self):
        pass


class Filter(ABC):
    @abstractmethod
    def process(self, item):
        pass


class PipelineExecutor(ABC):
    def __init__(self, filters):
        self.filters = filters

    @abstractmethod
    def execute(self, data):
        pass


class ThreadingPipe(Pipe):
    def __init__(self):
        self.queue = queue.Queue()

    def put(self, item):
        self.queue.put(item)

    def get(self):
        return self.queue.get()

    def join(self):
        self.queue.join()


class ThreadingExecutor(PipelineExecutor):
    def execute(self, data):
        pipes = [ThreadingPipe() for _ in range(len(self.filters) + 1)]
        threads = []

        for i, filter in enumerate(self.filters):
            thread = threading.Thread(
                target=self.run_filter, args=(filter, pipes[i], pipes[i + 1]))
            thread.start()
            threads.append(thread)

        for item in data:
            pipes[0].put(item)

        for pipe in pipes:
            pipe.put(None)

        for thread in threads:
            thread.join()

        results = []
        while not pipes[-1].queue.empty():
            results.append(pipes[-1].get())
        return results

    def run_filter(self, filter, input_pipe, output_pipe):
        while True:
            item = input_pipe.get()
            if item is None:
                break
            processed_item = filter.process(item)
            output_pipe.put(processed_item)
            input_pipe.queue.task_done()


class MultiprocessingPipe(Pipe):
    def __init__(self):
        self.queue = multiprocessing.Queue()

    def put(self, item):
        self.queue.put(item)

    def get(self):
        return self.queue.get()

    def join(self):
        pass  # Multiprocessing queues do not have a join method


class MultiprocessingExecutor(PipelineExecutor):
    def execute(self, data):
        pipes = [MultiprocessingPipe() for _ in range(len(self.filters) + 1)]
        processes = []

        for i, filter in enumerate(self.filters):
            process = multiprocessing.Process(
                target=self.run_filter, args=(filter, pipes[i], pipes[i + 1]))
            process.start()
            processes.append(process)

        for item in data:
            pipes[0].put(item)

        for pipe in pipes:
            pipe.put(None)

        for process in processes:
            process.join()

        results = []
        while not pipes[-1].queue.empty():
            results.append(pipes[-1].get())
        return results

    def run_filter(self, filter, input_pipe, output_pipe):
        while True:
            item = input_pipe.get()
            if item is None:
                break
            processed_item = filter.process(item)
            output_pipe.put(processed_item)


class AsyncioPipe(Pipe):
    def __init__(self):
        self.queue = asyncio.Queue()

    async def put(self, item):
        await self.queue.put(item)

    async def get(self):
        return await self.queue.get()

    async def join(self):
        pass  # Asyncio queues do not have a join method


class AsyncioExecutor(PipelineExecutor):
    async def execute(self, data):
        pipes = [AsyncioPipe() for _ in range(len(self.filters) + 1)]
        tasks = []

        for i, filter in enumerate(self.filters):
            task = asyncio.create_task(
                self.run_filter(filter, pipes[i], pipes[i + 1]))
            tasks.append(task)

        for item in data:
            await pipes[0].put(item)

        for pipe in pipes:
            await pipe.put(None)

        await asyncio.gather(*tasks)

        results = []
        while not pipes[-1].queue.empty():
            results.append(await pipes[-1].get())
        return results

    async def run_filter(self, filter, input_pipe, output_pipe):
        while True:
            item = await input_pipe.get()
            if item is None:
                break
            processed_item = filter.process(item)
            await output_pipe.put(processed_item)


# class RxPyPipe(Pipe):
#     def __init__(self):
#         self.subject =

#     def put(self, item):
#         self.subject.on_next(item)

#     def get(self):
#         return self.subject

#     def join(self):
#         self.subject.on_completed()


# class RxPyExecutor(PipelineExecutor):
#     def execute(self, data):
#         pipes = [RxPyPipe() for _ in range(len(self.filters) + 1)]

#         for i, filter in enumerate(self.filters):
#             pipes[i].get().pipe(
#                 ops.map(filter.process)
#             ).subscribe(pipes[i + 1].put)

#         for item in data:
#             pipes[0].put(item)

#         pipes[0].join()

#         results = []
#         pipes[-1].get().subscribe(results.append)
        return results


class MultiplyByTwoFilter(Filter):
    def process(self, item):
        return item * 2


class AddOneFilter(Filter):
    def process(self, item):
        return item + 1


class SquareFilter(Filter):
    def process(self, item):
        return item ** 2


if __name__ == '__main__':
    freeze_support()
    filters = [MultiplyByTwoFilter(), AddOneFilter(), SquareFilter()]

    # 使用 ThreadingExecutor
    executor = ThreadingExecutor(filters)
    data = range(10)
    results = executor.execute(data)
    print("ThreadingExecutor results:", results)

    # 使用 MultiprocessingExecutor
    executor = MultiprocessingExecutor(filters)
    results = executor.execute(data)
    print("MultiprocessingExecutor results:", results)

    # 使用 AsyncioExecutor
    executor = AsyncioExecutor(filters)
    results = asyncio.run(executor.execute(data))
    print("AsyncioExecutor results:", results)

    # # 使用 RxPyExecutor
    # executor = RxPyExecutor(filters)
    # results = executor.execute(data)
    # print("RxPyExecutor results:", results)
