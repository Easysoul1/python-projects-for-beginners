# Pratice Exercises
# Question 1 Week 12
# Continuing the Data Analysis project

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report

# Load the dataset
data = pd.read_csv('./asset/iris.csv')

# Prepare the data
X = data.drop(columns=['species'])
y = data['species']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 1. Implement a decision tree classifier
decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)

# Predict using the decision tree classifier
y_pred_dt = decision_tree.predict(X_test)

# 2. Evaluate the model's performance using accuracy, precision, and recall
accuracy_dt = accuracy_score(y_test, y_pred_dt)
precision_dt = precision_score(y_test, y_pred_dt, average='weighted')
recall_dt = recall_score(y_test, y_pred_dt, average='weighted')

print("Decision Tree Classifier Performance:")
print(f"Accuracy: {accuracy_dt}")
print(f"Precision: {precision_dt}")
print(f"Recall: {recall_dt}")
print("\nClassification Report:\n", classification_report(y_test, y_pred_dt))

# 3. Use random forest classifier on iris dataset
random_forest = RandomForestClassifier(random_state=42)
random_forest.fit(X_train, y_train)

# Predict using the random forest classifier
y_pred_rf = random_forest.predict(X_test)

# Evaluate the random forest classifier's performance
accuracy_rf = accuracy_score(y_test, y_pred_rf)
precision_rf = precision_score(y_test, y_pred_rf, average='weighted')
recall_rf = recall_score(y_test, y_pred_rf, average='weighted')

print("\nRandom Forest Classifier Performance:")
print(f"Accuracy: {accuracy_rf}")
print(f"Precision: {precision_rf}")
print(f"Recall: {recall_rf}")
print("\nClassification Report:\n", classification_report(y_test, y_pred_rf))
