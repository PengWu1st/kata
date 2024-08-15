from abc import ABC, abstractmethod


class Template(ABC):

    def template_method(self) -> None:
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()

        if self.hook1():
            self.base_operation3()
        self.required_operation2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self) -> None:
        print("Template method: base operation1")

    def base_operation2(self) -> None:
        print("Template method: base operation2")

    def base_operation3(self) -> None:
        print("Template method: base operation3")

    @abstractmethod
    def required_operation1(self) -> None:
        pass

    @abstractmethod
    def required_operation2(self) -> None:
        pass

    def hook1(self) -> bool:
        return False

    def hook2(self) -> None:
        pass


class ConcreteClass1(Template):

    def required_operation1(self) -> None:
        print("ConcreteClass1 says: Implemented operation1")

    def required_operation2(self) -> None:
        print("ConcreteClass1 says: Implemented operation2")

    def hook1(self) -> bool:
        return True

    def hook2(self) -> None:
        print("ConcreteClass1 says: Overridden hook2")


class ConcreteClass2(Template):

    def required_operation1(self) -> None:
        print("ConcreteClass2 says: Implemented operation1")

    def required_operation2(self) -> None:
        print("ConcreteClass2 says: Implemented operation2")


def main():

    concrete_class_1 = ConcreteClass1()
    concrete_class_1.template_method()

    concrete_class_2 = ConcreteClass2()
    concrete_class_2.template_method()


if __name__ == "__main__":
    main()
