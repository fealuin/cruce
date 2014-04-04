fd = open('file.fdl','r')

for line in fd.readlines():
    line = line.strip() # eliminamos el \n
    parts = line.split(' ')
    campo = parts[0]
    tipo_dato = parts[1]
    print "nombre del campo:",campo
    print "tipo de dato:",tipo_dato
    print "------------------------"
