#IMPORTS 
import json
with open("students.json", "r") as data:
    estudiantes = json.load(data)

from functions import show_students, average_grade, close_assignature, close_program,upload_califications

menu = True #menu variable to control de flow of the program an close it with funct

while menu:
    print("\n----------MENU----------")#opciones para usuario
    print("1. Student list")
    print("2. Average grades")
    print("3. Upload calification")
    print("4. Close assignature")
    print("5. Exit")

    opcion = input("Choose an option: ")#input usuario para opciones

    if opcion == "1": #Student list
        print()
        show_students(estudiantes)
    elif opcion == "2":
        print()
        average_grade(estudiantes)
    elif opcion == "3":
        print()
        upload_califications(estudiantes)
    elif opcion == "4":
        print()
        close_assignature(estudiantes)
    elif opcion == "5":
        print()
        menu = close_program(estudiantes)
    else:
        print()
        print("Invalid option, please enter one of the below")
            