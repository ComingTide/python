translation_dictionary = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
                          "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}


def num_translate(word):
    if word.istitle():
        return str(translation_dictionary.get(word.lower())).title()
    return translation_dictionary.get(word)


print(num_translate(input("Какую цифру нужно перевести: ")))
