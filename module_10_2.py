from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = power

    def run(self):
        enemies = 100
        number_of_days = 0
        print(f'{self.name}, на нас напали!')
        for i in range(enemies):
            if enemies > 0:
                enemies -= self.power
                number_of_days += 1
                sleep(1)
                print(f"{self.name} сражается {number_of_days}..., осталось {enemies} воинов.")
                if enemies == 0:
                    print(f'{self.name} одержал победу спустя {number_of_days} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')
