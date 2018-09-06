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

class FirstClass(): # Определяет объект класса
	def setdata(self, value): # Определяет метод класса
		self.data = value # self – это экземпляр
	def display(self):
		print(self.data)


class Person:
	def __init__(self, name, job, pay): # Конструктор принимает 3 аргумента
		self.name = name # Заполняет поля при создании
		self.job = job # self – новый экземпляр класса
		self.pay = pay
class q():
    def __init__(self,data):

        self.data = data
    def summ(self):
        return self.__data *2


"""
Адаптер - паттерн, структурирующий классы и объекты.
Преобразует интерфейс одного класса в интерфейс другого, который ожидают клиенты.
Адаптер обеспечивает совместную работу классов с несовместимыми интерфейсами, которая без него была бы невозможна.
"""


class Dog(object):
    def __init__(self, name):
        self._name = name

    def bark(self):
        return '%s: гав-гав!' % self._name


class Cat(object):
    def __init__(self, name):
        self._name = name

    def meow(self):
        return '%s: мяу-мяу!' % self._name


class CatAdapter(Dog):
    # благодаря адаптеру мы можем использовать
    # интерфейс класса `Dog`, а реализацию класса `Cat`.

    def __init__(self, name):
        super(CatAdapter, self).__init__(name=name)
        self._cat = Cat(name=name)

    def bark(self):
        # запрос `bark` преобразуется в запрос `meow`
        return self._cat.meow()


dog = Dog('Тузик')
print (dog.bark())  # Тузик: гав-гав!

dog = CatAdapter('Тузик')
print (dog.bark())  # Тузик: мяу-мяу!