class Boolean:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Boolean):
            return self.value == __value.value
        else:
            return False
    
    def __str__(self) -> str:
        return f'{self.value}'

    def __repr__(self):
        return f'《{self.value}》'
    
    @property
    def reducible(self):
        return False


class LessThan:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return f'{self.left} < {self.right}'
    
    def __repr__(self):
        return f'《{self.left} < {self.right}》'
    
    @property
    def reducible(self):
        return True
    
    def reduce(self, environment):
        if self.left.reducible:
            return LessThan(self.left.reduce(environment), self.right)
        elif self.right.reducible:
            return LessThan(self.left, self.right.reduce(environment))
        else:
            return Boolean(self.left.value < self.right.value)


class Number:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Number):
            return self.value == __value.value
        else:
            return False
    
    def __str__(self) -> str:
        return f'{self.value}'

    def __repr__(self):
        return f'《{self.value}》'
    
    @property
    def reducible(self):
        return False

class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'{self.left} + {self.right}'

    def __repr__(self):
        return f'《{self.left} + {self.right}》'

    @property
    def reducible(self):
        return True
    
    def reduce(self, environment):
        if self.left.reducible:
            return Add(self.left.reduce(environment), self.right)
        elif self.right.reducible:
            return Add(self.left, self.right.reduce(environment))
        else:
            return Number(self.left.value + self.right.value)

class Mult:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f'{self.left} * {self.right}'

    def __repr__(self):
        return f'《{self.left} * {self.right}》'
    
    @property
    def reducible(self):
        return True
    
    def reduce(self, environment):
        if self.left.reducible:
            return Mult(self.left.reduce(environment), self.right)
        elif self.right.reducible:
            return Mult(self.left, self.right.reduce(environment))
        else:
            return Number(self.left.value * self.right.value)

class Variable:
    def __init__(self, name):
        self.name = name
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def __repr__(self):
        return f'《{self.name}》'
    
    @property
    def reducible(self):
        return True
    
    def reduce(self, environment):
        return environment[self.name]

class DoNothing:
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, DoNothing)
    
    def __str__(self) -> str:
        return 'do-nothing'
    
    def __repr__(self):
        return '《do-nothing》'
    
    @property
    def reducible(self):
        return False

class Assign:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression
    
    def __str__(self) -> str:
        return f'{self.name} = {self.expression}'
    
    def __repr__(self):
        return f'《{self.name} = {self.expression}》'
    
    @property
    def reducible(self):
        return True
    
    def reduce(self, environment):
        if self.expression.reducible:
            return Assign(self.name, self.expression.reduce(environment)), environment
        else:
            environment[self.name] = self.expression
            return DoNothing(), environment



