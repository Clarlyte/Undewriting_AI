import spacy

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Function to tokenize text from a file and extract named entities
def extract_entities_from_file(file_path):
    # Read text from the file
    with open(file_path, 'r', encoding='latin-1') as file:
        text = file.read()

    # Tokenize text
    doc = nlp(text)

    # Initialize a dictionary to store extracted entities and their labels
    entities = {}

    # Iterate through named entities in the text
    for ent in doc.ents:
        # Extract the entity text and label
        entity_text = ent.text
        entity_label = ent.label_

        # Check if the entity label already exists in the dictionary
        if entity_label in entities:
            # If the label exists, append the entity text to the corresponding list
            entities[entity_label].append(entity_text)
        else:
            # If the label doesn't exist, create a new list with the entity text
            entities[entity_label] = [entity_text]

    # Return the dictionary of extracted entities and their labels
    return entities

# Example usage:
file_path = "C:\\Users\\biboy\\Desktop\\Underwrting Ai\\Underwriting_project\\extracted_text\\test2.txt"
entities = extract_entities_from_file(file_path)

# Print extracted entities and their labels
print("Extracted entities:")
for label, texts in entities.items():
    print(f"Label: {label}")
    for text in texts:
        print(text)
    print()
