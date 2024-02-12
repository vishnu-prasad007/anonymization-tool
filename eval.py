import re
import math

def check_for_entity_match(anonymized_text, original_entities):
    """
    Count the number of entities from original text found in anonymized text.

    Parameters:
    anonymized_text (str): The anonymized text to search for entities.
    original_entities (list): List of entity objects representing entities in the original text.
    Returns:
    int: The count of entities found in the anonymized text.
    """
    matches = 0
    # Iterate over each entity in original_entities
    for pid in original_entities:
        # Compile a regex pattern for the entity value
        pattern = re.compile(pid.value)
        # Find all matches of the entity value in the anonymized text
        entities_matches = pattern.findall(anonymized_text)
        # Increment matches if at least one match is found
        if len(entities_matches) >= 1:
            matches += 1
    return matches

def compute_recall(true_positive_count, false_negative_count):
    """
    Recall is computed from the true positive and false negative counts. 
    We assume successful anonymization only if all mentions of an entity are completely masked. If not, it's considered a false negative.

    Parameters:
    true_positive_count (int): Count of true positive instances.
    false_negative_count (int): Count of false negative instances.
    Returns:
    float: The computed recall value.
    """
    return (true_positive_count / (true_positive_count + false_negative_count))

def evaluate(original_entities, anonymized_text):
    """
    Evaluate the effectiveness of anonymization by comparing original and anonymized data.

    Parameters:
        original_entities (list): A list of entity objects representing entities in the original text.
        anonymized_text (str): The anonymized text to be evaluated.
        anonymized_entities (list): A list of entity objects representing entities in the anonymized text.

    Returns:
        float: The recall value.
    """
    # Count the number of matches between anonymized entities and original entities
    no_of_matches = check_for_entity_match(anonymized_text, original_entities)
    
    # Compute recall based on the number of matches
    recall = compute_recall(len(original_entities), no_of_matches)

    # Return recall
    return recall