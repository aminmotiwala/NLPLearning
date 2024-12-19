import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_md")

with open ("data/wiki_us.txt", "r") as f:
    text = f.read()

# creating nlp object
doc = nlp(text)

for ents in doc.ents:
    print (ents.text, ents.label_)

print("==========rendering entities==========")
output_path = "entities.html"
with open(output_path, "w", encoding="utf-8") as f:
    html = displacy.render(doc, style="ent")
    f.write(html)