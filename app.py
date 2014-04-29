f = open("InvDict_bigrams.txt","r")
for line in f:
	line=line.replace("\n","")
	line=line[:-1]
	buf=line.split("(")
	term=buf[0]
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
	print term
	print eventos
	print
