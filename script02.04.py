price=float(input("Δώσε τιμή προϊόντος:"))

print(f"Όπως δόθηκε:{price}")
print(f"Με 2 δεκαδικά:{price:.2f}")
print(f"Με 4 δεκαδικά:{price:.4f}")

item=input("Όνομα προϊόντος:")
price=float(input("Τιμή:"))

print(f"{item:<20}{price:>10.2f}evro")

revenue=float(input("Δώσε ποσό(π.χ.τζίρος):"))
rate=float(input("Δώσε ποσοστό ως δεκαδικό (π.χ. 0.075):"))

print(f"Ποσό με χιλιάδες:{revenue:,.2f}evro")
print(f"Ποσοστό:{rate:.1%}")
print(f"Επιστημονική γραφή:{revenue:.3e}")

customer=input("Πελάτης:")

item1=input("Προϊόν 1:")
price1=float(input("Τιμή 1:"))
qty1=float(input("Ποσότητα 1:"))

item2=input("Προϊόν 2:")
price2=float(input("Τιμή 2:"))
qty2=float(input("Ποσότητα 2:"))

line1=price1*qty1
line2=price2*qty2

subtotal=line1+line2
vat=subtotal*0.24
total=subtotal+vat

width=50
print("\n"+"="*width)

print(f"{'ΑΝΑΦΟΡΑ ΠΩΛΗΣΗΣ':^{width}}")
print("="*width)
print(f"(Πελάτης:{customer})")
print("-"*width)
print(f"{'Προϊόν':<20}{'Ποσ.':>7}{'Σύνολο':>13}")
print("-"*width)

print(f"{item1:<20}{qty1:>7.0f}{price1:>10.2f}{line1:>13.2f}")
print(f"{item2:<20}{qty2:>7.0f}{price2:>10.2f}{line2:>13.2f}")

print("-"*width)
print(f"{'Καθαρή Αξία':<37}{subtotal:>13.2f}")
print(f"{'ΦΠΑ 24%:':<37}{vat:13.2f}")
print(f"{'ΣΥΝΟΛΟ:':<37}{total:>13,.2f}")
print("-"*width)























