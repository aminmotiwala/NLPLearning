import spacy
import json
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")

with open ("../data/alice.json", "r") as f:
    doc = json.load(f)

text = doc[0][2][0]

#it has some misplaced ` lets clean this text. lets replace ` with '

text = text.replace("`","'")

#pattern to grab person saying or thinking something
# capture ' marks
# ORTH	The exact verbatim text of a token.
# OP + MATCH ONE OR MORE
# OP * MATCH ZERO OR ONE
# REFERENCE: https://spacy.io/api/matcher

matcher = Matcher(nlp.vocab)
pattern = [
    {"ORTH": "'"},
    {"IS_ALPHA": True, "OP": "+"}, #THIS PLUS GRABS EVERYTHING AFTER ALPHA
    {"IS_PUNCT": True, "OP": "*"},
    {"ORTH": "'"}
]
matcher.add("SAYING_THINKING", [pattern], greedy="LONGEST")
document = nlp(text)
matches = matcher(document)

print("==========SAYING AND THOUGHTS==========")
for m in matches:
    print(document[m[1]: m[2]])

# ABOVE GIVE SAYING AND THOUGHTS BUT NOT WHO SAID
speak_lemmas = ["think", "say"]

matcher = Matcher(nlp.vocab)
pattern = [
    {"ORTH": "'"},
    {"IS_ALPHA": True, "OP": "+"}, #THIS PLUS GRABS EVERYTHING AFTER ALPHA
    {"IS_PUNCT": True, "OP": "*"},
    {"ORTH": "'"},
    {"POS": "VERB", "LEMMA": {"IN": speak_lemmas}},
    {"POS":"PROPN", "OP": "+"},
    {"ORTH": "'"},
    {"IS_ALPHA": True, "OP": "+"},  # THIS PLUS GRABS EVERYTHING AFTER ALPHA
    {"IS_PUNCT": True, "OP": "*"},
    {"ORTH": "'"},
]
matcher.add("SAYING_THINKING", [pattern], greedy="LONGEST")
document = nlp(text)
matches = matcher(document)

print("==========SAYING AND THOUGHTS WITH PERSON==========")
for m in matches:
    print(document[m[1]: m[2]])



