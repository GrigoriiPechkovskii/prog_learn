print('start23')

#Lecture

# for G A_B_C_D
#
V = {'A','B','C','D'}
E = {('A','B'),('B','C'),('C','D')}

#matrix    
V = ['A','B','C','D']
index = {V[i]:i for i in range(len(V))}

A = [[0,1,0,0],
     [1,0,1,0],
     [0,1,0,1],
     [0,0,1,0]]
#adjacency list
G = {'A':{'B'},
     'B':{'A','C'},
     'C':{'B','D'},
     'D':{'C'}}

v = 'A' 
for neighbor in G[v]:
    print('neighbor is',neighbor)

#input for matrix
M,N = [int(x) for x in input().split()]
V = []
index = {}
A = [[0]*N for i in range(N)]
for i in range(M):
    v1,v2 = input().split()
    for v in v1,v2:
        if v not in index:
            V.append(v)
            index[v] = len(V)-1
    v1_i = index[v1]
    v2_i = index[v2]
    A[v1_i][v2_i] = 1
    A[v2_i][v1_i] = 1

#input for adjacency list
M,N = [int(x) for x in input().split()]
G = {}
for i in range(N):
    v1,v2 = input().split()
    for v,u in (v1,v2),(v2,v1):
        if v not in G:
            G[v] = {u}
        else:
            G[v].add(u)

#compact adjacency list unchangeable graph
'''
0:1
1:0,2,3
3:1,2,4
4:3
''' 
edges = [1,0,2,3,1,3,1,2,4,3]
offset = [0,1,4,6,9,10]
#edges[offset[i]:offset[i+1]]
print('end23')
    