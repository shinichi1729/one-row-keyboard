
# f[x]: xに対応する数字
f = {'!': '1', 'q': '1', 'a': '1', 'z': '1', 'w': '2', 's': '2', 'x': '2', 'e': '3', 'd': '3', 'c': '3', 'r': '4', 'f': '4', 'v': '4', 't': '5', 'g': '5', 'b': '5', 'y': '6', 'h': '6', 'n': '6', "'": '7', 'u': '7', 'j': '7', 'm': '7', 'i': '8', 'k': '8', ',': '8', 'o': '9', 'l': '9', '.': '9', 'p': '0', ';': '0', '/': '0', '?': '0'}


TRAIN_PATH     = "./data/train.txt"          # モデルに与える学習txtファイル
T15_EXCEL_PATH = "./data/T15-2020.1.7.xlsx"  # 学習データセットのxlsxファイル

EVALUATION_CSV = "./data/hear_year_near.csv" # 評価用データセットcsvファイル
EVALUATION_INPUT_PATH  = "./data/evaluate_input.txt"  # 評価用データセットをモデルに推論できる形にしたtxtファイル
EVALUATION_OUTPUT_PATH = "./data/evaluate_output.txt" # モデルが推論した結果のtxtファイル

