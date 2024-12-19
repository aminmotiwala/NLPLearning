import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

text = "amin likes playing MLBB."
# text = "The United States of America (U.S.A. or USA), commonly known as the United States (U.S. or US) or America, is a country primarily located in North America."
doc = nlp(text)
print(doc)

for token in doc:
    print(token.text, token.pos_, token.dep_)

print("==========Printing Sentence Structure==========")
output_path = "dependency_visualization.html"
with open(output_path, "w", encoding="utf-8") as f:
    html = displacy.render(doc, style="dep")
    f.write(html)