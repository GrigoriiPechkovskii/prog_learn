print('start')
import networkx as nx
import matplotlib.pyplot as plt

class SequenceFasta():
	'''Processes a fasta file'''
	def __init__(self,file_dir):
		self.file_dir=file_dir
		self.name_lst = []
		self.seq_lst = []
	def just_named(self):
		'''Works only with sequence names'''
		with open(self.file_dir) as file_opened:
			for line in file_opened:
				if '>' in line:
					self.name_lst.append(line)
	def seq_process(self,strip=False):
		seq_tmp = ''
		with open(self.file_dir) as file_opened:
			for line in file_opened:
				if '>' in line:							
					self.seq_lst.append(seq_tmp)
					seq_tmp = ''
					if strip:
						self.name_lst.append(line[1:].rstrip())
					else:
						self.name_lst.append(line[1:])	
				else:
					if strip:
						seq_tmp += line.rstrip()
					else:
						seq_tmp += line
		self.seq_lst.append(seq_tmp)
		del self.seq_lst[0]
		

sample = SequenceFasta('rosalind_grph.txt')
sample.seq_process(strip=True)

prefix,suffix = {},{}
k = 3

for index in range(len(sample.name_lst)):
	prefix[sample.name_lst[index]] = sample.seq_lst[index][:k]
	suffix[sample.name_lst[index]] = sample.seq_lst[index][-k:]

graph = []

for suffix_key, suffix_val in suffix.items():
	for prefix_key, prefix_val in prefix.items():
		if suffix_val==prefix_val and suffix_key!=prefix_key:
			graph.append([suffix_key,prefix_key])
for edge in graph:
	for node in edge:
		print(node,end=' ')
	print()
	



G = nx.Graph()
G.add_edges_from(graph)
nx.draw(G,with_labels=False)

plt.show()

print('end')