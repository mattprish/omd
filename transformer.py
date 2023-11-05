from tf import tf_transform
from idf import idf_transform


class TfidfTransformer():
    """
    АВТОБОТЫ, ТРАНСФОРМИРУЕМСЯ!
    """

    def __init__(self) -> None:
        # Создаём объект класса
        self.tf_idf_matrix = []

    def fit_transform(self, count_matrix: list) -> list:

        tf_matrix = tf_transform(count_matrix)
        idf_matrix = idf_transform(count_matrix)

        for text in tf_matrix:
            lst = []
            for i in range(len(tf_matrix[0])):
                lst.append(round(text[i] * idf_matrix[i], 3))
            self.tf_idf_matrix.append(lst)

        return self.tf_idf_matrix
