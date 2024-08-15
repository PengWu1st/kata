from typing import Callable
from functools import partial


def base_operation1() -> None:
    print("Template method: base operation1")


def base_operation2() -> None:
    print("Template method: base operation2")


def base_operation3() -> None:
    print("Template method: base operation3")


def template_method_basic(

    required_operation1: Callable[[], None],
    required_operation2: Callable[[], None],
    hook1: Callable[[], bool] = lambda: False,
    hook2: Callable[[], None] = lambda: None,
) -> None:

    base_operation1()
    required_operation1()
    base_operation2()

    if hook1():
        base_operation3()
    required_operation2()
    base_operation3()
    hook2()


def concrete_operation1() -> None:
    print("ConcreteClass1 says: Implemented operation1")


def concrete_operation2() -> None:
    print("ConcreteClass1 says: Implemented operation2")


def overidden_hook1() -> bool:
    return True


def overidden_hook2() -> None:
    print("ConcreteClass1 says: Overridden hook2")


def base_template_method_closure_version(
        required_operation1: Callable[[], None],
        required_operation2: Callable[[], None],
):
    def template_method(
        hook1: Callable[[], bool] = lambda: False,
        hook2: Callable[[], None] = lambda: None,
    ) -> None:
        base_operation1()
        required_operation1()
        base_operation2()

        if hook1():
            base_operation3()
        required_operation2()
        base_operation3()
        hook2()
    return template_method


def operation1_impl() -> None:
    print("ConcreteClass2 says: Implemented operation1")


def operation2_impl() -> None:
    print("ConcreteClass2 says: Implemented operation2")


def basic_version_usage():
    template_method_basic(
        concrete_operation1,
        concrete_operation2,
        overidden_hook1,
        overidden_hook2,
    )

    template_method_basic(
        operation1_impl,
        operation2_impl,
    )


def closure_version_usage():

    template_method = base_template_method_closure_version(
        operation1_impl, operation2_impl)
    template_method()

    template_method(
        hook1=overidden_hook1,
        hook2=overidden_hook2,
    )


def basic_version_using_partial():
    template_method = partial(
        template_method_basic,
        operation1_impl,
        operation2_impl,
    )
    template_method(
        hook1=overidden_hook1,
        hook2=overidden_hook2,
    )


def main():
    basic_version_usage()
    closure_version_usage()
    basic_version_using_partial()


if __name__ == "__main__":
    main()
