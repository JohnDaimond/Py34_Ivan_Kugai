import random
print ("Игра Камень, ножницы, бумага. Условные обозначения:")
print ("1- Камень, 2- Ножницы, 3 - Бумага")

user = int(input("Введите число\n"))

if user == 1:
	print('Вы выбрали Камень\n')
elif user == 2:
	print('Вы выбрали Ножницы\n')
elif user == 3:
	print('Вы выбрали Бумага\n')

bot = random.randint(1,3)

if bot ==1:
	print('Выбор бота Камень\n')
elif bot ==2:
	print('Выбор бота Ножницы\n')
elif bot ==3:
	print('Выбор бота Бумага\n')

if bot == user:
	print('Ничья\n')
elif bot ==1 and user ==2 or bot ==2 and user==3 or bot==3 and user==1:
	print('Бот выиграл\n')
elif bot ==2 and user==1 or bot==3 and user==2 or bot==1 and user==3:
	print('Вы выиграли\n')