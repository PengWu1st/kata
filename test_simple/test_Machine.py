from simple.simple import Add, Mult, Number, LessThan, Boolean
from simple.Machine import Machine


def test_machine_run():
    machine = Machine(
        Add(
            Mult(Number(1), Number(2)),
            Mult(Number(3), Number(4))
        ),
        {}
    )
    assert machine.run() == Number(14)


def test_machine_run_less_than():
    machine = Machine(
        LessThan(
            Add(Number(1), Number(2)),
            Mult(Number(3), Number(4))
        ),
        {}
    )
    assert machine.run() == Boolean(True)