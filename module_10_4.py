from queue import Queue
import threading
import time
from random import randint

#стол, хранит информацию о находящемся за ним гостем (Guest)
class Table:
    def __init__(self, number):
        self.number = number #номер стола
        self.guest = None    #имя гостя

#гость (поток)
class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        time.sleep(randint(3, 10)) #рандомная пауза

#кафе, в котором есть определённое кол-во столов и происходит имитация
# прибытия гостей (guest_arrival) и их обслуживания (discuss_guests).
class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()    #очередь
        self.tables = tables    #столы в этом кафе

    def guest_arrival(self, *guests):       #неограниченное кол-во гостей
        for guest in guests:                #выбираем гостей
            guest_fl = True                 #флаг, помогает определить, что все столы заняты
            for table in self.tables:       #смотрим столы
                if table.guest is None:     #если стол пустой
                    table.guest = guest     #садим гостя за стол
                    guest.start()           #запускаем поток гостя
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    guest_fl = False        #устанавливаем флаг занятого стола
                    break
            if guest_fl:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):               #процесс обслуживания гостей
        while not self.queue.empty() or any([table.guest for table in self.tables]):       #пока очередь не пустая
            for table in self.tables:       #проверяем столы
                if table.guest is not None and table.guest.is_alive() is False:
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()