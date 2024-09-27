def encrypt(text: str, lang: str):
    result = ""
    text_to_encrypt = text.upper()
    if lang == "ru":
        dictionary = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    elif lang == "en":
        dictionary = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    n = len(dictionary)

    for i in range(len(text_to_encrypt)):
        if text_to_encrypt[i] in dictionary:
            index = (dictionary.index(text_to_encrypt[i]) + 3) % n
            result += dictionary[index]
        else:
            result += text_to_encrypt[i]

    return result