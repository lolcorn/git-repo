import requests
import matplotlib.pyplot as plt

response = requests.get('https://api.github.com')

print("Статус код:", response.status_code)
print("Содержимое:", response.json())

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')

plt.title('Визуализация простого линейного графика')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()

plt.show()