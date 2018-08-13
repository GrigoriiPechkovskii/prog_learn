print('start')
import time
class hero():
	q = 33333
	#self.health = health + 111
	def __init__(self,health,manna):		
		self.health = health
		self.manna = manna
		print(self.q)
	def __myinit__(self):
		print(123213212231)
	def show_status(self):
		a = 1111
		print('health = ', self.health)
		print('manna = ', self.manna)


def show_status2(health):
	print('health', health)  


orc = hero(1000,0)
elf = hero(50,100)
#orc.show_status()
print('end')

class FirstClass: # Определяет объект класса
	def setdata(self, value): # Определяет метод класса
		self.data = value # self – это экземпляр
	def display(self):
		print(self.data)


class Person:
	def __init__(self, name, job, pay): # Конструктор принимает 3 аргумента
		self.name = name # Заполняет поля при создании
		self.job = job # self – новый экземпляр класса
		self.pay = pay