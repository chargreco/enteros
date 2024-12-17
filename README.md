# Clasificador de números enteros
## Equipo 3: 
* Becerra Lorenzo Saul Alejandro 
* Chargoy Olvera Rafael Eduardo
* Hernandez Hernandez Emanuel
* Moreno Ramirez José Jorge 

Este programa clasifica números enteros ingresados por el usuario en diferentes categorías (primos, compuestos, pares, impares, perfectos y deficientes) y grafica los resultados.

```python
from tkinter import *
from tkinter import filedialog
import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from identify import *
```
Importamos las bibliotecas necesarias para la interfaz gráfica, manejo de archivos CSV y generación de gráficos.

Inicializamos las variables globales que contarán las ocurrencias de cada categoría.

```python
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
```

Definimos la función `on_button_click` que se ejecutará cuando el usuario haga clic en el botón. Esta función toma el número ingresado por el usuario, lo clasifica y actualiza las variables globales y la etiqueta de resultados. También maneja errores de entrada.

```python
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
```

Definimos la función `load_csv` que permite al usuario cargar un archivo CSV con números enteros. Esta función procesa cada número en el archivo y actualiza las variables globales y la gráfica.

```python
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
```

Definimos la función `plot_graph` que crea y muestra una gráfica de barras con los resultados acumulados.

```python
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
```

Configuramos la ventana principal de Tkinter y agregamos los widgets necesarios (entrada de texto, botón, etiqueta de error y etiqueta de resultados).

```python
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
result_label.pack(pady=10, padx=20, anchor='w')  

raiz.mainloop()
```

## Código de identify.py

El archivo `identify.py` contiene las funciones que clasifican los números enteros en diferentes categorías. A continuación se muestra el código y la descripción de cada función.

```python
def primo(num):
    if num < 2:
        return 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    return 1

def compuesto(num):
    if num < 2:
        return 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 1
    return 0

def par(num):
    return 1 if num % 2 == 0 else 0

def impar(num):
    return 1 if num % 2 != 0 else 0

def perfecto(num):
    if num < 2:
        return 0
    suma = sum(i for i in range(1, num) if num % i == 0)
    return 1 if suma == num else 0

def deficiente(num):
    if num < 2:
        return 0
    suma = sum(i for i in range(1, num) if num % i == 0)
    return 1 if suma < num else 0
```

### Descripción de las funciones

- `primo(num)`: Determina si un número es primo. Retorna 1 si es primo, de lo contrario retorna 0.
- `compuesto(num)`: Determina si un número es compuesto. Retorna 1 si es compuesto, de lo contrario retorna 0.
- `par(num)`: Determina si un número es par. Retorna 1 si es par, de lo contrario retorna 0.
- `impar(num)`: Determina si un número es impar. Retorna 1 si es impar, de lo contrario retorna 0.
- `perfecto(num)`: Determina si un número es perfecto. Retorna 1 si es perfecto, de lo contrario retorna 0.
- `deficiente(num)`: Determina si un número es deficiente. Retorna 1 si es deficiente, de lo contrario retorna 0.
