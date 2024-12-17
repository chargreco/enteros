from tkinter import *
from tkinter import filedialog
import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from identify import *

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

def on_button_click():
    global a, b, c, d, e, f 
    user_input = entry.get()
    
    if not user_input.isdigit():
        error_label.config(text="Error: Por favor ingrese un número entero válido.")
        return
    else:
        error_label.config(text="")
    
    num = int(user_input) 
    
    a += primo(num)
    b += compuesto(num)
    c += par(num)
    d += impar(num)
    e += perfecto(num)
    f += deficiente(num)
    
    result_text = (
        f"{'Es primo' if primo(num) else 'NO es primo'}\n"
        f"{'Es compuesto' if compuesto(num) else 'NO es compuesto'}\n"
        f"{'Es par' if par(num) else 'NO es par'}\n"
        f"{'Es impar' if impar(num) else 'NO es impar'}\n"
        f"{'Es perfecto' if perfecto(num) else 'NO es perfecto'}\n"
        f"{'Es deficiente' if deficiente(num) else 'NO es deficiente'}\n"
    )
    result_label.config(text=result_text)
    
    plot_graph(a, b, c, d, e, f)

def load_csv():
    global a, b, c, d, e, f
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for item in row:
                num = int(item)
                a += primo(num)
                b += compuesto(num)
                c += par(num)
                d += impar(num)
                e += perfecto(num)
                f += deficiente(num)
    
    plot_graph(a, b, c, d, e, f)

def plot_graph(a, b, c, d, e, f):
    
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(1, 1, 1)
    
    etiquetas = ["Primos", "Compuestos", "Pares", "Impares", "Perfectos", "Deficientes"]
    valores = [a, b, c, d, e, f]
    
    plot.bar(etiquetas, valores)
    
    global canvas
    if 'canvas' in globals():
        canvas.get_tk_widget().pack_forget()  # Remove the previous canvas
    canvas = FigureCanvasTkAgg(fig, master=raiz)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

raiz = Tk()
raiz.title("Clasificador de numeros enteros")
raiz.config(bg="white")
raiz.geometry("650x400")

entry = Entry(raiz)
entry.pack(pady=10) 

error_label = Label(raiz, text="", fg="red", bg="white")
error_label.pack(pady=5)

button_frame = Frame(raiz)
button_frame.pack(pady=10)

button = Button(button_frame, text="Evaluar", command=on_button_click)
button.pack(side=LEFT, padx=5)

load_button = Button(button_frame, text="Cargar CSV", command=load_csv)
load_button.pack(side=LEFT, padx=5)

result_label = Label(raiz, text="", justify=LEFT, bg="white")
result_label.pack(pady=10, padx=20, anchor='w')  # Align to the left with padding

raiz.mainloop()