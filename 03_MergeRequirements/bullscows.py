import textdistance as td
import random


def bullscows(guess: str, secret: str) -> (int, int):
    bulls = td.hamming.similarity(guess, secret)
    ### ТУТ ПРОБЛЕМА, НЕ ПОЛУЧИЛОСЬ НАЙТИ подходящие МЕТРИКИ ИЗ textdistance для определения коров
    cows = td.damerau_levenshtein.similarity(guess, secret) - bulls
    return bulls, cows


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


def ask(prompt: str, valid: list[str] = None) -> str:
    ipt = input(prompt)
    while valid is not None and ipt not in valid:
        print("Слова нет в словаре")
        ipt = input(prompt)
    return ipt


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


if __name__ == '__main__':
    import sys
    import urllib.request
    try:
        words_source = sys.argv[1]
    except IndexError:
        print("Ожидался как минимум один аргумент!", file=sys.stderr)
        exit(1)
    try:
        length = int(sys.argv[2])
    except IndexError:
        length = 0
    except ValueError:
        print("Второй аргумент должен быть целым числом!", file=sys.stderr)
        exit(1)

    if words_source.startswith("https://") or words_source.startswith("http://"):
        with urllib.request.urlopen(words_source) as response:
           html = response.read().decode("utf-8")
        words = html.split("\n")
    else:
        with open(words_source) as f:
            words = f.readlines()

    if length != 0:
        words = list(filter(lambda x: len(x) == length, words))
    
    turns = gameplay(ask, inform, words)
    print(f"Слово отгадно за {turns} попыток!")
