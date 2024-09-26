import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self._enemies_left = 100
        self.days_of_battle = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self._enemies_left > 0:
            time.sleep(1)
            self.days_of_battle += 1
            self._enemies_left -= self.power
            if self._enemies_left <= 0:
                break
            else:
                print(f"{self.name} сражается {self.days_of_battle}..., осталось {self._enemies_left} воинов.")

        print(f'{self.name} одержал победу спустя {self.days_of_battle} дней(дня)!')

knight1 = Knight('Sir Lancelot', 10)
knight2 = Knight("Sir Galahad", 20)

# Запуск рыцарей
knight1.start()
knight2.start()

knight1.join()
knight2.join()

print('Все битвы закончились!')