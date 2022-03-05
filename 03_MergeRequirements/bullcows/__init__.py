import textdistance as td
import random


def bullscows(guess: str, secret: str) -> tuple[int, int]:
    hamming_len = td.Hamming().similarity(guess, secret)
    bag_len = td.Bag().similarity(guess, secret)
    return (hamming_len, bag_len)


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = random.choice(words)
    n = len(secret)
    turns = 0
    b = 0
    while b != n:
        guess = ask("Введите слово: ", words)
        turns += 1
        b, c = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", b, c)
    return turns
