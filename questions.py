import random
import sys

# Preguntas para el juego
questions = ["¿Qué función se usa para obtener la longitud de una cadena en Python?",
            "¿Cuál de las siguientes opciones es un número entero en Python?",
            "¿Cómo se solicita entrada del usuario en Python?",
            "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
            "¿Cuál es el operador de comparación para verificar si dos valores son iguales?"] 

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [("size()", "len()", "length()", "count()"),
            ("3.14", "'42'", "10", "True"),
            ("input()", "scan()", "read()", "ask()"), 
            ("// Esto es un comentario", "/* Esto es un comentario */", "-- Esto es un comentario", "# Esto es un comentario"),
            ("=", "==", "!=", "===")] 

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

score = 0
# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")

    #Variable booleana para hacer seguimiento a las respuestas del usuario y sumar/restar puntos
    correct = False 

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta:")

        #Verifico que la respuesta sea un numero y que este dentro del rango
        if not user_answer.isdigit() or not (1 <= int(user_answer) <= 4): 
            print("Respuesta inválida.")
            sys.exit(1)
        
        #Si es válido, lo convierto a entero
        answer_converted = int(user_answer) - 1 

        # Se verifica si la respuesta es correcta
        if answer_converted == correct_answers_index[question_index]:
            print("¡Correcto!")
            score += 1
            correct = True
            break
        else:
            print("Incorrecto")
            score -= 0.5

    if not correct:
        # Si el usuario no responde correctamente después de los 2 intentos, se muestra la respuesta correcta y se resta 0.5
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])
         
    # Se imprime un blanco al final de la pregunta
    print()

print(f'El jugador obtuvo {score} puntos')
