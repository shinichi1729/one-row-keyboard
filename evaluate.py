import pandas as pd
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

from constant import EVALUATION_CSV, EVALUATION_OUTPUT_PATH


LABEL = ["hear", "year", "near"]

    
def evaluate():
    """decoded_sentence.txtとhear_year_near.csvのoriginal sentenceを比べて評価を行い混同行列を作成"""
    df = pd.read_csv(EVALUATION_CSV)
    correct_labels = df["label"]
    correct_labels = [LABEL.index(label) for label in correct_labels]
    
    with open(EVALUATION_OUTPUT_PATH) as file:
        decoded_sentences = file.readlines()
        denoised_decoded_sentences = []
        for sentence in decoded_sentences:
            sentence = sentence.rstrip()
            sentence = sentence.split()
            sentence = [chunk.split("/")[1] for chunk in sentence]
            
            denoised_decoded_sentences.append(" ".join(sentence))
    
    pred_labels = []
    for sentence in denoised_decoded_sentences:
        for i, label in enumerate(LABEL):
            if label in sentence:
                pred_labels.append(i)
    return correct_labels, pred_labels
    

def make_confusion_matrix(correct_labels, pred_labels):
    cm = confusion_matrix(correct_labels, pred_labels)
    cm = pd.DataFrame(data=cm, index=LABEL, 
                            columns=LABEL)
    sns.heatmap(cm, square=True, cbar=True, annot=True, cmap='Blues')
    plt.yticks(rotation=0)
    plt.xlabel("Predict", fontsize=13, rotation=0)
    plt.ylabel("Correct", fontsize=13)
    plt.savefig('result/sklearn_confusion_matrix.png')


if __name__ == "__main__":
    correct_labels, pred_labels = evaluate()
    make_confusion_matrix(correct_labels, pred_labels)