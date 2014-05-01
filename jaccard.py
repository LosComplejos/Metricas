
#import pprint as p
import numpy
from readInvInd import parseInvInd
import sys
from NetworkMetrics import makeNetwork
from InterUnion import Inter_Union

#nombre de indice invertido se recibe como argumento
filename=sys.argv[1]
ii=parseInvInd(filename)
ii.build__Pub_x_Terms()
filename=filename.replace(".txt","")

pub_terms=ii.pub_terms
term_occs=ii.term_occs
term_pubs=ii.term_pubs
TERM=ii.TERM # diccionario   id termino <=> nombre termino

netw=makeNetwork()
for idpub in pub_terms:
	terms=pub_terms[idpub]
	netw.addCompleteSubGraph(idpub,terms)
N=len(netw.G)
print N
print "-----"



term_jaccards={}
def pushJacc(n1,n2,jacc):
	if not term_jaccards.has_key(n1):
		term_jaccards[n1]=[]
	term_jaccards[n1].append(jacc)
	
	if not term_jaccards.has_key(n2):
		term_jaccards[n2]=[]
	term_jaccards[n2].append(jacc)

G=netw.G
calc=Inter_Union()
for n in G.edges_iter():
	n1=n[0]
	n2=n[1]
#	print TERM[n1],TERM[n2]
	Pn1=sorted(term_pubs[n1].keys())
	Pn2=sorted(term_pubs[n2].keys())
#	print Pn1
#	print Pn2
	inter=calc.intersect(Pn1,Pn2)
	if inter!=0:
		union=calc.union(Pn1,Pn2)
#		print "\tintersect",inter
#		print "\tunion",union
		jacc=round(len(inter)/float(len(union)),4)
#		print "\t\tjaccard",jacc
		pushJacc(n1,n2,jacc)

file=open(filename+"__jaccard.txt","w")
for i in term_jaccards:
	jaccs=term_jaccards[i]
#	print TERM[i],jaccs
	prom=round((sum(jaccs)/float(len(jaccs))),4)
	stdv=round(numpy.std(jaccs),4)
	file.write(TERM[i]+"\t"+`prom`+"\t"+`stdv`+"\n")
#	print "\t",prom,stdv
file.close()

print filename+" END"

























