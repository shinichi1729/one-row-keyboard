from collections import defaultdict
import pandas as pd
from constant import TRAIN_PATH, T15_EXCEL_PATH


def count_word()
num2word = defaultdict(set)
with open(TRAIN_PATH, "r") as file:
    df = pd.read_excel(T15_EXCEL_PATH)
    sentences = df["#英語(原文)"]
    for sentence in sentences:
        sentence = sentence.split()
        for code_word in sentence:
            code, word = code_word.split("/")
            num2word[code].add(word)

words_set = set()
for key, words in num2word.items():
    for word in words:
        words_set.add(word)
    if len(words) >= 3:
        print(words)

print(len(words_set))


