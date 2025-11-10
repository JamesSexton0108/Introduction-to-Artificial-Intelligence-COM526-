from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, matthews_corrcoef, \
    confusion_matrix, ConfusionMatrixDisplay
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv("titanic_new.csv")

X = data.drop(["Survived"], axis=1)
y = data["Survived"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

#KNN
knn = KNeighborsClassifier(n_neighbors=3)

knn_model = knn.fit(X_train, y_train)

knn_pred = knn_model.predict(X_test)

print(f"KNN Accuracy is {accuracy_score(y_test, knn_pred)}")
print(f"KNN Recall is {recall_score(y_test, knn_pred)}")
print(f"KNN Specificity is {recall_score(y_test, knn_pred, pos_label=0)}")
print(f"KNN Precision is {precision_score(y_test, knn_pred)}")
print(f"KNN F1-Score is {f1_score(y_test, knn_pred)}")
print(f"KNN MCC is {matthews_corrcoef(y_test, knn_pred)}\n")

cm = confusion_matrix(y_test, knn_pred, labels=knn_model.classes_)
cm_visual = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=knn_model.classes_)
cm_visual.plot()
plt.show()

#SVM
svm = svm.SVC()

svm_model = svm.fit(X_train, y_train)

svm_pred = svm_model.predict(X_test)

print(f"SVM Accuracy is {accuracy_score(y_test, svm_pred)}")
print(f"SVM Recall is {recall_score(y_test, svm_pred)}")
print(f"SVM Specificity is {recall_score(y_test, svm_pred, pos_label=0)}")
print(f"SVM Precision is {precision_score(y_test, svm_pred)}")
print(f"SVM F1-Score is {f1_score(y_test, svm_pred)}")
print(f"SVM MCC is {matthews_corrcoef(y_test, svm_pred)}\n")

# See the confusion matrix
cm = confusion_matrix(y_test, svm_pred, labels=svm_model.classes_)
cm_visual = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=svm_model.classes_)
cm_visual.plot()
plt.show()

#Decision Tree
dt = DecisionTreeClassifier()

dt_model = dt.fit(X_train, y_train)

dt_pred = dt_model.predict(X_test)

print(f"DT Accuracy is {accuracy_score(y_test, dt_pred)}")
print(f"DT Recall is {recall_score(y_test, dt_pred)}")
print(f"DT Specificity is {recall_score(y_test, dt_pred, pos_label=0)}")
print(f"DT Precision is {precision_score(y_test, dt_pred)}")
print(f"DT F1-Score is {f1_score(y_test, dt_pred)}")
print(f"DT MCC is {matthews_corrcoef(y_test, dt_pred)}\n")

# See the confusion matrix
cm = confusion_matrix(y_test, dt_pred, labels=dt_model.classes_)
cm_visual = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=svm_model.classes_)
cm_visual.plot()
plt.show()

#Random Forest
rf = RandomForestClassifier(max_depth=5, random_state=0)

rf_model = rf.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

print(f"RF Accuracy is {accuracy_score(y_test, rf_pred)}")
print(f"RF Recall is {recall_score(y_test, rf_pred)}")
print(f"RF Specificity is {recall_score(y_test, rf_pred, pos_label=0)}")
print(f"RF Precision is {precision_score(y_test, rf_pred)}")
print(f"RF F1-Score is {f1_score(y_test, rf_pred)}")
print(f"RF MCC is {matthews_corrcoef(y_test, rf_pred)}\n")

# See the confusion matrix
cm = confusion_matrix(y_test, rf_pred, labels=rf_model.classes_)
cm_visual = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=svm_model.classes_)
cm_visual.plot()
plt.show()

#Neural Network NOT WORKING
nn = MLPClassifier()

nn_model = nn.fit(X_train, y_train)

nn_pred = nn_model.predict(X_test)

print(f"NN Accuracy is {accuracy_score(y_test, nn_pred)}")
print(f"NN Recall is {recall_score(y_test, nn_pred)}")
print(f"NN Specificity is {recall_score(y_test, nn_pred, pos_label=0)}")
print(f"NN Precision is {precision_score(y_test, nn_pred)}")
print(f"NN F1-Score is {f1_score(y_test, nn_pred)}")
print(f"NN MCC is {matthews_corrcoef(y_test, nn_pred)}\n")

# See the confusion matrix
cm = confusion_matrix(y_test, nn_pred, labels=nn_model.classes_)
cm_visual = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=svm_model.classes_)
cm_visual.plot()
plt.show()

print("Accuracy = TP + TN/TP + TN + FP + FN")
print("Recall = TP/TP + FN")
print("Specificity = TN/TN + FP")
print("Precision = TP/TP + FP")
print("F1-Score = 2((Precision x Recall)/(Precision + Recall))")
print("MCC = (TP x TN) – (FP x FN)/sqrt((TP + FP) x (TP + FN) x (TN + FP) x (TN + FN))")