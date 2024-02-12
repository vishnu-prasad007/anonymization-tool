import datetime
import random
import string

class PID:
    def __init__(self, value, entity, start_pos, end_pos, id=None):
        """
        Initialize a PID object.

        Parameters:
        value (str): The value of the PID.
        entity (str): The type of entity (e.g., PERSON, CAR_PLATE).
        start_pos (int): The starting position of the PID in the original text.
        end_pos (int): The ending position of the PID in the original text.
        id (int, optional): The unique identifier for the PID. Defaults to None.
        """
        self.value = value
        self.entity = entity
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.id = id

    def __repr__(self) -> str:
        """
        Return a string representation of the PID object.

        Returns:
        str: A string representation of the PID object.
        """
        return f"value: {self.value}, Label: {self.entity}, start: {self.start_pos}, end: {self.end_pos}, ID: {self.id}"
    
    def set_id(self, id):
        """
        Set the ID of the PID.

        Parameters:
        id (int): The ID to set for the PID.
        """
        self.id = id
    
class AnonymizePID:
    def __init__(self, pid: PID):
        """
        Initialize the AnonymizePID object with a PID.

        Parameters:
        pid (PID): The PID object to anonymize.
        """
        self.pid = pid
        
    def get_anonymized_pid(self) -> PID:
        """
        Get the anonymized PID based on the entity type.

        Returns:
        PID: The anonymized PID object.
        """
        if self.pid.entity == 'PERSON':
            return PID(value=self.generate_name(), entity=self.pid.entity, start_pos=self.pid.start_pos, end_pos=self.pid.end_pos)
        elif self.pid.entity == 'CAR_PLATE':
            return PID(value=self.generate_car_plate(), entity=self.pid.entity, start_pos=self.pid.start_pos, end_pos=self.pid.end_pos)
        elif self.pid.entity == 'SOCIAL_SECURITY_NUMBER':
            return PID(value=self.generate_social_security_number(), entity=self.pid.entity, start_pos=self.pid.start_pos, end_pos=self.pid.end_pos)
        elif self.pid.entity == 'CREDIT_CARD':
            return PID(value=self.generate_credit_card_number(), entity=self.pid.entity, start_pos=self.pid.start_pos, end_pos=self.pid.end_pos)
        elif self.pid.entity == 'ORG':
            return PID(value=self.generate_org_name(), entity=self.pid.entity, start_pos=self.pid.start_pos, end_pos=self.pid.end_pos)
        elif self.pid.entity == 'PASSPORT':
            return PID(value=self.generate_passport_number(), entity=self.pid.entity, start_pos=self.pid.start_pos, end_pos=self.pid.end_pos)
        else:
            return PID(value='******', entity=self.pid.entity, start_pos=self.pid.start_pos, end_pos=self.pid.end_pos)
        
    def generate_name(self):
        """
        Generate a random name.

        Returns:
        str: A randomly generated name.
        """
        # List of common first names
        first_names = ['John', 'Emma', 'Michael', 'Sophia', 'William', 'Olivia', 'James', 'Ava', 'Alexander', 'Isabella']
        # List of common last names
        last_names = ['Smith', 'Johnson', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Taylor']
        # Randomly select a first name and a last name
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        # Combine the first name and last name
        full_name = f"{first_name} {last_name}"
        return full_name
    
    def generate_car_plate(self):
        """
        Generate a random car plate number.

        Returns:
        str: A randomly generated car plate number.
        """
        # Generate three random letters for the prefix
        prefix = ''.join(random.choices(string.ascii_uppercase, k=3))
        # Generate four random digits for the suffix
        suffix = ''.join(random.choices(string.digits, k=4))
        # Concatenate the parts to form the car plate
        car_plate = f"{prefix}-{suffix}"
        return car_plate
    
    def generate_social_security_number(self):
        """
        Generate a random social security number.

        Returns:
        str: A randomly generated social security number  (ssn)
        """
        # Generate a random 9-digit number
        ssn = ''.join(random.choices('0123456789', k=9))
        formatted_ssn = f"{ssn[:3]}-{ssn[3:5]}-{ssn[5:]}"
        return formatted_ssn
    
    def generate_credit_card_number(self):
        """
        Generate a random credit card number

        Returns:
        str: A randomly generated credit card number.
        """
        # Generate a random 16-digit number (credit card numbers typically have 16 digits)
        credit_card_number = ''.join(random.choices('0123456789', k=16))
        return credit_card_number
    
    def generate_org_name(self):
        """
        Generate a random organization name.

        Returns:
        str: A randomly generated organization name.
        """
        # List of common prefixes and suffixes for organization names
        prefixes = ['Global', 'National', 'International', 'United', 'World', 'American', 'Global', 'International', 'Universal']
        suffixes = ['Corp', 'Inc', 'Ltd', 'Group', 'Organization', 'Associates', 'Enterprises', 'Solutions', 'Industries', 'GmbH']
        # Generate a random organization name by combining a random prefix and a random suffix
        org_name = random.choice(prefixes) + " " + random.choice(suffixes)
        return org_name
    
    def generate_passport_number(self):
        """
        Generate a random passport number

        Returns:
        str: A randomly generated passport number.
        """
        # Generate a random string of uppercase letters and digits for the passport number
        passport_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
        return passport_number

def anonymize(pid: PID):
    """
    Anonymize a PID.

    Parameters:
    pid (PID): The PID object to anonymize  .

    Returns:
    PID: The anonymized PID object.
    """
    anonymized_pid = AnonymizePID(pid)
    return anonymized_pid.get_anonymized_pid()

def rewrite_text(source_text: str, pids: list):
    """
    Rewrite the source text with anonymized PIDs.

    Parameters:
    sourceText (str): The original text to be rewritten.
    pids (list): A list of PID objects representing entities in the original text.

    Returns:
    str: The rewritten text with anonymized PIDs.
    """
    new_text = source_text
    offset = 0
    pids.sort(key=lambda x: x.start_pos, reverse=False)  # Sort PIDs by start position
    ids_visited = {} # We anonymize based on IDs to preserve the original semantics in the anonymized text
    for pid in pids:
        if pid.id not in ids_visited.keys():
            anonymized_pid = anonymize(pid)
            ids_visited[pid.id] = anonymized_pid
            pid = anonymized_pid
        else:
            # Use anonymized PID if ID already visited
            pid = PID(value=ids_visited[pid.id].value, entity=pid.entity, start_pos=pid.start_pos, end_pos=pid.end_pos)
        # Replace original PID value with anonymized value in the new text
        new_text = new_text[:pid.start_pos + offset] + pid.value + new_text[pid.end_pos + offset:]
        offset += len(pid.value) - (pid.end_pos - pid.start_pos)
    return new_text


def assign_id_to_entities(entities_o):
    """
    Assigns IDs to entities based on their values while preserving the original order and semantics. Ensuring entities with the same value have the same ID
    
    Parameters:
    entities_o (list): A list of entity objects to which IDs will be assigned.
    Returns:
    list: A list of entity objects with unique IDs assigned.
    """
    # Dictionary to track visited entity values and their assigned IDs
    visited_value = {}
    entities = entities_o  # Make a copy of the entities list

    # Iterate over the entities list
    for i in range(0, len(entities)):
        # Check if the current entity value (with "'s" removed) is not in the visited_value dictionary
        # We check if the entity value with "'s" removed is not in the visited_value dictionary to treat possessive forms consistently with original entity names (such as "person's name")
        if entities[i].value.replace("'s", "") not in visited_value.keys():
            # Generate a random ID for the entity
            id = random.randint(1, 1000)
            # Store the entity value (with "'s" removed) and its assigned ID in the visited_value dictionary
            visited_value[entities[i].value] = id
            # Set the ID of the current entity
            entities[i].set_id(id)
        else:
            # Retrieve the ID from the visited_value dictionary for the current entity value (with "'s" removed)
            id = visited_value[entities[i].value.replace("'s", "")]
            # Set the ID of the current entity
            entities[i].set_id(id)

    return entities
