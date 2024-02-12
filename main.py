import sys
import utils
import pid
import eval
import textparser

def main(dir_path):
    # Read input files from the 'dir_path' directory
    files = utils.read_input_dir(dir_path)

    # Read the contents of each file
    documents = utils.read_files(files)

    # Process each document
    for document in documents:
        # Extract the name and content of the document
        document_name = document[0]
        document_content = document[1]
        
        # Extract entities from the original document
        original_entities = textparser.extract_entities(document_content)
        
        # Assign unique IDs to entities
        original_entities = pid.assign_id_to_entities(original_entities)
        
        # Anonymize the document content
        anonymized_text = pid.rewrite_text(document_content, original_entities)
        
        # Write the anonymized text to a file in the 'anonymized' directory
        utils.write_to_file('anonymized', document_name, anonymized_text)
        
        # Evaluate the anonymization effectiveness
        recall = eval.evaluate(original_entities, anonymized_text)
        
        # Print the recall value for the document
        print(f"For {document_name} Recall : {recall}")


if __name__ == "__main__":
    # Check if exactly one command-line argument is provided
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <argument>")
        sys.exit(1)
    
    # Pass the command-line argument to the main function
    main(sys.argv[1])

