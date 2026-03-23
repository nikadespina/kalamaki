amount=float(input("Ποιό είναι το ποσό αγοράς;"))
if amount > 100:
    value_ekptosis=amount*0.10
    final=amount-value_ekptosis
    print(f"Το συνολικό ποσό είναι:{final:.2f}")
else:
    final=amount
    print(f"Το συνολικό ποσό είναι:{final:.2f}")