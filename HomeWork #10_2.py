# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Потоки на классах"

import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)
        self.num_enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        counter_day = 0
        while self.num_enemies > 0:
            time.sleep(1)
            counter_day += 1
            self.num_enemies -= self.power
            print(f"{self.name} сражается {counter_day}..., "
                  f"осталось {self.num_enemies} воинов.")
        print(f"{self.name} одержал победу спустя {counter_day} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
first_knight.start()

second_knight = Knight("Sir Galahad", 20)
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
