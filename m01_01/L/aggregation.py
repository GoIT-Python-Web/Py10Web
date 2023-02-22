class Animal:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def get_info(self):
        return f"{self.nickname} {self.age}"


class Owner:
    def __init__(self, fullname, phone):
        self.fullname = fullname
        self.phone = phone

    def get_phone(self):
        return self.phone


class Cat(Animal):
    def __init__(self, nickname, age, owner: Owner):
        super().__init__(nickname, age)
        self.owner = owner

    def say(self):
        return f"{self.nickname} say meow!"


if __name__ == '__main__':
    contact = Owner('Andriy', '0500010101')
    cat = Cat('Borys', 2, contact)
    print(cat.owner.get_phone())



