import spacy

nlp = spacy.blank("en")
print(nlp.analyze_pipes())

# we can only use those pipes that we want.
nlp.add_pipe("sentencizer")
print(nlp.analyze_pipes())

text = "hi, my name is amin. I am a software engineer."

doc= nlp(text)

for sen in doc.sents:
    print(sen)