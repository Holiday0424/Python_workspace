import pandas as pd
from numpy import ndarray

#Series对象
series = pd.Series([1,2,3,4,5],name ='A')
print(series)

#自定义索引
custom_index = [1,2,3,4,5]
Series_with_index = pd.Series([1,2,3,4,5],index = custom_index,name = 'A')
print(Series_with_index)


#DataFrame对象
#1-使用列表创建
data = [['Google',10],['Runoob',12],['Wiki',13]]
df = pd.DataFrame(data,columns=['Site','Age'])
df['Site'] =df['Site'].astype(str)
df['Age'] =df['Age'].astype(int)
#2-使用字典创建
data ={'Site':['Google','Runoob','Wiki'],'Age':[10,12,13]}
df = pd.DataFrame(data)
#3-使用ndarrays创建
import numpy as np
ndarray_data =np.array([
    ['Google', 10],
    ['Runoob', 12],
    ['Wiki', 13]
])
df=pd.DataFrame(ndarray_data,columns=['Site','Age'],index=[0,1,3])

print(df.loc[1])#第二行
print(df.iloc[1:2])#指定索引
#查看前2行数据
print(df.head(2))
#查看基本信息
print(df.info())
#排序
print(df.sort_values('Age',ascending=False))
# 计算分组统计（按城市分组，计算平均年龄）
print(df.groupby('City')['Age'].mean())
# 按索引选择行
print(df.iloc[1:3])  # 选择第二到第三行（按位置）

# 按标签选择行
print(df.loc[1:2])  # 选择第二到第三行（按标签）
# 计算分组统计（按城市分组，计算平均年龄）
print(df.groupby('City')['Age'].mean())

# 处理缺失值（填充缺失值）
df['Age'] = df['Age'].fillna(30)

# 导出为 CSV 文件
df.to_csv('output.csv', index=False)

#Excel读取
df = pd.read_excel('output.xlsx')
df = pd.read_excel('output.xlsx',sheet_name='Sheet1')
dfs = pd.read_excel('output.xlsx',sheet_name=['Sheet1','Sheet2'])
# 自定义列名并跳过前两行
df = pd.read_excel('data.xlsx', header=None, names=['A', 'B', 'C'], skiprows=2)
print(df)



#Excel写入
df = pd.DataFrame({
'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, 30, 35],
'City': ['New York', 'Los Angeles', 'Chicago']
})
# 将 DataFrame 写入 Excel 文件，写入 'Sheet1' 表单
df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
# 写入多个表单，使用 ExcelWriter
with pd.ExcelWriter('output.xlsx') as writer:
df.to_excel(writer, sheet_name='Sheet1', index=False)
df.to_excel(writer, sheet_name='Sheet2', index=False)


