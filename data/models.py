from sklearn.linear_model import LogisticRegression

# Define a function which trains a logistic model
def createModel(X_train, y_train):
    
    
    LogitModel = LogisticRegression(solver = 'lbfgs', 
                             max_iter = 100, 
                             random_state = 1234)
    
    LogitModel.fit(X_train, y_train)  
    
    #Display model accuracy on the training data.
    print(f'Accuracy for the training sample: {LogitModel.score(X_train, y_train):.2f}')
    return LogitModel
  
# ---------------------

