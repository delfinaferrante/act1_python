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

# Se combinan las preguntas, las respuestas y las respuestas correctas en una lista nueva
questions_to_ask = list(zip(questions, answers, correct_answers_index))

# Se seleccionan aleatoriamente 3 preguntas de la lista anterior, se deja de usar índices. Uso random.sample() para que no se repitan las preguntas
questions_to_ask = random.sample(questions_to_ask, k=3)

score = 0

# El usuario deberá contestar 3 preguntas. En cada iteración se muestra una tupla de la lista nueva
for una_pregunta, opciones_respuestas, respuesta_correcta in questions_to_ask:

    # Se muestra una pregunta y sus posibles respuestas
    print(una_pregunta)
    for i, answer in enumerate(opciones_respuestas):
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
        if answer_converted == respuesta_correcta:
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
        print(opciones_respuestas[respuesta_correcta])
         
    # Se imprime un blanco al final de la pregunta
    print()

print(f'El jugador obtuvo {score} puntos')
