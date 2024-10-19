from random import randint
from time import sleep
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        self.transaction_number = 0

    def deposit(self):

        for i in range(100):
            random_amount = randint(50, 500)
            self.balance += random_amount
            self.transaction_number += 1
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Номер транзакции: {self.transaction_number}. Пополнение: {random_amount}. Баланс: {self.balance}\n")
            sleep(0.001)

    def take(self):

        for i in range(100):
            random_amount = randint(50, 500)
            print(f' Запрос на {random_amount}\n')
            self.transaction_number += 1
            if random_amount <= self.balance:
                self.balance -= random_amount
                print(f'Номер транзакции: {self.transaction_number}. Снятие {random_amount}. Баланс: {self.balance}\n')
            else:
                print(f'Запрос отклонён, недостаточно средств\n')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()  # создаем объект класса

th1 = Thread(target=bk.deposit)
th2 = Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
