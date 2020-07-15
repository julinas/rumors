from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

nlp = English()
tokenizer = Tokenizer(nlp.vocab)

def convertText(text):
    tokens = tokenizer(text)
    return tokens