# Sentence-Retrieval-Embeddings
Sentence-level information retrieval using embeddings

This is a simple use case where embeddings are used to validate the input of the user by providing a sentence from the paper that contains the same information.
The output is an actual quote from the document, rather than a RAG answer, briging reliability to the answer.

Input: 
   This work deals with the detection of cocoa agroforest.

Output:
   Based on the analysis of the models and the frequency of selection of each feature, the authors conclude that, although the confusion matrices reveal some confusion between these classes, the features obtained in August are useful to detect cocoa.


# Dependencies
PyPDF2
nltk
transformers
sentence_transformers

# Model used for embedding generation
all-MiniLM-L6-v2.pt