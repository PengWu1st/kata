class Machine:
    def __init__(self, statement, environment: dict):
        self.statement = statement
        self.environment = environment

    def step(self):
        self.statement, self.environment = self.statement.reduce(self.environment)

    def run(self):
        while self.statement.reducible:
            print(self.statement)
            self.step()
        print(self.statement, self.environment)
        return self.statement
