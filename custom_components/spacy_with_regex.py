import spacy
from spacy.tokens import Span
import re
from spacy import Language

text = "Paul Newman was an American actor, but Paul Hollywood is a British TV Host. The name Paul is quite common. Paul Batsman."



#FLAG GPE TO LOC
@Language.component("paul_ner")
def paul_ner(doc):
    original_ents = list(doc.ents)
    multi_word_token_entities = []
    pattern = r"Paul [A-Z]\w+"
    for match in re.finditer(pattern, doc.text):
        start, end = match.span()  # these are character indexes but nlp document has tokens from document
        span = doc.char_span(start, end)
        if span is not None:
            # this helps to perform regex on normal text
            # and get matching tokens so that we can get spacy token
            # which can be used to further to nlp magic
            # start and end will be of token from above sentence rather than
            # character indexes
            multi_word_token_entities.append((span.start, span.end, span.text))

    # now lets inject back these tokens to orginal doc
    for ent in multi_word_token_entities:
        start, end, name = ent
        per_ent = Span(doc, start, end, label="PERSON")
        original_ents.append(per_ent)

    doc.ents = original_ents
    return doc

nlp = spacy.blank("en")
nlp.add_pipe("paul_ner")
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)
