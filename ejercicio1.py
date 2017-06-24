message="hello world! Hey: "
amount= 10*5 

print message + str(amount)

numero = 500

if numero == 500:
	print "Es igual a 500"
elif numero <500:
	print "El numero es menor a 500"
else:
	print "Es mayor a 500"

nombre= "Christian"
'''
for x in nombre:
	print x

'''
animals = ['dog','cat','bird']

print animals
print animals[0]

animals.append('horse')
animals[1]= 'gato'
for x in animals:
	print x

#Diccionario
#aqui no importa el tab o index
alumno = {'nombre':'Leonidas',
		'edad':32,
		'direccion':'calle los telares 247'
	}

#mostramos solo direccion

print alumno['direccion']

def PrintDictionary(TheDictionary):
	for key in TheDictionary:
		print key + "=" + str(TheDictionary[key])

PrintDictionary(alumno)

software = { 'title':'Odoo','type':'Business' }

PrintDictionary(software)
