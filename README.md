# Anonymization Tool
## Introduction

This is a command-line tool designed to anonymize text data by replacing sensitive information such as names, organizations, passport numbers, car plates, social security numbers, and credit card numbers with anonymized placeholders.

## Anonymization process
### Entity Recognition: 
The tool utilizes natural language processing (NLP) techniques, specifically Named Entity Recognition (NER) from the SpaCy model, to identify and extract entities such as PERSON, ORG and PASSPORT_NUMBER from text data.

Entities like CAR_PLATE, SOCIAL_SECURITY_NUMBER, and CREDIT_CARD_NUMBERS are identified and extracted using regular expressions (Regex). These regular expressions are designed to match specific patterns corresponding to these entities within the text data.

### Anonymization
Once the entities are extracted, they are anonymized by replacing them with randomly generated data of the same entity type. For example, if a CAR_PLATE is extracted from the original text, a randomly generated CAR_PLATE number is used to anonymize the sensitive information


## Evaluation
To measure the effectiveness of the anonymization process, the tool employs recall as the evaluation metric. A recall of 1 indicates successful anonymization, while a value less than 1 suggests that some sensitive PIDs may still be present in the anonymized text


## Runtime complexity

The time complexity of the operations are described per text document as follows: $$O(p \times m + e + n \log n)$$

This represents the overall time complexity of the operations per text file or document, where:
- $p$  represents the patterns like (Regex, NER)
- $m$ represents matches, text that matched the pattern
- $e$ represents the extracted entities
- $n$ represents the size of a list, in this case list of entities.

Each term in the expression contributes to the overall time complexity of the operations performed.

## How to run the code ?.

### Installation
1. Clone the repository to your local machine:

```console
git clone git@github.com:vishnu-prasad007/anonymization-tool.git
```

2. Install the required dependencies:
```console
pip install -r requirements.txt
```

### Usage

1. Prepare your input text files and place them in the input directory.
2. Run the anonymization tool from the command line:

```console
python3 main.py './input'
```

The tool will process the input files, anonymize the text data, and save the anonymized versions in the anonymized directory.

Evaluation metric recall will be displayed in the command line for each document processed.