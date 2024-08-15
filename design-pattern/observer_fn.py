

from typing import Callable


def update_observer1(value: str) -> None:
    print(f"observer1 received: {value}")


def update_observer2(value: str) -> None:
    print(f"observer2 received: {value}")


UpdateFn = Callable[[str], None]


def notify(update_fns: list[UpdateFn], value: str) -> None:
    for update_fn in update_fns:
        update_fn(value)


def main():
    notify([update_observer1, update_observer2], "hello world")


if __name__ == "__main__":
    main()
