import glob
import os
import pandas as pd

import utils
from  constant import f, TRAIN_PATH, T15_EXCEL_PATH, EVALUATION_CSV, EVALUATION_INPUT_PATH

def train_data_preprocess():
    """データセット (T15_EXCEL_PATH file) からモデル学習用に TRAIN_PATH file を作成"""
    with open(TRAIN_PATH, "w") as train_file:
        df = pd.read_excel(T15_EXCEL_PATH)
        sentences = df["#英語(原文)"]
        for sentence in sentences:
            sentence = sentence.lower().split()
            processed_sentence = []
            exist_ng_word = False
            for word in sentence:
                try:
                    word2number = "".join(f[w] for w in word)
                    processed_sentence.append(word2number + "/" + word)
                except:
                    # 記号変換に対応していないwordがある可能性. ex) [, ], ^
                    exist_ng_word = True
            if not exist_ng_word:
                train_file.write(" ".join(processed_sentence) + "\n")


def make_encoded_sentences():
    """評価に使うencodedされた150文のtxtファイルの作成"""
    df = pd.read_csv(EVALUATION_CSV)
    encoded_sentences = df["encoded sentence"]
    with open(EVALUATION_INPUT_PATH, "w") as f:
        for sentence in encoded_sentences:
            if isinstance(sentence, str):
                f.write(sentence + "\n")