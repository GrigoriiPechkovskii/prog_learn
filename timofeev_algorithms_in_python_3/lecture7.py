#Рекурсия

print('start')

def matreshka(n):
	if n == 1:
		print("matreshechka")
	else:
		print("up matreshka n = ",n)
		matreshka(n-1)
		print('down matreshka n = ',n)


import graphics as gr 

#window = gr.GraphWin("Russia game",600,600)
alpha = 0.05

def fractal_rectangle(A, B, C, D, deep=10):
	if deep < 1:
		return
	for M, N in (A, B), (B, C), (C, D), (D, A):
		gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
	A1 = (A[0]*(1-alpha) + B[0]*alpha, A[1]*(1-alpha) + B[1]*alpha)
	B1 = (B[0]*(1-alpha) + C[0]*alpha, B[1]*(1-alpha) + C[1]*alpha)
	C1 = (C[0]*(1-alpha) + D[0]*alpha, C[1]*(1-alpha) + D[1]*alpha)
	D1 = (D[0]*(1-alpha) + A[0]*alpha, D[1]*(1-alpha) + A[1]*alpha)
	fractal_rectangle(A1, B1, C1, D1, deep-1)

#fractal_rectangle((100,100), (500,100), (500,500), (100,500),50)

def f(n:int):
	assert n>=0, 'Factorial is not defined'
	if n == 0:
		return 1
	return f(n-1)*n

print(f(5))

def gcd(a,b):
	'''Алгориттм Евклида'''
	if a==b:
		return a
	elif a > b:
		return gcd(a-b,b)
	else: #a < b
		return gcd(a,b-a)

def gcd(a,b):
	if b==0:
		return a
	else: #a < b
		return gcd(b,a%b)

def gcd(a,b):
	return a if b == 0 else gcd(b,a%b)

print(gcd(10,15))

#быстрое возведение в степень
def pow(a:float,n:int):
	if n == 0:
		return 1
	else:
		return pow(a,n-1)*a

def pow2(a:float,n:int):
	if n == 0:
		return 1
	elif n%2 == 1: #нечетные
		return pow(a,n-1)*a
	else: #четное
		return pow(a**2,n//2)

print('end')