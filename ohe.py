from typing import List, Tuple
import unittest
import pytest
from pprint import pprint


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (
            int(b) for b in bin_format.format(1 << len(seen_categories))
            )
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


def test_empty():
    with pytest.raises(TypeError):
        fit_transform()


def test_string():
    a = 'hello'
    assert a in fit_transform(a)[0]


def test_four_cities():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    assert transformed_cities is not None
    assert transformed_cities == exp_transformed_cities


def test_six_cities():

    cities = ['Moscow', 'New York', 'Moscow', 'aboba', 'bebra', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 0, 0, 1]),
        ('New York', [0, 0, 0, 1, 0]),
        ('Moscow', [0, 0, 0, 0, 1]),
        ('aboba', [0, 0, 1, 0, 0]),
        ('bebra', [0, 1, 0, 0, 0]),
        ('London', [1, 0, 0, 0, 0])
        ]
    transformed_cities = fit_transform(cities)
    assert transformed_cities == exp_transformed_cities


class TestOHE(unittest.TestCase):

    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_string(self):
        a = 'hello'
        self.assertIn(a, fit_transform(a)[0])

    def test_four_cities(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertIsNotNone(transformed_cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_six_cities(self):

        cities = ['Moscow', 'New York', 'Moscow', 'aboba', 'bebra', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 0, 0, 1]),
            ('New York', [0, 0, 0, 1, 0]),
            ('Moscow', [0, 0, 0, 0, 1]),
            ('aboba', [0, 0, 1, 0, 0]),
            ('bebra', [0, 1, 0, 0, 0]),
            ('London', [1, 0, 0, 0, 0])
            ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)


if __name__ == '__main__':

    unittest.main()
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    transformed_cities = fit_transform(cities)
    pprint(transformed_cities)
    assert transformed_cities == exp_transformed_cities
