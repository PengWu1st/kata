from simple.simple import Add, Mult, Number, LessThan, Boolean, Assign, Variable
from simple.Machine import Machine


def test_machine_run():
    machine = Machine(
        Assign('x',Add(
            Mult(Number(1), Number(2)),
            Mult(Number(3), Number(4))
        )
               )
        ,
        {}
    )
    machine.run()
    assert machine.environment == {'x': Number(14)}


def test_machine_run_less_than():
    machine = Machine(
        Assign('x',LessThan(
            Add(Number(1), Number(2)),
            Mult(Number(3), Number(4))
        ))
        ,
        {}
    )
    machine.run()
    assert machine.environment == {'x': Boolean(True)}



def test_machine_run_assign():
    machine = Machine(
        Assign('x', Add(Variable('x'), Number(1))), 
        {'x': Number(2)}
    )
    machine.run()
    assert machine.environment == {'x': Number(3)}