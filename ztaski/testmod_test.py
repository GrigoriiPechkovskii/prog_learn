import doctest

print('start')

t = []
def fun_test(w):
	'''
	Make fun test
	>>> x=4
	>>> fun_test(x)
	9
	'''
	e = w + 5
	t.append(w)
	return e, e+5
	
r = fun_test(5)

fun_test(5)
fun_test(5)
fun_test(5)
#doctest.testmod()

print('end')