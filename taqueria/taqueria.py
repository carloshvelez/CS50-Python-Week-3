# Permitir al usuario hacer una orden:
# Solicitar los items, uno por línea, hasta que el usuario presione control_d
# Mostrar el costo total de todos los itemes, prefijado con el símbolo $ y con dos decimales.
# El input del usuario es case insensitive; ignora cualquier input que no es un item. Asume que cada item en el menu tiene mayúscula de título


# 1. Agregar un diccionario con los items.

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


# 2. Dentro de un ciclo while, Solicitar el input del usuario (hasta que presione control D.); quizá tenga que imprimir una nueva \n:

sumador = 0
while True:
    try:
        orden = input("Item: ").strip().title()

        ##. Buscar en el diccionario y agregar a un sumador el valor de cada item.
        sumador += menu[orden]
        print(f"Total: ${sumador:.2f}")

    ## Si el usuario ingresa una clave que no está, esto es un Key error, por lo tanto, la excepción es un pass.
    except KeyError:
        pass

    ## Si el usuario ingresa un ctrl - D, esto es un EOFError, por lo tanto, la excepción será un imprimir el sumador.
    except EOFError:
        print(f"\nTotal: ${sumador:.2f}")
        break
