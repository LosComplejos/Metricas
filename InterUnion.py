
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
