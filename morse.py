"""Morse Code Translator"""

import doctest
import pytest

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответсвие с таблицей азбуки Морзе.

    >>> encode('JAMES BOND')
    '.--- .- -- . ...   -... --- -. -..'
    >>> encode('OLD-FASHIONED WAY.')
    '--- .-.. -.. -....- ..-. .- ... .... .. --- -. . -..   .-- .- -.-- .-.-.-'
    >>> encode('SOS')
    '... --- ...'
    >>> encode('WELL, I LIKE TO DO SOME THINGS THE OLD-FASHIONED WAY.')
    Traceback (most recent call last):
        ...
    ValueError: Unknown character
    >>> encode('p')
    Traceback (most recent call last):
        ...
    ValueError: Unknown character
    """

    for i in message:
        if i not in LETTER_TO_MORSE.keys():
            raise ValueError('Unknown character')

    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)


def decode(morse_message: str) -> str:
    """
    Декодирует строку из азбуки Морзе в английский
    """

    for i in morse_message.split():
        if i not in MORSE_TO_LETTER.keys():
            raise ValueError('Unknown morse letter')

    decoded_letters = [
        MORSE_TO_LETTER[letter] for letter in morse_message.split()
    ]

    return ''.join(decoded_letters)


@pytest.mark.parametrize(
    'morse_letter, decoded_answer',
    [
        ('... --- ...', 'SOS'),
        ('.- .-- . ... --- -- -....- ---', 'AWESOM-O'),
        ('... .- ..- .-.. -....- --. --- -. .', 'SAUL-GONE'),
    ],
)
def test_decode(morse_letter, decoded_answer):
    assert decode(morse_letter) == decoded_answer


if __name__ == '__main__':
    doctest.testmod(optionflags=doctest.DONT_ACCEPT_BLANKLINE)
    morse_msg = '.--. -.-- - .... --- -.'
    decoded_msg = decode(morse_msg)
    print(decoded_msg)
    assert morse_msg == encode(decoded_msg)
