# **************************************Processed data START **********************************************************
import pandas
import numpy
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer

# load data
url = "/Users/uboh/Desktop/Machine Learning/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)


#process missing values in training and testing sets and replace wtih mean
dataframe[['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age']] = \
    dataframe[['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age']].replace(0,numpy.NaN)
array = dataframe.values
imputer = Imputer()
transformed_array = Imputer(missing_values='NaN', strategy='mean')
transformed_array = imputer.fit_transform(array)
print(pandas.isnull(transformed_array.sum))

#split data into array elements
X = transformed_array[:,0:8]
Y = transformed_array[:,8]

# split data into trains and testing sets with a ration of 0.8 to training
X_train_D1, X_test_D2 = train_test_split(X, test_size=0.2)
Y_train_D1, Y_test_D2 = train_test_split(Y, test_size=0.2)

# Select 5 feature on D1 with chi2 to conduct D3
test = SelectKBest(score_func=chi2, k=5)
fit = test.fit(X_train_D1, Y_train_D1)

# Building a classifier on D3
model = svm.SVC(gamma=0.001)
kfold = KFold(n_splits=3, random_state=7)

result_precision_training_1 = cross_val_score(model, X_train_D1, Y_train_D1, cv=kfold, scoring='precision')
result_recall_training_1 = cross_val_score(model, X_train_D1, Y_train_D1, cv=kfold, scoring='recall')
result_F_score_training_1 = cross_val_score(model, X_train_D1, Y_train_D1, cv=kfold, scoring='f1')

print("Results from processed training data:")
print("Precision: "),print(result_precision_training_1.mean())
print("Recall: "),print(result_recall_training_1.mean())
print("F-Score: "),print(result_F_score_training_1.mean())

# Testing the classifier on D2 and evaluate the results with precision, recall and F-score
result_precision_testing_1 = cross_val_score(model, X_test_D2, Y_test_D2, cv=kfold, scoring='precision')
result_recall_testing_1 = cross_val_score(model, X_test_D2, Y_test_D2, cv=kfold, scoring='recall')
result_F_score_testing_1 = cross_val_score(model, X_test_D2, Y_test_D2, cv=kfold, scoring='f1')

print("Results from processed testing data:")
print("Precision: "),print(result_precision_testing_1.mean())
print("Recall: "),print(result_recall_testing_1.mean())
print("F-Score: "),print(result_F_score_testing_1.mean())

# *****************************************Processed data END ********************************************************


# **************************************Un-Processed data START *******************************************************
import pandas
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn import svm
from sklearn.model_selection import train_test_split

# load data
url = "/Users/uboh/Desktop/Machine Learning/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values

#split data into array elements
X = array[:,0:8]
Y = array[:,8]

# split data into trains and testing sets with a ration of 0.8 to training
X_train_D1, X_test_D2 = train_test_split(X, test_size=0.2)
Y_train_D1, Y_test_D2 = train_test_split(Y, test_size=0.2)

# Select 5 feature on D1 with chi2 to conduct D3
test = SelectKBest(score_func=chi2, k=5)
fit = test.fit(X_train_D1, Y_train_D1)

# Building a classifier on D3
model = svm.SVC(gamma=0.001)
kfold = KFold(n_splits=3, random_state=7)

result_precision_training_2 = cross_val_score(model, X_train_D1, Y_train_D1, cv=kfold, scoring='precision')
result_recall_training_2 = cross_val_score(model, X_train_D1, Y_train_D1, cv=kfold, scoring='recall')
result_F_score_training_2 = cross_val_score(model, X_train_D1, Y_train_D1, cv=kfold, scoring='f1')

print("Results from unprocessed training data:")
print("Precision: "), print(result_precision_training_2.mean())
print("Recall: "),print(result_recall_training_2.mean())
print("F-Score: "),print(result_F_score_training_2.mean())

# Testing the classifier on D2 and evaluate the results with precision, recall and F-score
result_precision_testing_2 = cross_val_score(model, X_test_D2, Y_test_D2, cv=kfold, scoring='precision')
result_recall_testing_2 = cross_val_score(model, X_test_D2, Y_test_D2, cv=kfold, scoring='recall')
result_F_score_testing_2 = cross_val_score(model, X_test_D2, Y_test_D2, cv=kfold, scoring='f1')

print("Results from unprocessed testing data")
print("Precision: "),print(result_precision_testing_2.mean())
print("Recall: "),print(result_recall_testing_2.mean())
print("F-Score: "),print(result_F_score_testing_2.mean())

# *****************************************Un-Processed data END ******************************************************
