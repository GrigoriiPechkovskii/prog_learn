
import platform
platform.python_version()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import re
import sklearn
from sklearn.datasets import load_iris

print('start')

#plt.style.use('seaborn-whitegrid')


import matplotlib.pyplot as plt
'''
fig = plt.figure()
# Добавление на рисунок прямоугольной (по умолчанию) области рисования
ax = fig.add_axes([0, 0, 1, 1])
print (type(ax))
plt.scatter(0.1, 0.1)
plt.savefig('example 142a.png', fmt='png')


fig = plt.figure()
# Добавление на рисунок круговой области рисования
ax = fig.add_axes([0, 0, 1, 1], polar=True)
plt.scatter(0.0, 0.5)
plt.savefig('example 142b.png', fmt='png')



#plt.show()


x = np.linspace(0, 10, 100)
plt.figure()
# Создаем рисунок для графика
# Создаем первую из двух областей графика и задаем текущую ось
plt.subplot(1, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))# Создаем вторую область и задаем текущую ось

plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x),'--');



fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 10, 1000)
#x = np.array([0,1,2,3,4,5,6,7])
ax.plot(x, np.sin(x),linestyle='solid',label='sin(x)')
ax.plot(x, np.cos(x),'--g',label='cos(x)')

#plt.legend(framealpha=0)
plt.legend(facecolor='red')
'''

#plt.savefig('demo.png', transparent=True)
'''
x = np.linspace(0, 10, 1000)
ax = plt.axes()
ax.plot(x, np.sin(x),label='cos(x)')
ax.set(xlim=(0, 10), ylim=(-2, 2),xlabel='x', ylabel='sin(x)',title='A Simple Peot'); # Простая диаграмма
ax.legend()

rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
	plt.plot(rng.rand(5), rng.rand(5), marker,
		label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8)

rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
cmap='viridis')
plt.colorbar(); # Отображаем цветовую шкалу



from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T 
plt.scatter(features[0], features[1], alpha=0.2,
s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1]);

x = np.linspace(0, 1, 3)
dy = 10
q = np.array([1,5,10])
y = np.sin(x) + dy * np.random.randn(3)
plt.errorbar(x, y, yerr=q, fmt='o',ecolor='blue', color='red',elinewidth=30, capsize=10)


from sklearn.gaussian_process import GaussianProcess
# Описываем модель и отрисовываем некоторые данные
model = lambda x: x * np.sin(x)
xdata = np.array([1, 3, 5, 6, 8])
ydata = model(xdata)
# Выполняем подгонку Гауссова процесса
gp = GaussianProcess  (corr='cubic', theta0=1e-2, thetaL=1e-4,thetaU=1E-1, random_start=100)
gp.fit(xdata[:, np.newaxis], ydata)
xfit = np.linspace(0, 10, 1000)
yfit, MSE = gp.predict(xfit[:, np.newaxis], eval_MSE=True)
dyfit = 2 * np.sqrt(MSE) # 2*сигма ~ область с уровнем доверия 95%
plt.plot(xdata, ydata, 'or')
plt.plot(xfit, yfit, '-', color='gray')
plt.fill_between(xfit, yfit - dyfit, yfit + dyfit,
color='gray', alpha=0.2)
plt.xlim(0, 10)

def f(x, y):
	return np.sin(x) ** 10 + np.cos(10  * x) * np.cos(x)

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contour(X, Y, Z, colors='black');


plt.style.use('ggplot')

'''

data = np.random.randn(100)
data2 = data + 5
plt.hist(data, bins=100, alpha=1,color='blue',edgecolor='black');
plt.hist(data2, bins=100, alpha=1,color='red',edgecolor='black');

'''
plt.hist(data, bins=300, normed=True, alpha=1,
histtype='stepfilled', color='steelblue',
edgecolor='none');




fig1 = plt.figure()   # Создание объекта Figure
print (fig1.axes)   # Список текущих областей рисования пуст
print (type(fig1))   # тип объекта Figure
plt.scatter(1.0, 1.0)   # scatter - метод для нанесения маркера в точке (1.0, 1.0)
plt.figure()
# После нанесения графического элемента в виде маркера
# список текущих областей состоит из одной области
print (fig1.axes)
'''

plt.show()

print('end')