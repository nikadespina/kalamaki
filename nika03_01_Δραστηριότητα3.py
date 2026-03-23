message = input("Ποιά είναι η γλώσσα προγραμματισμού που κάνεις τώρα;")
print("\n"+"Το μήκος του μηνύματος είναι:")
print(len(message))
print("\n"+"Tο μήνυμα με κεφαλαία είναι:")
print(message.upper())
result = "Python" in message
print("\n"+"Υπάρχει η λέξη Python στο μήνυμα;")
print("Η λέξη Python υπάρχει στο μήνυμα:",result)