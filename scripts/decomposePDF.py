import PyPDF2
import nltk
import re
from nltk.tokenize import sent_tokenize

# Download NLTK tokenizer model
nltk.download('punkt')

def tokenize(text):
    print(text)
    return sent_tokenize(text)

def clean_text(text):
    """
    Perform basic text cleaning:
    - Remove line breaks
    - Handle hyphens splitting words across lines
    """
    # Remove line breaks
    text = text.replace('\n', ' ')
    # Remove hyphens at line breaks (e.g., "hyphen-\nated" -> "hyphenated")
    text = re.sub(r'-\s+', '', text)
    return text


def extract_sentences_from_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        
        # Extract text from each page
        for page in reader.pages:
            text += page.extract_text()
    
    # Clean the text
    cleaned_text = clean_text(text)
    
    # Split the text into sentences
    sentences = tokenize(cleaned_text)
    return sentences



def write_sentences_to_file(outputlocation, sentences):

    f = open(outputlocation, "w")
    f.write("data=[\n")
    for sentence in sentences:
        f.write('"%s",\n' % sentence)
    f.write("]\n")
