import tkinter as tk

LINEAS_GANADORAS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


class Triqui:
    def __init__(self, ventana):
        self.ventana = ventana
        ventana.title("Triqui")
        ventana.resizable(False, False)

        self.estado = tk.Label(ventana, font=("Arial", 16))
        self.estado.grid(row=0, column=0, columnspan=3, pady=10)

        self.botones = []
        for i in range(9):
            boton = tk.Button(
                ventana, text="", width=5, height=2, font=("Arial", 32, "bold"),
                command=lambda i=i: self.jugar(i),
            )
            boton.grid(row=1 + i // 3, column=i % 3, padx=2, pady=2)
            self.botones.append(boton)

        tk.Button(ventana, text="Reiniciar", font=("Arial", 12),
                  command=self.reiniciar).grid(row=4, column=0, columnspan=3, pady=10)

        self.reiniciar()

    def reiniciar(self):
        self.tablero = [""] * 9
        self.turno = "X"
        self.terminado = False
        for boton in self.botones:
            boton.config(text="", state="normal", bg="SystemButtonFace")
        self.estado.config(text=f"Turno de {self.turno}")

    def jugar(self, i):
        if self.terminado or self.tablero[i]:
            return
        self.tablero[i] = self.turno
        self.botones[i].config(text=self.turno, state="disabled",
                               disabledforeground="blue" if self.turno == "X" else "red")

        linea = self.ganador()
        if linea:
            for j in linea:
                self.botones[j].config(bg="lightgreen")
            self.estado.config(text=f"¡Ganó {self.turno}!")
            self.terminar()
        elif all(self.tablero):
            self.estado.config(text="¡Empate!")
            self.terminar()
        else:
            self.turno = "O" if self.turno == "X" else "X"
            self.estado.config(text=f"Turno de {self.turno}")

    def ganador(self):
        for a, b, c in LINEAS_GANADORAS:
            if self.tablero[a] and self.tablero[a] == self.tablero[b] == self.tablero[c]:
                return (a, b, c)
        return None

    def terminar(self):
        self.terminado = True
        for boton in self.botones:
            boton.config(state="disabled")


if __name__ == "__main__":
    ventana = tk.Tk()
    Triqui(ventana)
    ventana.mainloop()
