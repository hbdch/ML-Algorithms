import CustomExceptions

class DecisionTreeClassifier():
    
    def __init__(self, criterion='gini'):
        if criterion not in ('gini', 'entropy'):
            raise CustomExceptions.CriterionError('Invalid criterion received, select either: gini, entropy')
        self.criterion = criterion
    
    def get_criterion(self):
        return self.criterion
    
    def fit(self, features_train, labels_train):
        pass
    
    def predict(self, features_test):
        pass
    
    def score(self, features_test, labels_test):
        pass
