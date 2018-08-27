import os
print('start gener')

directory = os.getcwd()
files = os.listdir(directory)
def gen():
	for file in files:
		if file.endswith('.aln'):
			yield file
	
for i in gen():
	print(i)


print('end gener')