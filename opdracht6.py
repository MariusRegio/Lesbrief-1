class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = person(input("Wat is persoon eens naam?"), int(
    input("Wat is de leeftijd van persoon een?")))
p2 = person(input("Wat is persoon twee naam?"), int(
    input("Wat is de leeftijd van persoon twee?")))

print(p1.name if p1.age > p2.age else p2.name,
      "is ourder dan", p1.name if p1.age < p2.age else p2.name)
