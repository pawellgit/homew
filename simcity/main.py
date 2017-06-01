class house:
    def __init__(self, people):
        self.people = int(people)

    def __str__(self):
        return "{} жителей".format(self.people)

class street:
    def __init__(self, name):
        self.name = name
        self._houses = []
        self._people = 0

    def add(self, house):  # добавление дома на улицу
        self._houses.append(house)
        #self._people += house.people
        print()

    def get_house(self, number):  # поиск дома на улице
        return (self._houses[number])

    def del_house(self, number):  # удаление дома с улицы
        self._houses.pop(number)

    def count(self):
        return len(self._houses)

petrovka = street('Petrovka')
petrovka.add(10)
petrovka.add(20)
petrovka.add(30)


print(petrovka.get_house(0))

petrovka.del_house(0)

print(petrovka.get_house(0))