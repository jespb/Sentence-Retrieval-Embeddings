
from scipy.spatial import distance


def myDistance(t1, t2):
	"""
	Return the cosine distance between two vectors with the same size
	"""
	return distance.cosine(t1, t2)

def getDistances(embedding, embeddingDB):
	return [ myDistance(embedding, target[0]) for target in embeddingDB ]


class SelectClosest:
	embDB = None
	model = None

	def __init__(self, embDB, model):
		self.embDB = embDB
		self.model = model

	def attribute(self, sentence):
		emb = list(self.model.encode(sentence))

		distances = getDistances(emb, self.embDB)

		ind = distances.index(min(distances))

		return [ind]



