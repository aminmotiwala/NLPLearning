#matcher unlike does not put label in entities rather than it uses vocab

import spacy
from spacy.matcher import Matcher

#Build upon the spaCy Small Model
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

#task find email address from a bunch of text
pattern1 = [{ "LIKE_EMAIL": True}]
pattern2 = [{"LIKE_NUM": True}]
matcher.add("EMAIL_ADDRESSES", [pattern1])
matcher.add("NUMERIC", [pattern2])

#Sample text
text = "amin's email is aminmotiwala92@gmail.com. Umer's is umer@gmail.com. These 2 are friends"
doc = nlp(text)

matches = matcher(doc)
print(matches)
