import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# parameters
k = 5
l = 100


df = pd.read_csv('.\\西瓜数据集4.0.csv')
df.drop(['编号'], axis=1, inplace=True)
df_sample = df.sample(n=k)


standard_nodes = []
for row_s in df_sample.itertuples():
    standard_nodes.append([row_s[1], row_s[2]])


for i in range(l):
    list_of_nodes = [[]for i in range(k)]

    for row_r in df.itertuples():
        drow_list = []
        for row_s in standard_nodes:
            x1, y1 = row_r[1], row_r[2]
            x2, y2 = row_s[0], row_s[1]
            drow = (x1-x2)**2+(y1-y2)**2
            drow_list.append(drow)
        
        a = drow_list.index(min(drow_list))
        list_of_nodes[a].append([row_r[1], row_r[2]])


    # visualization & update

    standard_nodes = []
    for i in range(k):
        mat = np.array(list_of_nodes[i])
        plt.scatter(mat[:,0],mat[:,1])
        m = np.mean(mat, axis=0)
        listm = list(m)
        standard_nodes.append(listm)
    print(standard_nodes)

plt.show()
    


