from random import randint
pierre = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
ciseau = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
papier = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
print("0 pour Pierre/1 pour feuille/2 pour Ciseau")
while True:
    ch=input("0/1/2 :")
    if not ch.isdigit():
        print("Vous aves entré un choix invalid")
    elif not int(ch) in range(0,3):
        print("Vous aves entré un choix invalid")
    else:
        break
pc=str(randint(0,2))
print("votre tour :\n")
if ch=="0":
    print(pierre)
elif ch=="1":
    print(papier)
else:
    print(ciseau)
print("Tour de l'ordinateur:\n")
if pc=="0":
    print(pierre)
elif pc=="1":
    print(papier)
else:
    print(ciseau)
if ch==pc:
    print("Egalité")
else:
    if ch=="0":
        if pc=="2":
            print("Gagnant")
        else:
            print("Perdent")
    elif ch=="1":
        if pc=="0":
            print("Gagnant")
        else:
            print("Perdent")
    else:
        if pc=="1":
            print("Gagnant")
        else:
            print("Perdent")