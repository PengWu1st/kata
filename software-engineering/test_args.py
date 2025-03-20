from typing import Any, Type, TypeVar
from unittest import TestCase
from dataclasses import dataclass, field, fields, is_dataclass, Field

T = TypeVar('T')


class Args:
    @staticmethod
    def parse(optionsClass: Type[T], *args: str) -> T:
        if not is_dataclass(optionsClass):
            raise TypeError(f"{optionsClass} is not a dataclass")

        values = [Args._parseOption(field, *args)
                  for field in fields(optionsClass)]

        return optionsClass(*values)

    @staticmethod
    def _parseOption(field: Field, *args: str) -> Any:
        if field.type == bool:
            return '-'+field.metadata['label'] in args
        elif field.type == int:
            index = args.index('-'+field.metadata['label'])
            return int(args[index + 1])
        elif field.type == str:
            index = args.index('-'+field.metadata['label'])
            return args[index + 1]
        else:
            return


class TestArgs(TestCase):

    # Single Option cases:
    @dataclass
    class BooleanOption:
        logging: bool = field(metadata={"label": "l"})

    def test_should_set_boolean_option_to_true_if_flag_present(self):
        options = Args.parse(self.BooleanOption, "-l")
        self.assertTrue(options.logging)

    def test_should_set_boolean_option_to_false_if_flag_not_present(self):
        options = Args.parse(self.BooleanOption)
        self.assertFalse(options.logging)

    @dataclass
    class IntegerOption:
        port: int = field(metadata={"label": "p"})

    def test_should_set_integer_option(self):
        options = Args.parse(self.IntegerOption, "-p", "8080")
        self.assertEqual(8080, options.port)

    @dataclass
    class StringOption:
        directory: str = field(metadata={"label": "d"})

    def test_should_set_string_option(self):
        options = Args.parse(self.StringOption, "-d", "/usr/logs")
        self.assertEqual("/usr/logs", options.directory)

    @dataclass
    class MultipleOptions:
        logging: bool = field(metadata={"label": "l"})
        port: int = field(metadata={"label": "p"})
        directory: str = field(metadata={"label": "d"})

    def test_should_set_multiple_options(self):
        args = ("-l", "-p", "8080", "-d", "/usr/logs")
        options = Args.parse(self.MultipleOptions, *args)
        self.assertTrue(options.logging)
        self.assertEqual(8080, options.port)
        self.assertEqual("/usr/logs", options.directory)

    # sad path

    """
    - TODO bool - l t / -l t f
    - TODO int - p / -p 8080 8080
    - TODO string - d / -d / usr/logs / usr/vars

    default value
    - TODO bool: false
    - TODO int: 0
    - TODO string: ""

    """

    def _test_should_example_2(self):
        """-g this is a list -d 1 2 -3 5"""
        @dataclass
        class ListOptions:
            group: str = field(metadata={"label": "g"})
            decimals: int = field(metadata={"label": "d"})

        options = Args.parse(
            ListOptions, "-g", "this", "is", "a", "list", "-d", "1", "2", "-3", "5")

        self.assertEqual(['this', 'is', 'a', 'list'], options.group)
        self.assertEqual([1, 2, -3, 5], options.decimals)
