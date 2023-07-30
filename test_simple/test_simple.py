from simple.simple import (
    Boolean, Number, Add, Mult, LessThan, Variable, DoNothing,
    Assign
)


def test_boolean_str():
    boolean = Boolean(True)
    assert str(boolean) == 'True'

def test_boolean_repr():
    boolean = Boolean(True)
    assert repr(boolean) == '《True》'

def test_boolean_reducible():
    boolean = Boolean(True)
    assert boolean.reducible == False

def test_less_than_str():
    less_than = LessThan(Number(1), Number(2))
    assert str(less_than) == '1 < 2'

def test_less_than_repr():
    less_than = LessThan(Number(1), Number(2))
    assert repr(less_than) == '《1 < 2》'

def test_less_than_reducible():
    less_than = LessThan(Number(1), Number(2))
    assert less_than.reducible == True

def test_less_than_reduce():
    less_than = LessThan(Number(1), Number(2))
    assert less_than.reducible == True
    less_than_reduced = less_than.reduce({})
    assert isinstance(less_than_reduced, Boolean)
    assert less_than_reduced.reducible == False
    assert str(less_than_reduced) == 'True'

    
def test_number_str():
    number = Number(1)
    assert str(number) == '1'

def test_number_repr():
    number = Number(1)
    assert repr(number) == '《1》'

def test_number_reducible():
    number = Number(1)
    assert number.reducible == False

def test_add_str():
    add = Add(Number(1), Number(2))
    assert str(add) == '1 + 2'

def test_add_repr():
    add = Add(Number(1), Number(2))
    assert repr(add) == '《1 + 2》'


def test_add_reducible():
    add = Add(Number(1), Number(2))
    assert add.reducible == True


def test_add_reduce():
    add = Add(Number(1), Number(2))
    assert add.reducible == True
    add_reduced = add.reduce({})
    assert isinstance(add_reduced, Number)
    assert add_reduced.reducible == False
    assert str(add_reduced) == '3'


def test_mult_str():
    mult = Mult(Number(1), Number(2))
    assert str(mult) == '1 * 2'

def test_mult_repr():
    mult = Mult(Number(1), Number(2))
    assert repr(mult) == '《1 * 2》'

def test_mult_reducible():
    mult = Mult(Number(1), Number(2))
    assert mult.reducible == True

def test_mult_reduce():
    mult = Mult(Number(1), Number(2))
    assert mult.reducible == True
    mult_reduced = mult.reduce({})
    assert isinstance(mult_reduced, Number)
    assert mult_reduced.reducible == False
    assert str(mult_reduced) == '2'


def test_variable_str():
    variable = Variable('x')
    assert str(variable) == 'x'

def test_variable_repr():
    variable = Variable('x')
    assert repr(variable) == '《x》'

def test_variable_reducible():
    variable = Variable('x')
    assert variable.reducible == True

def test_variable_reduce():
    variable = Variable('x')
    assert variable.reducible == True
    variable_reduced = variable.reduce({'x': Number(1)})
    assert isinstance(variable_reduced, Number)
    assert variable_reduced.reducible == False
    assert str(variable_reduced) == '1'

def test_do_nothing_str():
    do_nothing = DoNothing()
    assert str(do_nothing) == 'do-nothing'

def test_do_nothing_repr():
    do_nothing = DoNothing()
    assert repr(do_nothing) == '《do-nothing》'

def test_do_nothing_reducible():
    do_nothing = DoNothing()
    assert do_nothing.reducible == False

def test_assign_str():
    assign = Assign('x', Number(1))
    assert str(assign) == 'x = 1'

def test_assign_repr():
    assign = Assign('x', Number(1))
    assert repr(assign) == '《x = 1》'

def test_assign_reducible():
    assign = Assign('x', Number(1))
    assert assign.reducible == True

def test_assign_reduce():
    assign = Assign('x', Number(1))
    assert assign.reducible == True
    assign_reduced, env = assign.reduce({})
    assert isinstance(assign_reduced, DoNothing)
    assert assign_reduced.reducible == False
    assert str(assign_reduced) == 'do-nothing'
    assert env == {'x': Number(1)}

def test_assign_reduce_with_variable():
    assign = Assign('x', Variable('y'))
    assert assign.reducible == True
    assign_reduced, env = assign.reduce({'y': Number(1)})
    assert isinstance(assign_reduced, Assign)
    assert assign_reduced.reducible == True
    assert str(assign_reduced) == 'x = 1'
    assert env == {'y': Number(1)}
    assign_reduced2, env2 = assign_reduced.reduce(env)
    assert assign_reduced2.reducible == False
    assert str(assign_reduced2) == 'do-nothing'
    assert env2 == {'x': Number(1), 'y': Number(1)}

def test_more_complicated_expression():
    expr = Add(Number(1), Mult(Number(2), Number(3)))
    assert str(expr) == '1 + 2 * 3'
    assert repr(expr) == '《1 + 2 * 3》'


    expr = Add(Mult(Number(2), Number(3)), Mult(Number(4), Number(5)))
    assert str(expr) == '2 * 3 + 4 * 5'
    assert repr(expr) == '《2 * 3 + 4 * 5》'

def test_more_complicated_reduce():
    expr = Add(Number(1), Mult(Number(2), Number(3)))
    assert str(expr) == '1 + 2 * 3'
    assert repr(expr) == '《1 + 2 * 3》'

    assert expr.reducible == True
    expr_reduced = expr.reduce({})
    assert isinstance(expr_reduced, Add)
    assert expr_reduced.reducible == True
    assert str(expr_reduced) == '1 + 6'

    expr_reduced = expr_reduced.reduce({})
    assert isinstance(expr_reduced, Number)
    assert expr_reduced.reducible == False
    assert str(expr_reduced) == '7'


