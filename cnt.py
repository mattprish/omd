class CountVectorizer:
    """
    Сейчас мы жестко отвекторизуем корпус текстов
    """

    def __init__(self) -> None:
        # Создаём объект класса
        self.bag_of_words = set()
        self.count_matrix = []

    def fit_transform(self, corpus: list) -> list:
        # Разбираем корпус на детальки

        for text in corpus:
            words = text.split(' ')
            for word in words:
                word = word.lower()
                if word not in self.bag_of_words:
                    self.bag_of_words.add(word)
        ordered_list = list(self.bag_of_words)
        self.ordered_list = ordered_list

        for text in corpus:
            words = text.split(' ')
            this_text = []
            for key_word in ordered_list:
                cnt = 0
                for word in words:
                    word = word.lower()
                    if key_word == word:
                        cnt += 1
                this_text.append(cnt)
            self.count_matrix.append(this_text)
        return self.count_matrix

    def get_feature_names(self) -> list:
        return self.ordered_list


def demo():
    corp = ['Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste']
    corp = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corp)
    print(vectorizer.get_feature_names())
    print(count_matrix)


if __name__ == '__main__':
    demo()
