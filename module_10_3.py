import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            random_dep = randint(50, 500)
            self.balance += random_dep
            print(f'Пополнение: {random_dep}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            random_take = randint(50, 500)
            print(f'Запрос на {random_take}')
            if random_take <= self.balance:
                self.balance -= random_take
                print(f'Снятие: {random_take}. Баланс: {self.balance}')
            else:
                self.lock.acquire()
                print('Запрос отклонён, недостаточно средств')


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')