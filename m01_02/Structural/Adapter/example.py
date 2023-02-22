class LegacySystem:
    def execute_operation(self, value_one, value_two, operation):
        if operation == 'add':
            return value_one + value_two
        elif operation == 'sub':
            return value_one - value_two
        else:
            raise ValueError('Unknown operation')


class NewSystem:
    def perfom_operation(self, operation, value_one, value_two):
        if operation == '+':
            return value_one + value_two
        elif operation == '-':
            return value_one - value_two
        else:
            raise ValueError('Unknown operation')


class Adapter:
    def __init__(self, adapted):
        self.adapted = adapted

    def perfom_operation(self, operation, value_one, value_two):
        if operation == '+':
            return self.adapted.execute_operation(value_one, value_two, 'add')
        elif operation == '-':
            return self.adapted.execute_operation(value_one, value_two, 'sub')
        else:
            raise ValueError('Unknown operation')


if __name__ == '__main__':
    ns = NewSystem()
    ls = Adapter(LegacySystem())

    res = ns.perfom_operation("+", 5, 3)
    print(res)

    res = ls.perfom_operation("-", 5, 3)
    print(res)
    