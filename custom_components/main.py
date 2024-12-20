import spacy
from spacy import Language

nlp = spacy.load("en_core_web_sm")

doc = nlp("Pakistan is a country. Amin is a software engineer.")
for ents in doc.ents:
    print(ents.text, ents.label_)

#FLAG GPE TO LOC
@Language.component("remove_gpe")
def remove_gpe(doc):
    original = list(doc.ents)
    for ent in doc.ents:
        if ent.label_ == "GPE":
            original.remove(ent)
    doc.ents = original
    return doc

nlp.add_pipe("remove_gpe")
print("========== after rmoving gpe ==========")
doc = nlp("Pakistan is a country. Amin is a software engineer.")
for ents in doc.ents:
    print(ents.text, ents.label_)