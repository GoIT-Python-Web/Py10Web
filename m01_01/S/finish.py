class PersonInfo:

    def value_of(self):
        raise NotImplementedError


class PersonPhoneNumber(PersonInfo):
    def __init__(self, phone: str, operator_code: str):
        self.phone = phone
        self.operator_code = operator_code

    def value_of(self):
        return f"+38({self.operator_code}){self.phone}"


class PersonAddress(PersonInfo):
    def __init__(self, city: str, street: str, house: str):
        self.city = city
        self.street = street
        self.house = house

    def value_of(self):
        return f"{self.city}, {self.street}, {self.house}"


class Person:
    def __init__(self, name: str, phone: PersonPhoneNumber, address: PersonAddress):

        self.name = name
        self.phone = phone
        self.address = address

    def get_phone_number(self):
        return f"{self.name}: {self.phone.value_of()}"

    def get_address(self):
        return f"{self.name}: {self.address.value_of()}"


if __name__ == '__main__':
    phone = PersonPhoneNumber("9995544", "050")
    address = PersonAddress('Kyiv', 'Ploscha Svodody', '23/A')
    person = Person("Alexander", phone, address)
    print(person.get_phone_number())
    print(person.get_address())