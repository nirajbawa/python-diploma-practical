import pandas as pd
import numpy as np

def print_series():
    a = np.array(['A', 'B', 'C', 'D', 'E'])
    s = pd.Series(a)
    print(s)

def print_dataFrame():
    a = [[10,20],[30,40]]
    data_fr = pd.DataFrame(a)
    print(data_fr)

def print_dataFrameWithDict():
    dic = {
        'emp no':[101,102,103],
        'name':['AAA', 'BBB', 'CCC'],
        'salary':[10000,15000,25000]
    }
    
    data_fr = pd.DataFrame(dic)
    print(data_fr)

print_series()
print_dataFrame()
print_dataFrameWithDict()