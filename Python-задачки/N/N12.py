"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе
должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()),
умножение (mul()), деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
---
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
клеток.
---
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
---
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
этих двух клеток.
---
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
---
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке
https://pythonworld.ru/osnovy/peregruzka-operatorov.html
"""


class Cell:

    def __init__(self, cells_num=0):
        self.quantity = cells_num

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        res = self.quantity - other.quantity
        if res >= 0:
            return Cell(self.quantity - other.quantity)
        else:
            print('Значение меньше 0!')

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, n_in_row):
        rows = self.quantity // n_in_row
        for i in range(rows):
            print('*' * n_in_row)
        print('*' * (self.quantity % n_in_row))
        print('-' * 15)


a = Cell(15)
a.make_order(7)
b = Cell(7)
b.make_order(3)

# сложение
c = a + b
c.make_order(9)

# вычитание
d = c - a
d.make_order(2)

# умножение
e = d * b
e.make_order(10)

# целочисленное деление
# f = e // a
# f.make_order(2)

a += b
a.make_order(3)
