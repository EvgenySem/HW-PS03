import requests
from bs4 import BeautifulSoup
from googletrans import Translator

url = "https://randomword.com/"

def get_english_word():
    global url

    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        english_word = soup.find("div", id="random_word").text.strip()
        english_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_word": english_word,
            "english_definition": english_definition
        }

    except:
        print("Произошла ошибка")
        return None


def translate_to_rus():
    english_dict = get_english_word()
    translator = Translator()

    return {
        "russian_word": translator.translate(english_dict.get("english_word"), dest="ru").text,
        "russian_definition": translator.translate(english_dict.get("english_definition"), dest="ru").text
    }


def game():
    print("Добро пожаловать в игру!")

    while True:
        word_dict = translate_to_rus()

        word = word_dict.get("russian_word")
        definition = word_dict.get("russian_definition")

        print(f"Значение слова: {definition}")
        user_input = input("Что это за слово? ")
        if user_input == word:
            print("Верно!")
        else:
            print(f"Это слово -- {word}")

        if input("Сыграем еще? (да/нет) ") != "да":
            print("Спасибо за игру!")
            break


game()