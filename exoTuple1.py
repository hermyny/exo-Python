#Exercice 1 : Tri et Recherche dans une Liste de Tuples
#Écris un programme qui gère une liste de tuples représentant des étudiants. Chaque tuple contient le nom de l'étudiant et sa note. Le programme doit :
#1. Trier la liste des étudiants par note en ordre décroissant.
#2. Trier la liste des étudiants par ordre alphabétique.
#3. Trouver et afficher l'étudiant avec la meilleure note.
#4. Trouver et afficher l'étudiant avec la note la plus basse.


studentName = ["Rook", "Potin", "Mercier", "Avatar", "Justin", "Koffi", "Vladimir", "Quentin", "Poutin", "Trudeau", "Bellami", "Jordan", "Verrier", "Adam", "Calliope", "Huaut"]
studentAverage = [15, 14, 2, 14, 5, 8, 10, 20, 11, 20, 13,12,16,12, 11, 10 ]
for name, average in zip(studentName, studentAverage):
    print(name, average)


studentList = list(zip(studentName, studentAverage))
print(studentList)
studentList.sort(key=lambda x: x[1])
print(f'La liste des étudiants par ordre croissant de leurs moyennes est : ')
for name, average in studentList:
    print(f"{name}: {average}")

studentList.sort(key=lambda x: x[0])
print(f'La liste des étudiants par ordre alphabétique est : ')
for name, average in studentList:
    print(f"{name}: {average}")

studentListB = studentList.sort(key=lambda x: x[1], reverse =True)
print(f'La liste des étudiants par ordre décroissnt de leurs moyennes est : ')
for name, average in studentList:
    print(f"{name}: {average}")


max_average = max(studentAverage)
best_student = [name for name, average in studentList if average == max_average]
print(f"L'étudiant avec la meilleure moyenne est :")
for student in best_student:
    print(f"{student} avec une note de {max_average}")

maxAverage = 0
bestStudent = []

for name, average in studentList:
    if average > maxAverage:
        maxAverage = average
        bestStudent = [name]
    elif average == maxAverage:
        bestStudent.append(name)

print(f"L'étudiant avec la meilleure moyenne est :")
for student in bestStudent:
    print(f"{student} avec une note de {maxAverage}")

min_average = min(studentAverage)
lowest_student = [name for name, average in studentList if average ==min_average]
print(f"L'étudiant avec la moins bonne moyenne est :")
for student in lowest_student:
    print(f"{student} avec une note de {min_average}")



