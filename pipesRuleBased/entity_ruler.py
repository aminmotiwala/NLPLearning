#THIS HELPS TO MANUALLY TELL YOUR MODEL HOW TO ANALYZE IF WE HAVE SPECIFIC RULES
#TOPONYM - ISSUE IS IN MODELS, EXAMPLE MR DEEDS CAN BE A MOVIE OR A PERSON DEPENDING ON CONTEXT
import spacy

#Build upon the spaCy Small Model
nlp = spacy.load("en_core_web_sm")

#Sample text
text = "West Chestertenfieldville was referenced in Mr. Deeds."

#mr deeds is a movie but it does not know

#Create the Doc object
doc = nlp(text)

#extract entities
for ent in doc.ents:
    print (ent.text, ent.label_)

ruler = nlp.add_pipe("entity_ruler", before="ner")
print(nlp.analyze_pipes())

patterns = [
    {"label": "GPE", "pattern": "West Chestertenfieldville"},
    {"label": "MOVIE", "pattern": "Mr. Deeds"}
]

ruler.add_patterns(patterns)

doc2 = nlp(text)
for ent in doc2.ents:
    print (ent.text, ent.label_)