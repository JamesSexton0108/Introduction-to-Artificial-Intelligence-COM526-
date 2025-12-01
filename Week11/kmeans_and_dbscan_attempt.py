from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np


#titanic = pd.read_csv("titanic_new.csv")
#employees = pd.read_csv("Employee.csv")
iris = pd.read_csv("iris.csv")

#iris
X = iris.drop(["species"], axis=1)
y = iris["species"]


kmeans = KMeans(n_clusters=3).fit(X)
dbscan = DBSCAN(eps=0.5, min_samples=3).fit(X)

iris["kmeans"]=kmeans.labels_
iris["DBSCAN"]=dbscan.labels_
#print(iris.to_string())



types = iris["species"].unique()

for flower in types:
    specific = iris[iris["species"] == flower]
    plt.scatter(specific["petal_length"], specific["petal_width"], label=flower)



for flower in types:
    specific = iris[iris["species"] == flower]
    plt.scatter(specific["kmeans"], specific["DBSCAN"], label=flower)

plt.legend(types)
plt.show()








