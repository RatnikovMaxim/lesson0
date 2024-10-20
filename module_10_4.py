from threading import Thread
from random import randint
from time import sleep
import queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None
        # print(number)

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name


    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *queue):
        self.queue = queue
        self.tables = tables
        # print(queue)
#
    def guest_arrival(self, *guests):
        self.guests = guests
        tg1 = Guest(self.guests)
        tg1.start()
        tg1.join()
        

#
#
#
#     def discuss_guests(self):
#         pass



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# print(tables)
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]
# print(guests_names)
# print(guests)
# Заполнение кафе столами
cafe = Cafe(*tables)
# print(cafe)
# # Приём гостей
cafe.guest_arrival(*guests)
# # Обслуживание гостей
# cafe.discuss_guests()