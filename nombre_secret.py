nombre_secret = int(17)
#Penser a implementer un random100
print("Entrez un nombre")
nombre = int(input())
if nombre == nombre_secret:
        print ("C'est gagne !")
elif nombre < nombre_secret:
        print("C'est plus grand")
else:
        print("C'est plus petit")
print("Nif")
