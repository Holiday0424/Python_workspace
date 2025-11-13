import numpy as np #pandas也需要与numpy相结合
import pandas as pd
print(f"np.nan的值为:\n{np.nan}\n----------")

#Series创建
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(f"Series对象s的值:\n{s}")



print('{0} {1}'.format('Hello', 'Python'))

table = {'Sjoerd': 123, 'Jack': 456, 'Dcab': 789}
for name, phone in table.items():print('{0:10} ==> {1:10d}'.format(name, phone))