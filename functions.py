import json

def show_students(estudiantes): #show student function
    if not estudiantes: #if to validate if the student is registered in class
        print("There is no registered students")
    else:
        print("The students registered are:")
        for student in estudiantes.keys(): #for loop to
            print(student)

def average_grade(estudiantes):
    user = input("Choose the student: ")
    if user not in estudiantes:
        print("Student not found in the class")
        return None
    
    notas = estudiantes[user].values()
    promedio = sum(notas) / len(notas)
    print(f"The average of {user} is: {promedio:.2f}")

def validate_grade(prompt="Enter grade (0-5): "):
    """
    Pide una nota al usuario y valida que sea entre 0-5
    
    Returns:
        float: Nota válida entre 0-5
    """
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 5:
                return grade
            else:
                print("Grade must be between 0 and 5")
        except ValueError:
            print("Please enter a valid number")

def upload_califications(estudiantes):
    """Permite actualizar la nota de un estudiante"""
    user = input("Choose the student: ")
    if user not in estudiantes:
        print("Student not found in the class")
        return
    
    # Mostrar notas actuales
    print(f"\nCurrent grades for {user}:")
    exams = list(estudiantes[user].keys())
    for i, exam in enumerate(exams, 1):
        nota = estudiantes[user][exam]
        print(f"{i}. {exam} - Current: {nota}")

    # Elegir examen
    try:
        choice = int(input("\nChoose exam number: ")) - 1
        if choice < 0 or choice >= len(exams):
            print("Invalid choice")
            return
    except ValueError:
        print("Must be a number")
        return
    
    exam_to_update = exams[choice]

    # Pedir nueva nota
    new_grade = validate_grade("Enter new grade: ")

    # Actualizar
    estudiantes[user][exam_to_update] = new_grade  
    print(f" Updated: {exam_to_update} = {new_grade}")

def average_calculus(estudiantes, user): #funct to calculate the average grade
    if user not in estudiantes:
        print("Student not found in the class")
        return
    
    notas = estudiantes[user].values()
    promedio = sum(notas) / len(notas)
    return promedio

def close_assignature(estudiantes):

    if not estudiantes:
        print("No students registered")
        return
    
    # Un solo ciclo para recorrer a todos los estudiantes
    for user, grades in estudiantes.items(): 
        # grades es el diccionario interno, e.g., {"Parcial 1": 1.5, ...}
        notas = grades.values()
        promedio = sum(notas) / len(notas)
        
        if promedio >= 3.0:
            status = "PASSED"
        else:
            status = "FAILED"
            
        print(f"Student: {user:12} | Final Grade: {promedio:.2f} | Status: {status}")



def close_program(estudiantes): #close program funct, returns false to send the signal to the main to close de menu
    with open("students.json", "w") as file:
        json.dump(estudiantes, file, indent=2)
    print("Closing the terminal...")
    return False


    