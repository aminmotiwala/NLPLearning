import spacy

nlp = spacy.load("en_core_web_sm")

with open ("data/wiki_us.txt", "r") as f:
    text = f.read()

print(text)

# creating nlp object
doc = nlp(text)
print("============DOC================")
print(doc)

# printing sentence
print()
print("============sentences================")
for sents in doc.sents:
    if len(sents) == 0:
        continue
    print(sents)

#printing first sentence
sentenceList = list(doc.sents)
print("============first sentences================")
sentence1 = sentenceList[0]
print(sentence1)

print("============printing text================")
print(sentence1.text)

print("============printing third token in sentence================")
token3 = sentence1[2]
print(token3)

print("============printing entity type================")
print(token3.ent_type_)
#it gives GPE - GEO POLITICAL ENTITY

print("============printing IOB================")
print(token3.ent_iob_)
#IOB code of named entity tag.
# “B” means the token begins an entity,
# “I” means it is inside an entity,
# “O” means it is outside an entity, and
# "" means no entity tag is set.

print("============printing LEMA================")
#Base form of the token
# Base of better is good
# base of hunter is hunt
print(token3.lemma_)

print("============printing morph================")
#Morphological analysis of token
token12 = sentence1[12]
print(token12.text)
print(token12.morph)
#Aspect=Perf|Tense=Past|VerbForm=Part
#this is perfect past participle

print("============printing pos================")
#part of speech
token2 = sentence1[2]
print(token2.text)
print(token2.pos_)
#PROPN
#this tells this is a proper noun

print("============printing dep================")
#Syntactic dependency relation
token2 = sentence1[2]
print(token2.text)
print(token2.dep_)
#nsubj
#this tells this is a subject

print("============printing lang================")
#Syntactic dependency relation
token2 = sentence1[2]
print(token2.text)
print(token2.lang_)
#en
#this tells this is english
