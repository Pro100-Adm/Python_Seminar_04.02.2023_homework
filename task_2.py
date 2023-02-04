def get_words(user_str):
    words = user_str.split(" ")
    for i in range(len(words)):
        print(f"{str(i + 1)}. {words[i][:10]}")


get_words(input("Введите слова через пробел: "))
