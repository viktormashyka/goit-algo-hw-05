# Порівняйте ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта 
# та Рабіна-Карпа на основі двох текстових файлів (стаття 1, стаття 2). Використовуючи timeit, 
# треба виміряти час виконання кожного алгоритму для двох видів підрядків: одного, 
# що дійсно існує в тексті, та іншого — вигаданого (вибір підрядків за вашим бажанням). 
# На основі отриманих даних визначте найшвидший алгоритм для кожного тексту окремо та в цілому.

# Програмно реалізовано алгоритми пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа.
# На основі виконання кожного з трьох алгоритмів визначено найшвидший алгоритм для кожного з двох текстів.
# Зроблено висновки щодо швидкостей алгоритмів для кожного тексту окремо та в цілому. 
# Висновки оформлено у вигляді документа формату markdown.

import timeit
import requests

# Реалізація алгоритмів

def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0: return 0
    skip = {pattern[i]: m - i - 1 for i in range(m - 1)}
    i = m - 1
    while i < n:
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i, j = i - 1, j - 1
        i += m - min(j, 1 + skip.get(text[i], m))
    return -1

def kmp_search(text, pattern):
    def compute_prefix(pattern):
        prefix = [0] * len(pattern)
        k = 0
        for i in range(1, len(pattern)):
            while k > 0 and pattern[k] != pattern[i]:
                k = prefix[k - 1]
            if pattern[k] == pattern[i]:
                k += 1
            prefix[i] = k
        return prefix
    
    prefix = compute_prefix(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefix[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return i - j + 1
    return -1

def rabin_karp(text, pattern):
    d, q = 256, 101  # d - алфавіт, q - просте число
    m, n = len(pattern), len(text)
    p, t, h = 0, 0, 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

# Вимірювання часу виконання
url_1 = 'https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh/view'
url_2 = 'https://drive.google.com/file/d/18BfXyQcmuinEI_8KDSnQm4bLx6yIFS_w/view'
response_1 = requests.get(url_1)
response_2 = requests.get(url_2)
text1 = response_1.text
text2 = response_2.text
pattern_existing = "Література"  # Існуючий підрядок
pattern_non_existing = "nonexisting"  # Вигаданий підрядок

algorithms = {
    'Boyer-Moore': boyer_moore,
    'KMP': kmp_search,
    'Rabin-Karp': rabin_karp
}

for algo_name, algo_func in algorithms.items():
    for text, text_name in [(text1, "Article 1"), (text2, "Article 2")]:
        print(f"{algo_name} - {text_name} - існуючий підрядок:")
        print(timeit.timeit(lambda: algo_func(text, pattern_existing), number=1000))
        
        print(f"{algo_name} - {text_name} - вигаданий підрядок:")
        print(timeit.timeit(lambda: algo_func(text, pattern_non_existing), number=1000))
