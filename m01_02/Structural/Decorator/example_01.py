class Greeting:
    def __init__(self, username):
        self.username = username

    def greet(self):
        return f"Hello {self.username}"


class GreetingDecorator:
    def __init__(self, wrapper):
        self.wrapper = wrapper

    def greet(self):
        base_greet = self.wrapper.greet()
        base_greet = base_greet.upper()
        return base_greet


if __name__ == '__main__':
    msg = GreetingDecorator(Greeting('Oleg'))
    print(msg.greet())

