from script3 import reset

name=input("Όνομα υπαλλήλου:")
sales=float(input("Πωλήσεις(evro):"))

commission=sales * 0.05

yellow="\033[33m"
green="\033[32m"
reset="\033[0m"

width=40

print("\n" + "=" * width)
print(f"{yellow}{'ΑΝΑΦΟΡΑ ΠΩΛΗΣΕΩΝ':^{width}}{reset}")
print("=" * width)

print(f"{'Υπάλληλος:':<20}{name:>20}")
print(f"{'Πωλήσεις:':<20}{sales:>20.2f}evro{reset}")
print(f"{'Προμήθεια:':<20}{green}{commission:>10.2f}evro{reset}")

print("="*width)