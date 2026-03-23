item=input("Προϊόν:")
price=float(input("Τιμή:"))

blue="\033[34m"
green="\033[32m"
reset="\033[0m"

print(f"{blue}{item:<20}{reset}{green}{price:>10.2f}evro{reset}")