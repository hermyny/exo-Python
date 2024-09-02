import statistics

#exercice 1

#exo 1.1

a = 5
b = 10
print(f'La variable a = {a} et la variable b = {b}')

a, b = b, a
print(f'Après le changement, la variable a = {a} et la variable b = {b}')

#exo 1.2

moyenne = [2,4,6]
moy = sum(moyenne)/len(moyenne)

print (f'On peut calculer en additionnant la somme de moyenne et en la divisant par la longueur de moyenne et on obtient {moy}')

print(f'La moyenne de ces trois variables est {statistics.mean(moyenne)}')


#exercice 2


#exo 2.1

firstname = "prénom"
name = "nom"

print(f'Votre identité est {firstname} {name}')


#exo 2.2
number = 23


print(f'Le nombre en tant que chaine de caractère est {str(number)}')

#exercice 3

#exo 3.1

listName = ["Hugo", "Thibaut", "Jean"]

listName.append("Marc")

listName.append("Josh")

print(f'La nouvelle liste des prénoms est {listName}')


#exo 3.2

scoreFirst = 32
scoreSecond = 63
scoreThird = 85
listScore = [scoreFirst, scoreSecond, scoreThird]
print(f'La moyenne des scores est {sum(listScore)/len(listScore)} ')


#exo 4.1

#print('Veuillez renseigner votre âge')
#age = int(input())
#if age >= 18:
        #print(f" Vous avez {age}, vous êtes autorisés à accéder à l'interface")
#else :
        #print(f'Vous avez {age}, vous êtes mineur, accès refusé')

#exo 4.2

numbers = [1,2,3,4,5]
for numb in numbers :
    print(numb)

#exo 5.2
print('Veuillez renseigner un rayon')
r = int(input())
pi = 3.14159
print(f"L'aire de ce cercle est {pi*r*r}")