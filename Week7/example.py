from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load in the dataset from CSV using Pandas
data = pd.read_csv("iris.csv")

X = data.drop(["species"], axis=1)
y = data["species"]

# Split data into training samples and test samples
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a decision tree classifier
dt = DecisionTreeClassifier()

# Train Decision Tree Classifier
dt_model = dt.fit(X_train, y_train)

# Test the model against the test data
dt_pred = dt_model.predict(X_test)

print(f"Decision Tree accuracy is {accuracy_score(y_test, dt_pred)}")

# ------- New example with KNN, using same dataset -----

# Create a KNN classifier
neigh = KNeighborsClassifier(n_neighbors=3)

knn_model = neigh.fit(X, y)

knn_pred = knn_model.predict(X_test)

print(f"KNN accuracy is {accuracy_score(y_test, knn_pred)}")

#Attempt using Support Vector Machine
SVM = svm.SVC()

SVM.fit(X_train, y_train)

SVC_pred = SVM.predict(X_test)

print(f"SVM accuracy is {accuracy_score(y_test, SVC_pred)}")

#Attempt using Random Forest
RandomForest = RandomForestClassifier(max_depth=2, random_state=0)

RandomForest.fit(X_train, y_train)

RandomForest_pred = RandomForest.predict(X_test)

print(f"Random Forest accuracy is {accuracy_score(y_test, RandomForest_pred)}")