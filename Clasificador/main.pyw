from tkinter import *
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
    num = int(user_input) 
    
    a += primo(num)
    b += compuesto(num)
    c += par(num)
    d += impar(num)
    e += perfecto(num)
    f += deficiente(num)
    
    result_text = (
        f"Es primo: {primo(num)}\n"
        f"Es compuesto: {compuesto(num)}\n"
        f"Es par: {par(num)}\n"
        f"Es impar: {impar(num)}\n"
        f"Es perfecto: {perfecto(num)}\n"
        f"Es deficiente: {deficiente(num)}"
    )
    result_label.config(text=result_text)
    
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

button = Button(raiz, text="Evaluar", command=on_button_click)
button.pack(pady=10)  # Align to the left with padding

result_label = Label(raiz, text="", justify=LEFT, bg="white")
result_label.pack(pady=10, padx=20, anchor='w')  # Align to the left with padding

raiz.mainloop()