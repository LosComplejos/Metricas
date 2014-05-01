class parseInvInd:

	def __init__(self,filename):
		self.name=filename
		self.TERM={}
		self.pub_terms={}
		self.term_pubs={}
		self.term_occs={}

	def pushTerms(self,idpub,term):
		if not self.pub_terms.has_key(idpub):
			self.pub_terms[idpub]={}
		self.pub_terms[idpub][term]=1
		
		if not self.term_pubs.has_key(term):
			self.term_pubs[term]={}
		self.term_pubs[term][idpub]=1

	def build__Pub_x_Terms(self):
		count=0
		f = open(self.name,"r")
		for line in f:
			line=line.replace("\n","")
			line=line[:-1]
			buf=line.split("(")
			term=buf[0]
			self.TERM[count]=term
			indinv=buf[1]
			events=indinv.split(";")
			eventos=[]
			for e in events:
				event=e.split("*")
				idpub=event[0]
				occ=event[1]
				event=[]
				event.append(idpub)
				event.append(occ)
				eventos.append(event)
			occs=0
			for i in eventos:
				idpub=i[0]
				self.pushTerms(idpub,count)
				occs+=int(i[1])
			self.term_occs[count]=occs
			count+=1
		f.close()
