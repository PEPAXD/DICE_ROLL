import random
import os

def printWelcome():
    # Imprimir mensaje de bienvenida
    print("\nWelcome to the Dice Rolling Simulator!")
    print("-------------------------------------")

def dice_type():

    printWelcome()

    # Solicitar al usuario el número de dados a lanzar
    number_rolldice = int(input("How many dice would you like to roll? ---> "))

    # Mostrar los tipos de dados disponibles para elegir
    dice_types = ["d4","d6","d8","d12","d20","d100"]
    print("\nWhich dice would you like to roll?\n")

    for index, dice in enumerate(dice_types, start=1):
        print(f"{index} - ({dice})")

    while True:

        # Solicitar al usuario que elija un tipo de dado válido
        choice = int(input("\nEnter your choice (1-6) ---> "))
        if 1 <= choice <= 6:
            break
        # Mostrar mensaje de error si la elección no es válida
        print("Invalid choice. Please enter a number from 1 to 6.")

    #clean terminal
    os.system('cls')

    # Obtener el número de lados del dado elegido
    sides = [4, 6, 8, 12, 20, 100][choice - 1]

    return number_rolldice, sides

def roll_dice(number_rolldice, number_sides):

    printWelcome()
    total = 0

    for numberRoll in range(1, number_rolldice + 1):

        # Generar un número aleatorio para cada lanzamiento de dado
        rollnumber = random.randint(1, number_sides)
        print(f"{numberRoll}) - roll is: {rollnumber}")

        # Sumar el nÚmero de lanzamiento de dado al total
        total += rollnumber
    print("\nTOTAL --->", total)

def roll_again():

    # Solicitar al usuario si desea volver a lanzar los dados
    roll_again = input("\nWould you like to roll again? (y/n) ---> ")
    if roll_again.lower() == 'y':
        os.system("cls")
        main()
    else:
        print("\nThank you for using the Dice Rolling Simulator!")

def main():

    # Obtener el nÚmero de dados y el nÚmero de lados a usar
    number_rolldice, number_sides = dice_type()

    #  Lanzar los dados
    roll_dice(number_rolldice, number_sides)

    # Solicitar al usuario si desea volver a lanzar los dados
    roll_again()

if __name__ == '__main__':
    main()
