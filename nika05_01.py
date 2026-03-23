players = []
goals = []
assists = []
total_goals = 0
total_assists = 0
average_goals = 0
average_assists = 0

#========================
#ΕΙΣΑΓΩΓΗ ΠΛΗΘΟΥΣ ΠΑΙΚΤΩΝ
#========================
while True:
    count_text = input("Πόσοι παίκτες θα καταχωριστούν;")

    if count_text.isdigit():
        count = int(count_text)

        if count > 0:
            break
        else:
            print("Δώσε αριθμό μεγαλύτερο από το 0.")
    else:
        print("Μη έγκυρη τιμή. Δώσε μόνο θετικό ακέραιο αριθμό.")
#========================
#ΕΙΣΑΓΩΓΗ ΣΤΟΙΧΕΙΩΝ ΠΑΙΚΤΩΝ
#========================
for i in range(count):
    print(f"\nΚαταχώριση παίκτη {i+1}")
    #Είσοδος ονόματος με έλεγχο
    while True:
        name = input("Όνομα παίκτη:").strip()

        if name == "":
            print("Το όνομα δεν μπορεί να είναι κενό.")
        else:
            break
    #Είσοδος γκολ με έλεγχο
    while True:
        goals_text = input("Γκολ:")

        if goals_text.isdigit():
            player_goals = int(goals_text)
            break
        else:
            print("Μη έγκυρη τιμή. Δώσε μόνο μη αρνητικό ακέραιο αριθμό.")
    #Είσοδος ασίστ με έλεγχο
    while True:
        assists_text = input("Ασίστ:")

        if assists_text.isdigit():
            player_assists = int(assists_text)
            break
        else:
            print("Μη έγκυρη τιμή. Δώσε μόνο μη αρνητικό ακέραιο αριθμό.")
    #Αποθήκευση των δεδομένων στις αντίστοιχες λίστες
    players.append(name)
    goals.append(player_goals)
    assists.append(player_assists)
#===========================
#ΕΜΦΑΝΙΣΗ ΑΠΟΤΕΛΕΣΜΑΤΩΝ
#===========================
print("\n---ΣΤΑΤΙΣΤΙΚΑ ΠΑΙΚΤΩΝ---")
#Μεταβλητές για τον καλύτερο παίκτη
best_player = ""
best_total = -1

for i in range(len(players)):
    total_contribution = goals[i] + assists[i]

    #Χαρακτηρισμός παίκτη με χρήση if-else -else
    if total_contribution > 10:
        level = "Εξαιρετική συμβολή"
    elif total_contribution >=5 :
        level = "Καλή συμβολή"
    else:
        level = "Μικρή συμβολή"

    print(f"Παίκτης:{players[i]}")
    print(f"Γκολ:{goals[i]}")
    print(f"Ασίστ:{assists[i]}")
    print(f"Συνολική συμμετοχή:{total_contribution}")
    print(f"Χαρακτηρισμός:{level}")
    print("-----------------------------")
    #λεγχος για τον καλύτερο παίκτη
    if total_contribution > best_total:
        best_total = total_contribution
        best_player = players[i]

print(f"\nΟ παίκτης με τη μεγαλύτερη συνολική συμμετοχή είναι: {best_player}")
print(f"Συνολική συμμετοχή:{best_total}")

for i in range(len(players)):
    total_goals =total_goals +goals[i]
    total_assists =total_assists +assists[i]
print(f"Το συνολικό πλήθος γκολ όλων των παιχτών:{total_goals}")
print(f"Το συνολικό πλήθος ασίστ όλων των παιχτών:{total_assists}")
    average_goals = total_goals / len(players)
    average_assists = total_assists / len(players)
    print(f"Η μέση τιμή γκολ είναι:{average_goals}")
    print(f"Η μέση τιμή ασίστ είναι:{average_assists}")









































