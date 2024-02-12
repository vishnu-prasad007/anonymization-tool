import spacy
import random
from patterns import patterns
import pid
import re

nlp = spacy.load("en_core_web_md")
 
def extract_entities(text):
    """
    Extracts entities from the given text using both regex patterns and spaCy's named entity recognition.

    Parameters:
    text (str): The input text from which entities will be extracted.
    Returns:
    list: A list of entity objects representing the extracted entities.
    """
    entities = []  # Initialize an empty list to store entities

    # Perform naive regex approach
    for pattern in patterns:  # Iterate over predefined patterns
        # Find all matches of the current pattern in the text
        matches = [(match.group(), match.start(), match.end(), id) for match in re.finditer(pattern['pattern'], text)]
        for m in matches:
            # Append the matched entity to the entities list, along with its label, start position, and end position
            entities.append(pid.PID(value=m[0], entity=pattern['label'], start_pos=m[1], end_pos=m[2]))

    # Use spaCy to extract named entities
    doc = nlp(text)
    # Extract entities recognized by spaCy, such as PERSON, ORG, PASSPORT
    entities = entities + [pid.PID(entity=ent.label_, value=ent.text, start_pos=ent.start_char, end_pos=ent.end_char) for ent in doc.ents if ent.label_ in ["PERSON", "ORG", "PASSPORT"]]

    return entities
