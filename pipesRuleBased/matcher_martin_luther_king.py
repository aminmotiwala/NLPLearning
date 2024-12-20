import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_md")

with open ("../data/wiki_mlk.txt", "r") as f:
    text = f.read()

print(text)
doc = nlp(text)

#Get all proper nouns from this documents
print("==========PROPER NOUNS===========")
matcher = Matcher(nlp.vocab)
pattern = [{"POS":"PROPN"}]
matcher.add("PROPER_NOUN", [pattern])
matches = matcher(doc)
print(len(matches))

unique = set()

for i,match in enumerate(matches):
    unique.add(doc[match[1]: match[2]].text)

for i,noun in enumerate(unique):
    print(i + 1, noun)

# this is breaking martin luther - into two separate nouns - we need to fix this
pattern = [{"POS":"PROPN", "OP": "+"}]
matcher.add("PROPER_NOUN", [pattern])
matches = matcher(doc)

uniqueAfter = set()

for i,match in enumerate(matches):
    uniqueAfter.add(doc[match[1]: match[2]].text)

for i,noun in enumerate(uniqueAfter):
    print(i + 1, noun)

# now this is giving martin then martin luther and then martin luther king
# lets get the longest nouns


print("==========GREEDY===========")

pattern = [{"POS":"PROPN", "OP": "+"}]
matcher.add("PROPER_NOUN", [pattern], greedy="LONGEST")
matches = matcher(doc)
#lets sort as ther are appearing in document
# so we know matches are like (451313080118390996, 84, 89) where 84 and 89 are placement in document
# lets sort with 84 - which is starting position. so its at first index x[1]
matches.sort(key = lambda x: x[1])

for i,match in enumerate(matches):
    print(i, doc[match[1]: match[2]].text)

# now lets get all the nouns that have a verb after them
print("==========VERB AFTER PROPER NOUN===========")
matcher = Matcher(nlp.vocab)
pattern = [{"POS":"PROPN", "OP": "+"}, {"POS":"VERB"}, {"POS":"PROPN", "OP": "+"}]
matcher.add("VERB_AFTER_NOUN", [pattern])
matches= matcher(doc)
matches.sort(key = lambda x: x[1])

for i,match in enumerate(matches):
    print(i, doc[match[1]: match[2]].text)