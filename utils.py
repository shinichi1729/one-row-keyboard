from typing import List

from constant import f


def encode(text: str) -> List[str]:
    try:
        text = text.lower()
        text = text[:-1] + " " + text[-1]
        encoded_text = []
        for word in text.split():
            encoded_word = "".join(f[w] for w in word)
            if encoded_word:
                encoded_text.append(encoded_word)
    except:
        return []
    return encoded_text



