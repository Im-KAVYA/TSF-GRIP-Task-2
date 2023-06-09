
# Importing necessary libraries
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  

from sklearn.cluster import KMeans

#importing data
df=pd.read_csv("/content/drive/MyDrive/TSP-GRIP/Iris.csv")

df.shape

df.head(10)

df.info()

df.describe()

df.isna().sum()

df=df.dropna()

df=df.drop_duplicates()

df.shape

df.groupby(df['Species']).count()

print(df['Species'].unique())

x=df.iloc[:,1:-1].values

#Finding the optimum number of clusters for k-means clustering

wcss=[]
for i in range(1,11):
  kmeans=KMeans(n_clusters=i,max_iter=300,n_init=10,random_state=0)
  kmeans.fit(x)
  wcss.append(kmeans.inertia_)

#Elbow Method
plt.plot(range(1, 11), wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS') #within cluster sum of squares
plt.show()

"""According to the elbow method, 3 is the optiaml number of clusters for the iris dataset"""

#K-Means Clustering
kmeans2 = KMeans(n_clusters=3,init='k-means++',max_iter = 300, n_init = 10, random_state = 42)
y_kmeans = kmeans2.fit_predict(x)

kmeans2.cluster_centers_[:,0]

#Visualising the clusters
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s=75,c = 'blue', marker='*')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s=75, c = 'orange', marker='p')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s=75, c = 'green' ,marker='o')

plt.xlabel("sepal length")
plt.ylabel("sepal width")

#Plotting the centroids of the clusters
plt.scatter(kmeans2.cluster_centers_[:, 0], kmeans2.cluster_centers_[:,1], s = 50, c = 'black', label = 'Centroids')

plt.legend()
plt.show()
