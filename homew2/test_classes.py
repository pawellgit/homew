class Second:
    color = "red"

    def changecolor(self, newcolor):
        self.color = newcolor

obj1 = Second()

print(obj1.color)  # вывод на экран "red circle"

obj1.changecolor("green")  # изменение цвета первого объекта

print(obj1.color)  # вывод на экран "green circle"
