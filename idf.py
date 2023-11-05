import math


def idf_transform(count_matrix):
    """Считает значение idf -
    важности слова для отдельного корпуса
    текстов. Больше идф - больше важность

    Examples:
    >>> idf_transform([[1, 1, 2], [0, 1, 1]])
    [[0.25, 0.25, 0.5], [0, 0.5, 0.5]]

    >>> idf_transform('some text')
    Traceback (most recent call last):
        ...
    ValueError: arg must be a list

    >>> idf_transform([['aboba'], [2]])
    Traceback (most recent call last):
        ...
    ValueError: matrix must contain ints or lists with ints


    Args:
        count_matrix (_type_): матрица с количеством
        появлений слов в предложениях

    Returns:
        idf_matrix (list): матрица с idf


    """

    if not type(count_matrix) is list:
        raise ValueError("arg must be a list")
    for el in count_matrix:
        if not (type(el) is list or type(el) is int):
            raise ValueError("matrix must contain ints or lists with ints")

    if type(count_matrix[0]) is int:
        return [1 for i in range(len(count_matrix))]

    new_list = []
    num_texts = len(count_matrix)

    for i in range(len(count_matrix[0])):
        s_in = 0
        for lst in count_matrix:
            if lst[i] > 0:
                s_in += 1
        new_list.append(s_in)

    idf_matrix = []
    for element in new_list:
        num = num_texts + 1
        denum = element + 1
        val = round(math.log(num/denum), 3) if num != denum else 0
        idf_matrix.append(val + 1)

    return idf_matrix
