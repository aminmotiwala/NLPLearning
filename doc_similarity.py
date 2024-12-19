import spacy

nlp = spacy.load("en_core_web_md")

doc1 = nlp("I like salty fries and hamburgers.")
doc2 = nlp("Fast food tastes very good.")
doc3 = nlp("Karachi is in Pakistan.")

print(doc1, ' - ', doc2, ' - ', doc1.similarity(doc2))
print(doc1, ' - ', doc3, ' - ', doc1.similarity(doc3))

doc4 = nlp("I like oranges.")
doc5 = nlp("I like apples.")
print(doc4, ' - ', doc5, ' - ', doc4.similarity(doc5))

doc6 = nlp("I like burgers.")
print(doc4, ' - ', doc6, ' - ', doc4.similarity(doc6))