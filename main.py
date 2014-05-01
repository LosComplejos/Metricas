
#import pprint as p
import numpy
from readInvInd import parseInvInd
import sys
from NetworkMetrics import makeNetwork

#nombre de indice invertido se recibe como argumento
filename=sys.argv[1]
ii=parseInvInd(filename)
ii.build__Pub_x_Terms()
filename=filename.replace(".txt","")

pub_terms=ii.pub_terms
term_occs=ii.term_occs
TERM=ii.TERM # diccionario   id termino <=> nombre termino

netw=makeNetwork()
for idpub in pub_terms:
	terms=pub_terms[idpub]
	netw.addCompleteSubGraph(idpub,terms)
N=len(netw.G)
print N
print "-----"

#OCURRENCIAS
file=open(filename+"__occs.txt","w")
for i in term_occs:
	file.write(TERM[i]+"\t"+`term_occs[i]`+"\n")
#	print TERM[i]+"\t"+`term_occs[i]`
file.close()

##COOCURRENCIAS
file=open(filename+"__cooccs.txt","w")
G=netw.G
for i in G.nodes_iter():
	if G[i]:
		weights=[]
		for j in G[i]:
			w=G[i][j]['weight']
#			file.write(TERM[i]+","+TERM[j]+"\t"+`w`)
			weights.append(w)
		prom = round(sum(weights)/float(len(weights)),4)
		stdv = round(numpy.std(weights),4)
		file.write(TERM[i]+"\t"+`prom`+"\t"+`stdv`+"\n")
file.close()

print filename+" occs+cooccs END"


