import turtle


def calcula_angulo():
    from datetime import datetime

    atual = datetime.now().strftime("%H:%M:%S")
    print(atual)
    lista = atual.split(":")
    hora = int(lista[0])
    minutos = lista[1]
    segundos = lista[2]

    if hora > 12:
        hora = hora - 12

    graus_segundos = (int(segundos) * 360) // 60
    graus_minutos = ((int(minutos) * 360) // 60) + ((int(segundos) * 6) // 60)
    graus_horas = ((hora * 360) // 12) + ((int(minutos) * 30) // 60)

    return [graus_horas, graus_minutos, graus_segundos]


def main():
    turtle.title("Relógio tic-tac")
    turtle.bgcolor("black")

    tortuguita = turtle.Turtle()

    tortuguita.home()
    tortuguita.shape("turtle")

    # Formato do relógio
    tortuguita.penup()
    tortuguita.speed(7)
    tortuguita.goto(0, -250)
    tortuguita.pendown()
    tortuguita.setheading(0)
    tortuguita.pen(pencolor="yellow", fillcolor="green", pensize=5)
    tortuguita.fillcolor("brown")
    tortuguita.begin_fill()
    tortuguita.circle(250)
    tortuguita.end_fill()
    tortuguita.penup()
    tortuguita.goto(0, -200)
    tortuguita.pendown()
    tortuguita.fillcolor("white")
    tortuguita.begin_fill()
    tortuguita.circle(200)
    tortuguita.end_fill()
    tortuguita.penup()
    tortuguita.home()
    tortuguita.pendown()

    # Riscos minutos
    tortuguita.penup()
    tortuguita.home()
    tortuguita.setheading(90)
    tortuguita.pencolor("black")
    for riscos in range(0, 60):
        tortuguita.forward(200)
        tortuguita.pendown()
        if riscos % 5 == 0:
            tortuguita.back(20)
            tortuguita.penup()
            tortuguita.back(180)
        else:
            tortuguita.back(10)
            tortuguita.penup()
            tortuguita.back(190)
        tortuguita.right(6)

    # Marca do relogio
    tortuguita.penup()
    tortuguita.goto(0, 60)
    tortuguita.pendown()
    tortuguita.pen(pencolor='green')
    tortuguita.write("ROLEX", False, align="center", font=("wide latin", 12, "normal"))

    # Numeros das horas
    tortuguita.penup()
    tortuguita.home()
    tortuguita.pen(pencolor='blue')
    tortuguita.right(-90)
    for hora in range(1, 13):
        tortuguita.right(30)
        if hora in range(4, 9):
           tortuguita.forward(170)
        else:
            tortuguita.forward(150)
        tortuguita.write(f"{hora}", False, align="center", font=("arial", 20, "normal"))
        tortuguita.goto(0, 0)

    # Data
    from datetime import date
    dia = str(date.today()).split("-")[2]
    tortuguita.goto(-80, -10)
    tortuguita.write(dia, align="center", font=('broadway', 15, "normal"))
    tortuguita.goto(-80, -20)
    tortuguita.pencolor("black")
    tortuguita.pendown()
    tortuguita.setheading(0)
    tortuguita.pen(pensize=2)
    tortuguita.circle(20)
    tortuguita.penup()

    # Coroa:
    tortuguita.home()
    tortuguita.pencolor("yellow")
    tortuguita.fillcolor("yellow")
    tortuguita.begin_fill()
    tortuguita.goto(-20, 80)
    tortuguita.setheading(90)
    tortuguita.pendown()
    tortuguita.forward(20)
    tortuguita.right(135)
    for voltas in range(2):
        tortuguita.forward(14.142)
        tortuguita.left(90)
        tortuguita.forward(14.142)
        tortuguita.right(90)
    tortuguita.right(45)
    tortuguita.forward(20)
    tortuguita.right(90)
    tortuguita.goto(-20, 80)
    tortuguita.end_fill()
    tortuguita.penup()
    tortuguita.fillcolor("green")
    tortuguita.goto(0, 0)

    # Ponteiro dos minutos:
    lista_angulos = calcula_angulo()
    tortuguita.pen(pencolor="black", fillcolor="green", pensize=3, pendown=True)
    tortuguita.speed(1)
    tortuguita.setheading(90)
    tortuguita.right(lista_angulos[1])
    tortuguita.forward(130)
    tortuguita.left(135)
    tortuguita.forward(10)
    tortuguita.back(10)
    tortuguita.left(90)
    tortuguita.forward(10)
    tortuguita.penup()
    tortuguita.home()
    tortuguita.pendown()

    # Ponteiro das horas:
    tortuguita.setheading(90)
    tortuguita.right(lista_angulos[0])
    tortuguita.forward(80)
    tortuguita.left(135)
    tortuguita.forward(10)
    tortuguita.back(10)
    tortuguita.left(90)
    tortuguita.forward(10)
    tortuguita.penup()
    tortuguita.home()
    tortuguita.pendown()

    # Ponteiro dos segundos
    tortuguita.setheading(90)
    tortuguita.right(lista_angulos[2])
    tortuguita.pen(pencolor='red')
    tortuguita.forward(175)
    tortuguita.penup()
    tortuguita.home()

    # Movimento dos ponteiros
    from time import sleep
    tortuguita.speed(0)
    aux = True
    lista_angulos_aux = lista_angulos[:]
    while aux:
        sleep(0.5)
        lista_nova_angulos = calcula_angulo()

        # Apagar o ponteiro segundos
        tortuguita.home()
        tortuguita.setheading(90)
        tortuguita.right(lista_angulos_aux[2])
        tortuguita.pencolor("white")
        tortuguita.pendown()
        tortuguita.forward(175)
        tortuguita.penup()

        # Refazer o ponteiro segundos
        tortuguita.home()
        tortuguita.setheading(90)
        tortuguita.right(lista_nova_angulos[2])
        tortuguita.pencolor('red')
        tortuguita.pendown()
        tortuguita.forward(175)
        tortuguita.penup()
        lista_angulos_aux[2] = lista_nova_angulos[2]

        # Apagar o ponteiro minutos:
        if lista_nova_angulos[1] != lista_angulos_aux[1]:
            print(lista_nova_angulos[1], lista_angulos_aux[1])
            tortuguita.home()
            tortuguita.pen(pencolor="white", fillcolor="green", pensize=3, pendown=True)
            tortuguita.setheading(90)
            tortuguita.right(lista_angulos_aux[1])
            tortuguita.forward(130)
            tortuguita.left(135)
            tortuguita.forward(10)
            tortuguita.back(10)
            tortuguita.left(90)
            tortuguita.forward(10)
            tortuguita.penup()
            tortuguita.home()

            # Refazer o ponteiro
            tortuguita.pen(pencolor="black", fillcolor="green", pensize=3, pendown=True)
            tortuguita.setheading(90)
            tortuguita.right(lista_nova_angulos[1])
            tortuguita.forward(130)
            tortuguita.left(135)
            tortuguita.forward(10)
            tortuguita.back(10)
            tortuguita.left(90)
            tortuguita.forward(10)
            tortuguita.penup()
            tortuguita.home()
            lista_angulos_aux[1] = lista_nova_angulos[1]

        # Apagar o ponteiro horas:
        if lista_nova_angulos[0] != lista_angulos_aux[0]:
            tortuguita.pen(pencolor="white", fillcolor="green", pensize=3, pendown=True)
            tortuguita.setheading(90)
            tortuguita.right(lista_angulos_aux[0])
            tortuguita.forward(80)
            tortuguita.left(135)
            tortuguita.forward(10)
            tortuguita.back(10)
            tortuguita.left(90)
            tortuguita.forward(10)
            tortuguita.penup()
            tortuguita.home()

            # Refazer o ponteiro horas:
            tortuguita.pen(pencolor="black", fillcolor="green", pensize=3, pendown=True)
            tortuguita.setheading(90)
            tortuguita.right(lista_nova_angulos[0])
            tortuguita.forward(80)
            tortuguita.left(135)
            tortuguita.forward(10)
            tortuguita.back(10)
            tortuguita.left(90)
            tortuguita.forward(10)
            tortuguita.penup()
            tortuguita.home()
            lista_angulos_aux[0] = lista_nova_angulos[0]

    turtle.done()


if __name__ == "__main__":
    main()