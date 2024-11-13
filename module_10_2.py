import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.warrior = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        number_of_days = 0
        while self.warrior:
            time.sleep(1)
            self.warrior -= self.power
            number_of_days += 1
            print(f'\n{self.name} сражается {number_of_days}..., осталось {self.warrior} воинов.', end='')
        print(f'\n{self.name} одержал победу спустя {number_of_days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')