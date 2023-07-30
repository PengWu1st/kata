class Machine:
    def __init__(self, expression, environment: dict):
        self.expression = expression
        self.environment = environment

    def step(self):
        self.expression = self.expression.reduce(self.environment)

    def run(self):
        while self.expression.reducible:
            print(self.expression)
            self.step()
        print(self.expression)
        return self.expression