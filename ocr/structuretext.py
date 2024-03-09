
import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Tokenize text
text = "I love using spaCy for natural language processing."
doc = nlp(text)

# Access tokens
for token in doc:
    print(token.text)

# NER
for ent in doc.ents:
    print(ent.text, ent.label_)

# Dependency parsing
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_)
