import math

from django.views import View, generic
from .models import CipherModel


# шифры
# маршрутная транспозиция
def cipher_transposition(text, key):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    s = len(text)
    n = len(key)
    m = math.ceil(s / n)
    if s < n * m:
        stroka = alphabet[:n * m - s]
        text = text + stroka
    list_key = list(key)
    sort_key = sorted(list_key)
    count = []

    for i in list_key:
        count.append(sort_key.index(i))
    print(count)
    table = [[' '] * n for _ in range(m)]
    k = 0
    text = list(text)
    for i in range(m):
        for j in range(n):
            table[i][j] = text[k]
            k += 1
            if k == len(text):
                break
    print(table)
    answer = ''
    for j in sorted(count):
        for i in table:
            answer += i[j]
    return answer


# дешифрование
def decipher_transposition(text, key):
    s = len(text)
    n = len(key)
    m = math.ceil(s / n)
    list_key = list(key)
    sort_key = sorted(list_key)
    count = []
    for i in list_key:
        count.append(sort_key.index(i))
    text = list(text)
    table_text = [[' '] * m for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(m):
            table_text[i][j] = text[k]
            k += 1
            if k == len(text):
                break
    table_answer = [[' '] * n for _ in range(m)]
    answer = ''
    i = 0
    for c in sorted(count):
        for j in range(m):
            table_answer[j][c] = table_text[i][j]
        i += 1
    for i in table_answer:
        answer += ''.join(i)
    return answer


# шифр виженера
def cipher_vigenere(text, key):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
    count = 0
    while True:
        if len(text) == len(key):
            break
        key = key + key[count]
        count += 1
        if count == len(key):
            count = 0
    new_text = ''
    for i in range(len(text)):
        count = 0
        for j in alphabet:
            if key[i] == j:
                break
            count += 1
        count_2 = 0
        for j in alphabet:
            if text[i] == j:
                break
            count_2 += 1
        num = count_2 + count
        print(num)
        if num >= len(alphabet):
            num = num - len(alphabet)
        new_text = new_text + alphabet[num]
    return new_text


def decipher_vigenere(text, key):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
    count = 0
    while True:
        if len(text) == len(key):
            break
        key = key + key[count]
        count += 1
        if count == len(key):
            count = 0
    new_text = ''

    for i in range(len(text)):
        count = 0
        for j in alphabet:
            if key[i] == j:
                break
            count += 1

        count_2 = 0
        for j in alphabet:
            if text[i] == j:
                break
            count_2 += 1
        num = (count - count_2) * (-1)
        print(num)
        if num >= len(alphabet):
            num = num - len(alphabet)
        new_text = new_text + alphabet[num]
    return new_text


# шифр цезаря
def cipher_caesar(text, key):
    alphabet = 'яабвгдежзийклмнопрстуфхцчшщьыэю'
    count = 0
    while True:
        if len(text) == len(key):
            break
        key = key + key[count]
        count += 1
        if count == 5:
            count = 0
    new_text = ''
    for i in range(len(text)):
        count = 0
        for j in alphabet:
            if key[i] == j:
                break
            count += 1

        count_2 = 0
        for j in alphabet:
            if text[i] == j:
                break
            count_2 += 1
        num = count_2 + count
        print(num)
        if num >= len(alphabet):
            num = num - len(alphabet)
        new_text = new_text + alphabet[num]
    return new_text


def decipher_caesar(text, key):
    alphabet = 'яабвгдежзийклмнопрстуфхцчшщьыэю'
    count = 0
    while True:
        if len(text) == len(key):
            break
        key = key + key[count]
        count += 1
        if count == 5:
            count = 0
    new_text = ''

    for i in range(len(text)):
        count = 0
        for j in alphabet:
            if key[i] == j:
                break
            count += 1

        count_2 = 0
        for j in alphabet:
            if text[i] == j:
                break
            count_2 += 1
        num = (count - count_2) * (-1)
        print(num)
        if num >= len(alphabet):
            num = num - len(alphabet)
        new_text = new_text + alphabet[num]
    return new_text


# одноразовый блокнот
def note(text, key):
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщьыъэюя')
    count = 0
    while True:
        if len(text) == len(key):
            break
        key = key + key[count]
        count += 1
        if count == len(key):
            count = 0
    text = list(text)
    key = list(key)
    index_text = []
    for i in text:
        for j in alphabet:
            if i == j:
                index_text.append(alphabet.index(j))
    index_key = []
    for i in key:
        for j in alphabet:
            if i == j:
                index_key.append(alphabet.index(j))
    print(index_text, index_key)
    answer = ''
    j = 0
    while j != len(index_text):
        for i in index_text:
            index = (i + index_key[j]) % len(alphabet)
            answer += ''.join(alphabet[index])
            j += 1
    return answer


def denote(text, key):
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщьыъэюя')
    count = 0
    while True:
        if len(text) == len(key):
            break
        key = key + key[count]
        count += 1
        if count == len(key):
            count = 0
    text = list(text)
    key = list(key)
    index_text = []
    for i in text:
        for j in alphabet:
            if i == j:
                index_text.append(alphabet.index(j))
    index_key = []
    for i in key:
        for j in alphabet:
            if i == j:
                index_key.append(alphabet.index(j))
    print(index_text, index_key)
    answer = ''
    j = 0
    while j != len(index_text):
        for i in index_text:
            index = (i - index_key[j] + len(alphabet)) % len(alphabet)
            answer += ''.join(alphabet[index])
            j += 1
    return answer


def text_edit(text):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.-_'
    for i in text:
        state = False
        for j in range(len(alphabet)):
            if alphabet[j] == i:
                state = True
        if state == False:
            return state
    return text

#ПОЕЙФЕР
alphabet = list('абвгдеёжзийклмнопрстуфхцчшщьыъэюя.-_')
def generateKeyMatrix(key):
    matrix_6x6 = [[0 for i in range(6)] for j in range(6)]
    simpleKeyArr = []
    for c in key:
        if c not in simpleKeyArr:
                simpleKeyArr.append(c)
    for i in alphabet:
        if i not in simpleKeyArr:
                simpleKeyArr.append(i)
    index = 0
    for i in range(6):
        for j in range(6):
            matrix_6x6[i][j] = simpleKeyArr[index]
            index += 1
    return matrix_6x6


def indexLocator(char, cipherKeyMatrix):
    indexOfChar = []
    for i, j in enumerate(cipherKeyMatrix):
        for k, l in enumerate(j):
            if char == l:
                indexOfChar.append(i)
                indexOfChar.append(k)
                return indexOfChar


def encryption(plainText, keyMatrix):
    cipherText = []
    i = 0
    while i < len(plainText):
        n1 = indexLocator(plainText[i], keyMatrix)
        n2 = indexLocator(plainText[i + 1], keyMatrix)
        if n1[1] == n2[1]:
            i1 = (n1[0] + 1) % 6
            j1 = n1[1]

            i2 = (n2[0] + 1) % 6
            j2 = n2[1]
            cipherText.append(keyMatrix[i1][j1])
            cipherText.append(keyMatrix[i2][j2])
        elif n1[0] == n2[0]:
            i1 = n1[0]
            j1 = (n1[1] + 1) % 6
            i2 = n2[0]
            j2 = (n2[1] + 1) % 6
            cipherText.append(keyMatrix[i1][j1])
            cipherText.append(keyMatrix[i2][j2])
        else:
            i1 = n1[0]
            j1 = n1[1]
            i2 = n2[0]
            j2 = n2[1]
            cipherText.append(keyMatrix[i1][j2])
            cipherText.append(keyMatrix[i2][j1])
        i += 2
    return cipherText


def convertPlainTextToDiagraphs(plainText):
    for s in range(0, len(plainText) + 1, 2):
        if s < len(plainText) - 1:
            if plainText[s] == plainText[s + 1]:
                plainText = plainText[:s + 1] + '.' + plainText[s + 1:]
    if len(plainText) % 2 != 0:
        plainText = plainText[:] + '.'
    return plainText

#дешифрование
from itertools import chain, islice

def playfair_decode(ct, keytable):
    rows = len(keytable)
    cols = len(keytable[0])
    table = list(chain(*keytable))
    pt = []
    for pair in zip(islice(ct, 0, None, 2), islice(ct, 1, None, 2)):
        pt.append(playfair_decode_pair(pair, table, rows, cols))
    return "".join(chain(*pt))


def playfair_decode_pair(pair, table, rows, cols):
    x1, y1 = find_in_table(pair[0], table, rows, cols)
    x2, y2 = find_in_table(pair[1], table, rows, cols)
    x1, y1, x2, y2 = playfair_decode_transform(x1, y1, x2, y2, rows, cols)
    return table[y1 * cols + x1], table[y2 * cols + x2]


def find_in_table(c, table, rows, cols):
    idx = table.index(c)
    return idx % cols, idx // cols


def playfair_decode_transform(x1, y1, x2, y2, rows, cols):
    if x1 == x2:
        y1 = (y1 - 1) % rows
        y2 = (y2 - 1) % rows
    elif y1 == y2:
        x1 = (x1 - 1) % cols
        x2 = (x2 - 1) % cols
    else:
        x1, x2 = x2, x1
    return x1, y1, x2, y2




class FormView(generic.ListView):
    model = CipherModel
    template_name = 'form.html'


class CipherView(generic.ListView):
    model = CipherModel
    template_name = 'cipher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key1 = self.request.GET.get('key')
        text1 = self.request.GET.get('text')
        key = key1.lower()
        text = text1.lower()
        if text_edit(key) == key and text_edit(text) == text:
            cipher = self.request.GET.get("cipher")
            answer = ''
            if cipher == "transposition":
                cipher = 'Маршрутная транспозия'
                if self.request.GET.get("encrypt") == "Зашифровать":
                    answer = cipher_transposition(text, key)
                    print(answer)
                if self.request.GET.get("decipher") == "Расшифровать":
                    answer = decipher_transposition(text, key)
            if cipher == "caesar":
                cipher = 'Шифр Цезаря'
                if self.request.GET.get("encrypt") == "Зашифровать":
                    answer = cipher_caesar(text, key)
                if self.request.GET.get("decipher") == "Расшифровать":
                    answer = decipher_caesar(text, key)
            if cipher == "vigenere":
                cipher = 'Шифр Виженера'
                if self.request.GET.get("encrypt") == "Зашифровать":
                    answer = cipher_vigenere(text, key)
                if self.request.GET.get("decipher") == "Расшифровать":
                    answer = decipher_vigenere(text, key)
            if cipher == "note":
                cipher = 'Одноразовый блокнот'
                if self.request.GET.get("encrypt") == "Зашифровать":
                    answer = note(text, key)
                if self.request.GET.get("decipher") == "Расшифровать":
                    answer = denote(text, key)
            if cipher == "playfair":
                cipher = 'Шифр Плейфера'
                keyMatrix = generateKeyMatrix(key)
                print(keyMatrix)
                if self.request.GET.get("encrypt") == "Зашифровать":
                    convertedPlainText = convertPlainTextToDiagraphs(text)
                    print(convertedPlainText)
                    answer = "".join(encryption(convertedPlainText, keyMatrix))
                if self.request.GET.get("decipher") == "Расшифровать":
                    answer = playfair_decode(text, keyMatrix)
            context['answer'] = answer
            context['text'] = text1
            context['key'] = key1
            context['cipher'] = cipher
        else:
            context['error'] = 'К сожалению вы ввели некорректный текст'
        return context
