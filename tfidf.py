from cnt import CountVectorizer
from transformer import TfidfTransformer


class TfidfVectorizer(CountVectorizer):

    def __init__(self) -> None:
        super().__init__()

    def fit_transform(self, corp):

        transformer = TfidfTransformer()

        count_matrix = super().fit_transform(corp)
        tf_idf_matrix = transformer.fit_transform(count_matrix)

        self.count_matrix = count_matrix
        self.tf_idf_matrix = tf_idf_matrix

        return tf_idf_matrix
