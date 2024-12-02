# Sentence-Retrieval-Embeddings
Sentence-level information retrieval using embeddings

As is, the main.py script follows these steps:

- decompose a .pdf file into a list of sentences
- calculates the embeddings of each sentence using mini llama
- calculates the embedding of "This work deals with the detection of cocoa agroforest."
- associates this sentence with the sentence in the pdf with the closest embedding using the cosine distance
