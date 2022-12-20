#Дан список чисел. Вернуть список, где при помощи функции map() переведется в строку с помощью lambda функции

numbers = [12, 5, 6, 7, 10]
result = map(lambda x:x, numbers)
print(list(result))

#Написать декоратор к 2-м любым функциям, который бы считал и вывоил время их выполнения

from datetime import datetime
import time

def time_decorator(my_function):
    def wrapper():
        start = float(datetime.now().strftime("%S"))
        my_function()
        end = float(datetime.now().strftime("%S"))
        print(end - start)
    return wrapper

@time_decorator
def time_sleep():
    time.sleep(5)

time_sleep()

#задача 3,4 09.12

import json
import csv

with open("zadacha.json") as f:
    date = json.loads(f.read())
    keys = list(date.keys())
    values = list(date.values())
    print(keys)
    print(values)
    with open("data.csv","w") as csvfile:
        writer = csv.writer(csvfile,quotechar ="\n")

        writer.writerow(keys)
        writer.writerow(values)
