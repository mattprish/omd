def tf_transform(count_matrix):
    """Преобразует количество появлений слов
    в предложении в долю

    Examples:
    >>> tf_transform([[1, 1, 2], [0, 1, 1]])
    [[0.25, 0.25, 0.5], [0, 0.5, 0.5]]

    >>> tf_transform('some text')
    Traceback (most recent call last):
        ...
    ValueError: arg must be a list


    Args:
        count_matrix (_type_): матрица с количеством
        появлений слов в предложениях

    Returns:
        tf_matrix (list): матрица с долей
        появлений слова среди всех в предложении


    """

    if not type(count_matrix) is list:
        raise ValueError("arg must be a list")

    tf_matrix = []
    for old_list in count_matrix:
        s = sum(old_list)
        new_list = []
        for element in old_list:
            element = element / s
            new_list.append(round(element, 3) if element != 0 else 0)
        tf_matrix.append(new_list)
    return tf_matrix
