from time import sleep
from threading import Thread
from datetime import datetime

time_start_def = datetime.now()
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write('Какое-то слово № ' + str(i) + '\n')
            sleep(0.1)
    print('Завершилась запись в файл ' + file_name)

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end_def = datetime.now()
print(f'Работа потоков {time_end_def - time_start_def}')

time_start_Thrd = datetime.now()

t1 = Thread(target=write_words, args=(10, 'example5.txt'))
t2 = Thread(target=write_words, args=(30, 'example6.txt'))
t3 = Thread(target=write_words, args=(200, 'example7.txt'))
t4 = Thread(target=write_words, args=(100, 'example8.txt'))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

time_end_Thrd = datetime.now()
print(f'Работа потоков {time_end_Thrd - time_start_Thrd}')