from datetime import date, time, datetime


people = ["Rook", "Potin", "Mercier", "Avatar", "Justin", "Koffi", "Vladimir", "Quentin", "Poutin", "Trudeau", "Bellami", "Jordan", "Verrier", "Adam", "Calliope", "Huaut"]
birthday = ["22 Oct 2021", "06 Jan 1986", "7 Nov 1964", "13 Jun 2001", "6 May 1997", "13 Dec 1978", "14 Feb 1999", "19 Feb 1957", "7 Aug 2002", "19 Nov 1988", "7 Nov 1955", "10 Jul 1964", "24 May 1972", "2 Dec 1971", "7 Mar 1999", "29 Jun 1967"]
identity = list(zip(people, birthday))
for name, birthDate in identity:
    today = datetime.now()
    # Conversion de la date de naissance de chaîne de caractères à objet datetime
    try:
        birthDateFormatted = datetime.strptime(birthDate, "%d %b %Y")
    except ValueError as e:
        print(f"Erreur de format pour {name} avec la date {birthDate}: {e}")
        continue

    # Calcul de l'âge
    age = today.year - birthDateFormatted.year - (
                (today.month, today.day) < (birthDateFormatted.month, birthDateFormatted.day))

    # Affichage du nom et de l'âge
    print(f'{name} a {age} ans')