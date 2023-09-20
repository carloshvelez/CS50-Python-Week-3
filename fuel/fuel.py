while True:
    try:
        cantidad_g = input("Fraction: ")
        x, y = cantidad_g.split("/")
        if int(x) > int(y):
            continue
        porcentaje = int(x) / int(y)

        break
    except (ValueError, ZeroDivisionError):
        pass

if porcentaje >= 0.99:
    print("F")
elif porcentaje <= 0.01:
    print("E")
else:
    print (f"{int(round(porcentaje * 100))}%")






