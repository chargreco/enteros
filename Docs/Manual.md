# Manual de Usuario

1. **Descarga e instalación de Python:**
   Debemos descargar el programa de Python, [Python Release Python 3.13.0 | Python.org](https://www.python.org), es importante que no sea una versión de prueba o de acceso anticipado, ya que puede haber problemas al momento de instalar las librerías necesarias para compilar el programa.

2. **Instalación de la librería matplotlib:**
   Una vez descargado el programa, presionaremos las teclas de **Windows + R**, abriremos la **PowerShell** y pondremos el siguiente comando:
     
   ```bash
     pip install matplotlib
   ```

   Esta librería será la encargada de graficar los datos. Las demás librerías ya vienen por defecto en Python.
![Imagen de powershell](imagen/2.png)


3. **Descarga del código en GitHub:**
   Una vez instalado todo, nos dirigiremos al [archivo requerido](../Clasificador/main.pyw) (en caso de no tener descargado el código) y lo descargaremos en la opción de Descargar.
![GitHub](imagen/3.png)


4. **Compilación del código:**
   Una vez guardado, abriremos de nuevo la **PowerShell** y lo compilaremos con el siguiente comando:
     
   ```bash
     python clasificador.py
   ```
![PS](imagen/5.png)


1. **Interfaz del programa:**
   Una vez compilado, se abrirá una ventana donde habrá varias opciones, entre ellas:
     - Evaluar
     - Cargar CSV
     - Descargar historial
![Inicio](imagen/6.png)


6. **Evaluación de datos:**
   Si decidimos ocupar el botón **Evaluar**, tendremos que ingresar los datos en el cuadro de arriba, dato por dato. Al clasificar un número, se podrá ver las categorías que cumple.
![Evaluar](imagen/7.png)


8. **Carga de archivo CSV:**
   Si decidimos ocupar el botón **Cargar CSV**, primero debemos tener un archivo CSV de este tipo. Al seleccionar y abrirlo, se cargarán automáticamente los datos.

   > **Nota:** Recordar que el programa es para números enteros. Si el archivo CSV contiene datos que no pertenezcan a este conjunto, no será analizado y tu PowerShell mostrará un mensaje de error.

![Carpeta](imagen/8.png)
![Csv](imagen/9.png)
![excel](imagen/10.png)
![ps3](imagen/11.png)


9. **Selección de datos cargados:**
   Al ingresar los datos del CSV, estos se cargarán todos automáticamente. Se cuenta con la opción de seleccionar un dato ingresado para ver en qué conjunto o conjuntos entra.
![seleccion](imagen/12.png)


10. **Descarga de datos ingresados:**
   Una vez que el usuario haya terminado de ingresar los datos, este puede descargar todos los números que haya ingresado. Así, en caso de que el primer CSV contenga datos erróneos, el usuario podrá tener un nuevo archivo con solo números enteros.
![purga](imagen/13.png)