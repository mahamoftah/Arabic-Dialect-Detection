import re


class Transformer:

    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.apply(self.processing)
        return X

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X)

    def processing(self, text):
        pattern = re.compile(r'[À-ÿ]')
        text = pattern.sub('', text)

        pattern = re.compile(r'https?://\S+|www\.\S+')
        text = pattern.sub(' ', text)

        pattern = re.compile(r'\b[a-zA-Z0-9]+\b|[@#:()%$؟&*\\u"،\\.!_\\n!?؛/-]')
        text = pattern.sub(' ', text)

        pattern = re.compile(r'\b[a-zA-Z0-9]+\b')
        text = pattern.sub(' ', text)

        pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"
            "\U0001F300-\U0001F5FF"
            "\U0001F680-\U0001F6FF"
            "\U0001F700-\U0001F77F"
            "\U0001F780-\U0001F7FF"
            "\U0001F800-\U0001F8FF"
            "\U0001F900-\U0001F9FF"
            "\U0001FA00-\U0001FA6F"
            "\U0001FA70-\U0001FAFF"
            "\U00002702-\U000027B0"
            "\U000024C2-\U0001F251"
            "]+", flags=re.UNICODE)

        text = pattern.sub(' ', text)
        text = re.sub(r'\s+', ' ', text).strip()

        return pattern.sub('', text)
