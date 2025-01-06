# Clasificador de números enteros
## Equipo 3: 
* Becerra Lorenzo Saul Alejandro 
* Chargoy Olvera Rafael Eduardo
* Hernandez Hernandez Emanuel
* Moreno Ramirez José Jorge 

[Aquí](Source/main.pyw) podrás encontrar el programa con extensión `.pyw`.
[Aquí](Docs/README.md) podrás encontrar toda la documentación.

Este programa clasifica números enteros ingresados por el usuario en diferentes categorías (primos, compuestos, pares, impares, perfectos y deficientes) y grafica los resultados.

```python
from tkinter import *
from tkinter import filedialog
import csv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
```
Importamos las bibliotecas necesarias para la interfaz gráfica, manejo de archivos CSV y generación de gráficos.

Definimos las funciones que clasifican los números enteros en diferentes categorías.

```python
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
            if i != num // i:
                suma += num // i
    return suma == num

def deficiente(num):
    return num > suma_divisores(num)

def suma_divisores(num):
    suma = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            suma += i
            if i != num // i:
                suma += num // i
    return suma
```

Inicializamos las variables globales que contarán las ocurrencias de cada categoría.

```python
a = 0 #primo
b = 0 #compuesto
c = 0 #par
d = 0 #impar
e = 0 #perfecto
f = 0 #deficiente
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
    
    primo_var.set(primo(num))
    compuesto_var.set(compuesto(num))
    par_var.set(par(num))
    impar_var.set(impar(num))
    perfecto_var.set(perfecto(num))
    deficiente_var.set(deficiente(num))
    
    num_listbox.insert(END, num)
    
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
                num_listbox.insert(END, num)
    
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

Definimos la función `on_listbox_select` que se ejecuta cuando el usuario selecciona un número de la lista. Esta función coloca el número seleccionado en la entrada y lo evalúa nuevamente.

```python
def on_listbox_select(event):
    selected_num = num_listbox.get(num_listbox.curselection())
    entry.delete(0, END)
    entry.insert(0, selected_num)
    on_button_click()
```

Definimos la función `save_history` que permite al usuario guardar los números almacenados en el historial en un archivo CSV.

```python
def save_history():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        numbers = [num_listbox.get(i) for i in range(num_listbox.size())]
        writer.writerow(numbers)
```

### Descripción de las funciones

- `primo(num)`: Determina si un número es primo. Retorna 1 si es primo, de lo contrario retorna 0.
- `compuesto(num)`: Determina si un número es compuesto. Retorna 1 si es compuesto, de lo contrario retorna 0.
- `par(num)`: Determina si un número es par. Retorna 1 si es par, de lo contrario retorna 0.
- `impar(num)`: Determina si un número es impar. Retorna 1 si es impar, de lo contrario retorna 0.
- `perfecto(num)`: Determina si un número es perfecto. Retorna 1 si es perfecto, de lo contrario retorna 0.
- `deficiente(num)`: Determina si un número es deficiente. Retorna 1 si es deficiente, de lo contrario retorna 0.
