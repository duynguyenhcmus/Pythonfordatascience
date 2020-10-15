## Load libraries ##
import pandas as pd
#import ML models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
# Import train_test_split function
from sklearn.model_selection import train_test_split
# Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
#Import libraries for cross validation
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

## 1. Loading Data ##
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
# Load dataset
path = 'https://raw.githubusercontent.com/duynguyenhcmus/Pythonfordatascience/main/Week01/Py4DS_Lab1_Dataset/diabetes.csv'
df = pd.read_csv(path, header=0, names=col_names)
print(df.head())
print(df.info())

## 2. Feature Selection ##
# Split dataset in features and target variable
feature_cols = ['pregnant', 'insulin', 'bmi', 'age', 'glucose', 'bp', 'pedigree']
X = df[feature_cols] # Feature
y = df.label # Target variable

## 3. Splitting Data ##
# Split dataset into training set and test set
# 70% training and 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

## 4. Building Decision Tree Model ##
# Create Decision Tree classifier object
clf = DecisionTreeClassifier()
# Train Decision Tree Classifier
clf = clf.fit(X_train, y_train)
# Predict the response for test dataset
y_pred = clf.predict(X_test)
# Model Accuracy, how often is the classifier corret?
print("Accuracy of decision tree: ", metrics.accuracy_score(y_test, y_pred))
# Evaluate a score by cross validation
scores = cross_val_score(clf, X, y, cv=5)
print("scores = {} \n final score = {} \n".format(scores, scores.mean()))

## 5. Building Random Forest Model ##
# Create Decision Tree classifier object
rdf = RandomForestClassifier()
# Train Decision Tree Classifier
rdf = rdf.fit(X_train, y_train)
# Predict the response for test dataset
y_pred = rdf.predict(X_test)
# Model Accuracy, how often is the classifier corret?
print("Accuracy of random forest: ", metrics.accuracy_score(y_test, y_pred))
# Evaluate a score by cross validation
scores = cross_val_score(rdf, X, y, cv=5)
print("scores = {} \n final score = {} \n".format(scores, scores.mean()))


## 6. Building Logistic Regression Model ##
# Create Decision Tree classifier object
lr = LogisticRegression(max_iter=2000)
# Train Decision Tree Classifier
lr = lr.fit(X_train, y_train)
# Predict the response for test dataset
y_pred = lr.predict(X_test)

## Evaluating Logistic Regression Model ##
# Model Accuracy, how often is the classifier corret?
print("Accuracy of logistic regression: ", metrics.accuracy_score(y_test, y_pred))
# Evaluate a score by cross validation
scores = cross_val_score(lr, X, y, cv=5)
print("scores = {} \n final score = {} \n".format(scores, scores.mean()))

