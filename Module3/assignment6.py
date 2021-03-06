import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
df = pd.read_csv('/home/alberto/workspace/DAT210x/Module3/Datasets/wheat.data')


#
# TODO: Drop the 'id' feature
# 
# .. your code here ..
df_drop = df.drop(df.columns[[0]], axis=1) 

#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..
df_drop.corr()
#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..

plt.imshow(df_drop.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df_drop.columns))]
plt.xticks(tick_marks, df_drop.columns, rotation='vertical')
plt.yticks(tick_marks, df_drop.columns)

plt.show()

