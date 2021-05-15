class Animal:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


if __name__ == '__main__':
    dog = Animal('bumbly', 4)
    cat = Animal('billy', 5)

    print(f'Dog\'s name is {dog.name}, and they are {dog.age} years old!')
    print(f'Cat\'s name is {cat.name}, and they are {cat.age} years old!')
    msg = 'Dog name is {name}'.format(name=dog.name)
    print(msg)
