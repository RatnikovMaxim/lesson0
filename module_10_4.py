from threading import Thread
from random import randint
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None
class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # sleep(randint(3, 10))
        sleep(0.1)
class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables
    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    guest.start()
                    print(f'{guest.name} сел(а) за стол номер {table.number}')
                    table.guest = guest
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')


    def discuss_guests(self):
        for guest in guests:
            for table in self.tables:
                if not self.queue.empty() or table.guest is not None:
                    if table.guest is not None and guest.is_alive():
                        print(f'{guest.name} покушал(-а) и ушел(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest = None
                        break
                    if not self.queue.empty() and table.guest is None:
                        print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        guest.start()
                        table.guest = self.queue.get(guest)
                        break


# Создание столов
tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# # Приём гостей
cafe.guest_arrival(*guests)
# # Обслуживание гостей
cafe.discuss_guests()
