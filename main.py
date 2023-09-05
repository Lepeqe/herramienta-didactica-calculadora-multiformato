import tkinter as tk
from num2words import num2words
from PIL import Image, ImageTk
import webbrowser

# Función para convertir a imprenta mayúscula
def num2words_upper(number):
    return num2words(number, lang='es').upper()

def on_click(event):
    current_text = display.get()
    clicked_button = event.widget.cget("text")

    if clicked_button == "=":
        try:
            result = eval(current_text)
            if result_format.get() == "words":
                display.set(num2words_upper(result))
            else:
                display.set(result)
        except Exception as e:
            display.set("Error")
    elif clicked_button == "C":
        display.set("")
    else:
        display.set(current_text + clicked_button)

def toggle_result_format():
    if result_format.get() == "numbers":
        result_format.set("words")
    else:
        result_format.set("numbers")

# Crear la ventana principal
root = tk.Tk()
root.title("CALCULADORA MULTI-FORMATO")
root.configure(bg="gray")
root.resizable(False, False)

# Variable para almacenar el texto de la pantalla de la calculadora
display = tk.StringVar()
display.set("")

# Variable de control para alternar el formato del resultado (numbers o words)
result_format = tk.StringVar()
result_format.set("numbers")

# Crear el widget de la pantalla con fuente en imprenta mayúscula (Verdana)
screen = tk.Entry(root, textvar=display, font=("Verdana", 24), justify="right", bg="gray", fg="black", bd=3, state="readonly")
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Lista de botones con sus respectivos colores
buttons_data = [
    ("7", "#FF0000"), ("8", "#FF0000"), ("9", "#FF0000"), ("/", "#FF0000"),
    ("4", "#FF0000"), ("5", "#FF0000"), ("6", "#FF0000"), ("*", "#FF0000"),
    ("1", "#FF0000"), ("2", "#FF0000"), ("3", "#FF0000"), ("-", "#FF0000"),
    ("0", "#FF0000"), (".", "#FF0000"), ("C", "#FF0000"), ("+", "#FF0000"),
    ("=", "#FF0000")
]

# Crear los botones y colocarlos en la ventana con colores personalizados
for i, (button_text, button_color) in enumerate(buttons_data):
    button = tk.Button(root, text=button_text, font=("Verdana", 20), width=5, height=2, fg="white", bg=button_color)

    row = i // 4 + 1
    column = i % 4

    if button_text == "=":
        button.grid(row=row, column=column, padx=5, pady=5, columnspan=2, sticky="nsew")
    else:
        button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

    button.bind("<Button-1>", on_click)

# Configurar el peso de las filas y columnas para que los botones se expandan uniformemente
for i in range(5):  # 5 filas (0 a 4)
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  # 4 columnas (0 a 3)
    root.grid_columnconfigure(i, weight=1)

def mostrar_mensaje():
    enlace = "https://www.fds-esc.edu.ar/es/"
    webbrowser.open(enlace)

ruta_imagen = "fds_logo.png"
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((100, 100), Image.LANCZOS)
foto = ImageTk.PhotoImage(imagen)

boton_imagen = tk.Button(root, image=foto, bg="gray", bd=0, highlightthickness=0, command=mostrar_mensaje)
boton_imagen.grid(row=6, column=1, padx=5, pady=5, columnspan=2, sticky="nsew")

# Crear el botón para cambiar el formato del resultado
format_button = tk.Button(root, text="C.Formato", font=("Verdana", 20), width=12, height=2, fg="black", bg="yellow",
                          command=toggle_result_format, bd=0)

# Colocar el botón "C.Formato" en la ventana (en la fila 5, columna 2)
format_button.grid(row=5, column=2, padx=5, pady=5, columnspan=2, sticky="nsew")  # Alineación del botón "c.formato"

# Ejecutar la ventana
root.mainloop()
