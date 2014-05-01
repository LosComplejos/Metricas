import networkx as nx

class makeNetwork:

	def __init__(self):
		self.G = nx.Graph() #Grafo no dirigido

	def addCompleteSubGraph(self,idpub,terms):
#		print terms
#		print
		G=self.G
		# <addnode> #
		for i in terms:
			G.add_node(i)
		# </addnode> #

		# <addedge> #
		from itertools import combinations
		edges = combinations(terms, 2)
		for n in edges:
			n1=n[0]
			n2=n[1]
			if G.has_edge(n1,n2):
				G[n1][n2]['weight']+=1
			else: G.add_edge(n1,n2,weight=1)
		self.G=G
		# </addedge> #

	#for n in netw.G.edges_iter():
	#	n1=n[0]
	#	n2=n[1]
	#	print `netw.G[n1][n2]['weight']`+" : ("+n1+","+n2+")"

	def highest_centrality(self,cent_dict):
		"""Returns a tuple (node,value) with the node
		with largest value from Networkx centrality dictionary."""
		# Create ordered tuple of centrality data
		cent_items=[(b,a) for (a,b) in cent_dict.iteritems()]
		# Sort in descending order
		cent_items.sort()
		cent_items.reverse()
		return tuple(reversed(cent_items[0]))

	def getMainComponent(self):
		components =nx.connected_component_subgraphs(self.G)
		return components[0]

	def getBetweennessC(self):
		mc=self.getMainComponent()
		return nx.betweenness_centrality(mc)

	def getClosenessC(self):
		mc=self.getMainComponent()
		return nx.closeness_centrality(mc)

	def getEigenvectorC(self):
		mc=self.getMainComponent()
		return nx.eigenvector_centrality(mc)

	def getAvgDeg(self):
		G=self.G
		N,K = G.order(), G.size()
		return float(K)/N




class Inter_Union:
	def unique(self,a):
	    """ return the list with duplicate elements removed """
	    return list(set(a))

	def intersect(self,a, b):
	    """ return the intersection of two lists """
	    return list(set(a) & set(b))

	def union(self,a, b):
	    """ return the union of two lists """
	    return list(set(a) | set(b))
