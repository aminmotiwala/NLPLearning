import spacy
import numpy as np

nlp = spacy.load("en_core_web_md")

with open ("data/wiki_us.txt", "r") as f:
    text = f.read()

# creating nlp object
doc = nlp(text)
sentence1 = list(doc.sents)[0]
print(sentence1)

# find similar words in our model embeddings
word = "world"
ms = nlp.vocab.vectors.most_similar(
    np.asarray([nlp.vocab.vectors[nlp.vocab.strings[word]]]), n=10)
words = [nlp.vocab.strings[w] for w in ms[0][0]]
distances = ms[2]

print(words)