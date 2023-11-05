from tfidf import TfidfVectorizer


def demo():

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = TfidfVectorizer()
    tf_idf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tf_idf_matrix)


if __name__ == '__main__':
    demo()
