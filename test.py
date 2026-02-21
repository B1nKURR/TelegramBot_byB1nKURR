class Person:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self):
        print(f"{self.имя} совершает атаку!")


class Putesh(Person):
    def elem_attack(self):
        print(f"{self.имя} использует специальную атаку!")


pyt = Putesh("Путешественник", 10)

pyt.attack()  # Выводит: Путешественник совершает атаку!
pyt.elem_attack()