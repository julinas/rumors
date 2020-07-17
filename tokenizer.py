from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

nlp = English()
tokenizer = Tokenizer(nlp.vocab)

def convertText(text):
    tokenList = tokenizer(text)
    if isinstance(tokenList, list):
        vectors = []
        for i in tokenList:
            vectors.append(i.vector)
        return vectors
    else:
        return tokenList.vector
    return tokenList