from tkinter import *
from tkinter import filedialog
import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def compuesto(num):
    return not primo(num)

def par(num):
    return num % 2 == 0

def impar(num):
    return not par(num)

def perfecto(num):
    suma = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            suma += i
            if i!= num // i:
                suma += num // i
    return suma == num

def deficiente(num):
    return num > suma_divisores(num)

def suma_divisores(num):
    suma = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            suma += i
            if i!= num // i:
                suma += num // i
    return suma

a = 0 #primo
b = 0 #compuesto
c = 0 #par
d = 0 #impar
e = 0 #perfecto
f = 0 #deficiente

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
    
    primo_var.set(primo(num))
    compuesto_var.set(compuesto(num))
    par_var.set(par(num))
    impar_var.set(impar(num))
    perfecto_var.set(perfecto(num))
    deficiente_var.set(deficiente(num))
    
    num_listbox.insert(END, num)
    
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
                num_listbox.insert(END, num)
    
    plot_graph(a, b, c, d, e, f)

def plot_graph(a, b, c, d, e, f):
    
    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot(1, 1, 1)
    
    etiquetas = ["Primos", "Compuestos", "Pares", "Impares", "Perfectos", "Deficientes"]
    valores = [a, b, c, d, e, f]
    
    plot.bar(etiquetas, valores)
    
    global canvas
    if 'canvas' in globals():
        canvas.get_tk_widget().pack_forget()  
    canvas = FigureCanvasTkAgg(fig, master=raiz)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

def on_listbox_select(event):
    selected_num = num_listbox.get(num_listbox.curselection())
    entry.delete(0, END)
    entry.insert(0, selected_num)
    on_button_click()

def save_history():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        numbers = [num_listbox.get(i) for i in range(num_listbox.size())]
        writer.writerow(numbers)

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

save_button = Button(button_frame, text="Descargar historial", command=save_history)
save_button.pack(side=LEFT, padx=5)

result_frame = Frame(raiz, bg="white")
result_frame.pack(pady=10, padx=20, anchor='w', side=LEFT)

primo_var = BooleanVar()
compuesto_var = BooleanVar()
par_var = BooleanVar()
impar_var = BooleanVar()
perfecto_var = BooleanVar()
deficiente_var = BooleanVar()

Label(result_frame, text="Es primo:", bg="white").grid(row=0, column=0, sticky='w')
Checkbutton(result_frame, variable=primo_var, state=DISABLED, bg="white").grid(row=0, column=1, sticky='w')

Label(result_frame, text="Es compuesto:", bg="white").grid(row=1, column=0, sticky='w')
Checkbutton(result_frame, variable=compuesto_var, state=DISABLED, bg="white").grid(row=1, column=1, sticky='w')

Label(result_frame, text="Es par:", bg="white").grid(row=2, column=0, sticky='w')
Checkbutton(result_frame, variable=par_var, state=DISABLED, bg="white").grid(row=2, column=1, sticky='w')

Label(result_frame, text="Es impar:", bg="white").grid(row=3, column=0, sticky='w')
Checkbutton(result_frame, variable=impar_var, state=DISABLED, bg="white").grid(row=3, column=1, sticky='w')

Label(result_frame, text="Es perfecto:", bg="white").grid(row=4, column=0, sticky='w')
Checkbutton(result_frame, variable=perfecto_var, state=DISABLED, bg="white").grid(row=4, column=1, sticky='w')

Label(result_frame, text="Es deficiente:", bg="white").grid(row=5, column=0, sticky='w')
Checkbutton(result_frame, variable=deficiente_var, state=DISABLED, bg="white").grid(row=5, column=1, sticky='w')

list_frame = Frame(result_frame, bg="white")
list_frame.grid(row=0, column=2, rowspan=6, padx=10, sticky='ns')

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

num_listbox = Listbox(list_frame, yscrollcommand=scrollbar.set)
num_listbox.pack(side=LEFT, fill=Y)
num_listbox.bind('<<ListboxSelect>>', on_listbox_select)

scrollbar.config(command=num_listbox.yview)

raiz.mainloop()