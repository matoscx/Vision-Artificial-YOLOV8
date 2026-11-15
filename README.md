👁️ Detección de Objetos en Tiempo Real con YOLOv8 y OpenCV
Implementación eficiente de Deep Learning para la identificación y etiquetado preciso de objetos en entornos dinámicos.

Este repositorio contiene un script en Python diseñado para realizar detección de objetos en tiempo real utilizando la potencia del modelo YOLOv8 nano de Ultralytics en conjunto con OpenCV. El sistema procesa streams de video desde la cámara web, aplicando filtros de confianza y traducción dinámica de etiquetas para ofrecer una visualización fluida, limpia y en español.   
deteccion.py

🚀 Características Principales
Procesamiento Eficiente: Aprovecha el parámetro stream=True de YOLOv8 para optimizar el rendimiento y garantizar una tasa de cuadros por segundo (FPS) fluida durante la ejecución.   
deteccion.py

Filtro de Confianza Adaptativo: Configurado con un umbral estricto (conf > 0.55) para asegurar que solo se dibujen detecciones con alta certeza estadística.   
deteccion.py

Diccionario de Traducción Local: Traduce automáticamente las clases detectadas al español (Cell phone ➔ Celular, Bottle ➔ Botella, etc.) para mejorar la accesibilidad y presentación de los resultados.   
deteccion.py

Interfaz Visual Optimizada: Incorpora renderizado con rectángulos en color cian y fondos de contraste sólido en las etiquetas flotantes para facilitar la lectura sobre cualquier fondo de video.   
deteccion.py

💻 Stack Tecnológico
Lenguaje: Python 3.x

Librerías Principales:

ultralytics (Implementación y gestión del modelo YOLOv8)

cv2 (OpenCV para la captura de video, renderizado de marcos y manipulación de gráficos)

⚙️ Uso y Ejecución
Asegúrate de tener Python instalado junto con las dependencias necesarias:

Bash
pip install ultralytics opencv-python
Clona este repositorio y ejecuta el script principal:

Bash
python deteccion.py
Presiona la tecla q en cualquier momento para cerrar la ventana de la cámara y finalizar el programa.   
deteccion.py

Desarrollado como parte de la exploración aplicada en Visión Artificial y Modelos de Deep Learning. ✨
