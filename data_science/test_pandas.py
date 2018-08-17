import numpy as np
import pandas as pd
import time
#import matplotlib as plt
import matplotlib.pyplot as plt
#print(pd.__version__)
data = pd.Series([0.25, 0.5, 0.75,1], ['a','b','c','d'])
#print(data)

area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
'Florida': 170312, 'Illinois': 149995}
area = pd.Series(area_dict)
#print(area)

population_dict = {'California': 38332521,
'Texas': 26448193,
'New York': 19651127,
'Florida': 19552860,
'Illinois': 12882135}
population = pd.Series(population_dict)
population

states = pd.DataFrame({'population': population,
'area': area})
#print(states)

pd.DataFrame(population, columns=['population'])

data = [{'a': i, 'b': 2 * i}
for i in range(3)]
pd.DataFrame(data)

pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])



area = pd.Series({'California': 423967, 'Texas': 695662,
'New York': 141297, 'Florida': 170312,
'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
'New York': 19651127, 'Florida': 19552860,
'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})
data

vals2 = np.array([1, np.nan, 3, 4])
vals2.dtype

print('end')

area2 = pd.Series({'California2': '123', 'Texas2': '34',
'New York2': '1232', 'Florida2': '2343',
'Illinois2': '2312'},dtype ='<U1')

q = {'California': '423967', 'Texas': '695662',
'New York': '141297', 'Florida': '170312',
'Illinois': '149995'}

def tt( ):
    for i in q.values():
        o=i

time_start = time.time()
for i in range(100000):
    tt()
time_end = time.time()
print('1===',time_end-time_start)