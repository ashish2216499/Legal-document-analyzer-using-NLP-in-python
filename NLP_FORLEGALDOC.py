import spacy # type: ignore

def process_legal_document(text):
  """
  Analyzes a legal document using spaCy for named entity recognition (NER).

  Args:
      text (str): The legal document text to be processed.

  Returns:
      dict: A dictionary containing the identified entities and their labels.
  """

  nlp = spacy.load("en_core_web_sm")  # Load the pre-trained English model
  doc = nlp(text)  # Process the legal text with spaCy

  entities = {}
  for entity in doc.ents:
    entities[entity.text] = entity.label_  # Store entity text and label

  return entities

# Sample legal text
text = """This contract is between Acme Corp. (Seller) and John Doe (Buyer).
Seller agrees to sell a product to Buyer for a price of $1000. The delivery date is set for June 1st, 2024."""

# Process the text and print the identified entities
processed_entities = process_legal_document(text)
print(processed_entities)
