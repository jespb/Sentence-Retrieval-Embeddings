from transformers import AutoModel
from transformers import pipeline
import os.path
from joblib import load, dump
from tqdm import tqdm




def calculateEmbedding(model, text):
	tmp = list(model.encode(text))
	return tmp



def makeEmbeddingDatabase(model, filename):

	# TODO: as is, its a bit finicky, fix later
	if filename == "EMLES.pdf":
		from precomputed.EMLES import data as dataset
	else:
		raise IOError("There is no %s.py file in the precomputed directory." % (filename.split(".")[0]))

	# Import data
	print("Creating embedding database...", end="")
	current_source = "NO_SOURCE"
	emb_cit_src = []
	for line_i in tqdm(range(len(dataset))):# Tokenize the input text
		emb_cit_src.append( [ calculateEmbedding(model, dataset[line_i]), line_i] )
	print("[DONE]")
	return emb_cit_src



def getEmbeddingDB(model, modelname, filename):
	dumpname = "%s_%s.lib" %(filename, modelname) 
	if not os.path.isfile( dumpname ):
		print("Dump file not found, generating embeddings")
		embeddingDB = makeEmbeddingDatabase(model, filename)
		print("Creating dump file for this pair of filename and modelname")
		dump( embeddingDB, dumpname )
	else:
		print("Dump file found, loading embeddings")
		embeddingDB = load( dumpname )
	return embeddingDB


