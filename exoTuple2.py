# exo 2

months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
amounts = [17888, 24558, 4452, 8799, 6654, 12000, 35471, 25930, 11712, 32360, 15078, 21457]
amount_per_month = list(zip(months, amounts))
for month, amount in amount_per_month :
    print(f'{month} : {amount} euros')

maxAmount = max(amounts)
bestMonths = [month for month, amount in amount_per_month if amount ==maxAmount]
print('Le mois avec la meilleure vente est  : ')
for month in bestMonths:
    print(f'{month} avec un montant de {maxAmount} euros')



minAmount = min(amounts)
lowAmount = [month for month, amount in amount_per_month if amount ==minAmount]
print('Le mois avec les moins bonnes ventes est : ')
for month in lowAmount:
    print(f'{month} avec un montant de {minAmount} euros')



totalAmount = sum(amount for month, amount in amount_per_month)
print(f" Les recettes annuelles s'élèvent à {totalAmount}  euros")


averageAmount = totalAmount/len(amount_per_month)
print(f" La moyenne des ventes s'élève à {averageAmount}  euros")