class FakeNewsModel:
    def __init__(self):
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.linear_model import PassiveAggressiveClassifier

        self.model = PassiveAggressiveClassifier()
        self.tf = TfidfVectorizer()

        self.dict = {'FAKE':0,'REAL':1}
        self.list = ["FAKE","REAL"]

    def train(self,data):
        X = data['text']
        y = data['label']

        X = self.tf.fit_transform(X)
        y = y.map(self.dict)

        self.model.fit(X,y)
        return "MODEL TRAINED SUCCESSFULLY!"

    def predict(self,test_data):
        import pandas as pd
        data = pd.read_csv('news_data.csv')
        self.train(data)

        test_data = self.tf.transform(test_data)
        test_y = self.model.predict(test_data)
        return self.list[test_y[0]]
