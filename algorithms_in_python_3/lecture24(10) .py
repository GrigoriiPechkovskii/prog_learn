print('start24')

def dfs(vertex,G,used)#,used=None):
    '''Depth-first search'''
    #if used is None:
    #    used =set()
    #used = used or set()
    used.add(vertex)
    for neighbour in G[vertex]:
        if neighbour not in used:
            dfs(neighbour,G,used)

used = set()
N = 0

for vertex in G:
    if vertex not in used:
        dfs(vertex,G,used)
        N +=1 

print(N)

print('end24')
    