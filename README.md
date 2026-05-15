# SCUBACATT
# Proyecto SCUBACAT

Este repositorio contiene el código fuente del proyecto **ScubaCat**, cuyo objetivo es el despliegue de un video/GIF animado a través de la identificación de gestos manuales mediante visión artificial.

## **NOTA IMPORTANTE SOBRE LA VERSIÓN DE PYTHON**

El proyecto **DEBE** ejecutarse utilizando **Python  3.10.x**, ya que existen incompatibilidades y excepciones en librerías críticas (como MediaPipe) cuando se utiliza una versión diferente (3.11+ o 3.9-). El branch `main` está validado únicamente para esta versión de Python.
 
## **REQUISITOS DEL SISTEMA**

- **Lenguaje:** Python 3.10 (Obligatorio)
- **Librerías:** OpenCV, MediaPipe, NumPy
- **Hardware:** Cámara web y archivo de video `gato.mp4` en el directorio raíz.

## **INSTALACIÓN Y CONFIGURACIÓN (BASH)**

Sigue estos pasos para preparar tu entorno de ejecución:

### 1. Clonar el repositorio

Si aún no has clonado el repositorio, puedes hacerlo con el siguiente comando:

```bash
git clone https://github.com/mishu006/Scubacat.git
cd Scubacat
```

### 2. Crear y activar entorno virtual

Es altamente recomendable usar un entorno virtual para evitar conflictos con otras librerías de Python:

```bash
python -m venv .venv
# En Windows:
.venv\Scripts\activate
# En macOS/Linux:
source .venv/bin/activate
```

### 3. Instalar las dependencias

Asegúrate de tener `pip` actualizado y luego instala las librerías necesarias:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## **EJECUCIÓN DEL PROYECTO**

Con el entorno configurado y las dependencias instaladas, ya puedes ejecutar el proyecto.

### 1. Asegúrate de tener conectada tu cámara web y que el archivo de video `gato.mp4` esté en la misma carpeta que el script.

### 2. Ejecuta el script principal

```bash
python scubacat.py
```

Esto iniciará el sistema de detección, y debería comenzar a detectar gestos manuales para controlar la reproducción del video.

## **Verificación de archivo de video**

Asegúrate de que el archivo de video llamado **`gato.mp4`** esté presente en el mismo directorio que el script **`scubacat.py`**. Si el archivo no está, el video no podrá cargarse.

## **LÓGICA DE CONTROL GESTUAL**

El sistema monitorea 21 puntos clave de la mano para ejecutar las siguientes acciones:

* **GESTO DE PUÑO:** Al detectar la contracción de los dedos hacia la base de la palma, se inicia la reproducción automática del video.
* **GESTO DE PALMA:** Al extender los dedos, el sistema detiene la captura y cierra la ventana del video.
* **TECLA ESC:** Finaliza la captura de la cámara principal y cierra el programa.

## **GUÍA DE SOLUCIÓN DE PROBLEMAS**

Si encuentras problemas durante la ejecución, aquí hay algunas soluciones comunes:

### **ERROR DE RUTA (FileNotFound)**

Asegúrate de que el archivo de video se llame exactamente `gato.mp4` y esté ubicado en la misma carpeta que el archivo `.py`.

### **LA CÁMARA NO ENCIENDE**

Verifica que ninguna otra aplicación (como Teams, Zoom, Discord, etc.) esté utilizando la cámara web en segundo plano.

### **ERROR DE ATRIBUTO (AttributeError)**

Si ves un error relacionado con `mediapipe.solutions`, asegúrate de que no haya un archivo llamado `mediapipe.py` en tu carpeta local, ya que esto puede interferir con el importador de Python.

### **ERROR DE COMANDO 'PIP'**

Si tu terminal no reconoce el comando `pip`, asegúrate de estar utilizando el entorno virtual correcto. Si no es reconocido, intenta usar el siguiente comando:

```bash
python -m pip install --upgrade pip
```

### **El video no se reproduce**

* Verifica que el archivo `gato.mp4` esté en el directorio correcto y que no haya errores de ruta.
* Además, asegúrate de que el formato del video sea compatible con OpenCV.

### **Problemas con la detección de gestos**

* Asegúrate de que la cámara tenga buena iluminación.
* Ajusta la posición de las manos frente a la cámara para asegurarte de que sean visibles.
* Si el gesto de "puño" no inicia el video, asegúrate de que los puntos de los dedos estén lo suficientemente cerca de la base de la palma.

## **Instalación de dependencias**

Para instalar todas las dependencias necesarias, puedes usar el archivo `requirements.txt` con el siguiente comando:

```bash
pip install -r requirements.txt
```
