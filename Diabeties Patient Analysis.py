# Diabetics Patients data analysis.

import pandas as pd
import seaborn as sb
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# This data files contains data of diabetes in at least 21 years old of Pima Indian heritage women.
diabetes_file=pd.read_csv("C:/Users/home/Desktop/diabetes.csv")
# print(diabetes_file.to_string())

# Printing the first five rows of the diabetes file.
print(diabetes_file.head())

# Checking the  file info: number of rows,number of columns, no of null values in the diabetes file.
print(diabetes_file.info())

# Checking the number of null values in eaxh coloumn.
print(diabetes_file.isnull().sum())
# So, we find that there are no null_values in any  columns of the data set.

#Predicting whether a woman has diabetes based on the independent factors.
# Here the dependent variable is Outcome which needs to be predicted.
y=diabetes_file["Outcome"]
x=diabetes_file.iloc[::,0:8]
# Taking train and test data from x independent variables and y dependent variable.
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2) #Applying the logistic regression model on the train data.
log_model=linear_model.LogisticRegression( max_iter=10000)
log_model.fit(x_train,y_train)

# Predicting whether a woman has diabetes using test data.
print(log_model.predict(x_test))

# Checking the accuracy of the logistic Regression Model.
print(log_model.score(x_test,y_test))  # 0.767
# This means that our model is moderately accurate.
# Checking the probabilities of the observations of the independent variables test_data.
print(log_model.predict_proba(x_test))
