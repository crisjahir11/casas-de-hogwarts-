
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

while True:
    try:
        pregunta1 = int(input("A) Do you like Dawn or Dusk? \n\t1)Dawn \n\t2)Dusk\n"))
        if pregunta1 == 1:
            Gryffindor += 0 + 1
            Ravenclaw += 0 + 1
        elif pregunta1 == 2:
            Hufflepuff += 0 + 1
            Slytherin += 0 + 1
        else:
            print("\nSolo puede ingresar un número del 1-2")
        break
    except ValueError:
        print("\nSolo puede ingresar un número del 1-2")
while True:
    try:
        pregunta2 = int(input("Q2) When I’m dead, I want people to remember me as: \n\t1) The Good \n\t2) The Great \n\t3) The Wise \n\t4) The Bold\n"))
        if pregunta2 == 1:
            Hufflepuff += 0 + 2
        elif pregunta2 == 2:
            Slytherin += 0 + 2
        elif pregunta2 == 3:
            Ravenclaw += 0 + 2
        elif pregunta2 == 4:
            Gryffindor += 0 + 2
        else:
            print("\nSolo puede ingresar un número del 1-4\n")
        break
    except ValueError:
        print("\nSolo puede ingresar un número del 1-4\n")
while True:
    try: 
        pregunta3 = int(input("Q3) Which kind of instrument most pleases your ear? \n\t1) The violin \n\t2) The trumpet \n\t3) The piano \n\t4) The drum\n"))
        if pregunta3 == 1:
            Slytherin += 0 + 4
        elif pregunta3 == 2:
            Hufflepuff += 0 + 4
        elif pregunta3 == 3:
            Ravenclaw += 0 + 4
        elif pregunta3 == 4:
            Gryffindor += 0 + 4
        else:
            print("\nSolo se puede ingresar un número del 1-4\n")
        break
    except ValueError:
        print("\nSolo se puede ingresar un número del 1-4\n")
print(f"\nGryffindor: {Gryffindor}")
print(f"Ravenclaw: {Ravenclaw}")
print(f"Hufflepuff: {Hufflepuff}")
print(f"Slytherin: {Slytherin}\n")

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    print(f"\nSu casa pertenece a Gryffindor con {Gryffindor} puntos.\n")
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print(f"\nSu casa pertenece a Ravenclaw con {Ravenclaw} puntos.\n")
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print(f"\nSu casa pertenece a Hufflepuff con {Hufflepuff} puntos.\n")
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
    print(f"\nSu casa pertenece a Slytherin con {Slytherin} puntos.\n")
else:
    print("\nSu casa no ha podido ser asignada\n")
