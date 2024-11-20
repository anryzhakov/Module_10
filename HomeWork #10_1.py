# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Введение в потоки"

from threading import Thread
from time import sleep
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово №{i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time = datetime.now()
print(start_time)
write_words(10, 'file_1_1.txt')
write_words(30, 'file_1_2.txt')
write_words(200, 'file_1_3.txt')
write_words(100, 'file_1_4.txt')
print('Продолжительность последовательной работы функций',
      datetime.now() - start_time)

start_time = datetime.now()
print(start_time)
thread1 = Thread(target=write_words, args=(10, 'file_2_1_.txt'))
thread2 = Thread(target=write_words, args=(30, 'file_2_2.txt'))
thread3 = Thread(target=write_words, args=(200, 'file_2_3.txt'))
thread4 = Thread(target=write_words, args=(100, 'file_2_4.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

print('Продолжительность работы потоков', datetime.now() - start_time)
