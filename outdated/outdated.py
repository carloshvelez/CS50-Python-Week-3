meses = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:

        a_domini = input("Date: ").strip()

        if a_domini[0].isdigit():
            mes, dia, año = a_domini.split("/")

        elif a_domini[0].isalpha():
            mes, dia, año = a_domini.split()
            if len(dia) < 2:
                continue
            dia = dia.strip(",")
            mes = meses.index(mes.capitalize()) + 1

        if int(dia) > 31 or int(mes) > 12:
            continue
        break

    except ValueError:
        pass

print(f"{int(año)}-{int(mes):02d}-{int(dia):02d}")
