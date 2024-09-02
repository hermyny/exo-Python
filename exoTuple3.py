product = ["cake", "juice", "apple","oil bottle", "egg","chicken", "milk bootle"]
quantity = [2, 5, 10, 2, 12, 1, 6 ]
priceForOne = [2.75, 1.80, 1.1, 3.5, 0.56, 7.80, 1.6]
invoice = list(zip(product, quantity, priceForOne))
print(f'voici la facture établie : ')
print(f'{invoice}')

totalPrice = [(prod, qty*price) for prod, qty, price in invoice]
print(f'Facture détaillée : ')
for prod, totalP in totalPrice:

    print(f'{prod} : {totalP: .2f} euros ')

maxTotalPrice = max(totalPrice, key=lambda item: item[1])
prod, totalP = maxTotalPrice
print(f'Produit avec le prix total maximum : {prod} avec un montant de {totalP:.2f} euros')

minTotalPrice = min(totalPrice, key=lambda item: item[1])
prod, totalP = minTotalPrice
print(f'Produit avec le prix total le plus bas : {prod} avec un montant de {totalP:.2f} euros')

totalInvoice = sum(totalP for _, totalP in totalPrice)
print(f"Le total de votre facture est de : {totalInvoice:.2f} euros")


