

from scripts.args import *
import os.path

filename="EMLES.pdf"
modelname = "MiniLM_L6_v2"


#
# Loads pdf and extracts a list to sentences to be saved in a .py file
#

sentence_output_file = "%s%s.py" % (PRECOMP_DIR, filename.split(".")[0])

from scripts.decomposePDF import extract_sentences_from_pdf, write_sentences_to_file

sentences = extract_sentences_from_pdf(FILE_DIR + filename)

if filename == "EMLES.pdf":
	# Removes the acknowledgements and references from the paper, 
	# since they are not necessary for this task.
	i = 0
	while not "Acknowledgements" in sentences[i]:
		i += 1
	sentences = sentences[:i]


write_sentences_to_file( sentence_output_file , sentences)




#
# Load embedding database 
# (calculates DB, if dumpfile does not exist)
#

from scripts.generateEmbeddings import getEmbeddingDB
from sentence_transformers import SentenceTransformer, models

model_dir = '/home/jebatista/Desktop/Desktop/Attribution/Attribution_old/LLM/all-MiniLM-L6-v2.pt'
model_st = SentenceTransformer(model_dir, device="cpu")

embDB = getEmbeddingDB(model_st, modelname, filename)



#
# Attributes sentences to input
#


from scripts.decomposePDF import tokenize
from attribution.selectClosest import SelectClosest

input_ = "This work deals with the detection of cocoa agroforest."
input_ = tokenize(input_)

model = SelectClosest(embDB, model_st)

for sentence in input_:

	sent_list = model.attribute(sentence)

	for index in sent_list:
		print(sentences[index])

