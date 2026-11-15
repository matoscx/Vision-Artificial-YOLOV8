import cv2
from ultralytics import YOLO

# 1. Cargamos el modelo preentrenado (YOLOv8 nano)
model = YOLO("yolov8n.pt") 

# Diccionario para traducir los objetos comunes 
traducciones = {
    "cell phone": "Celular",
    "pencil": "Lapiz",
    "cup": "Taza",
    "bottle": "Botella",
    "keyboard": "Teclado",
    "mouse": "Mouse",
    "book": "Libro",
    "scissors": "Tijeras"
}

# 2. Inicializamos la cámara web
cap = cv2.VideoCapture(0)

print("Presiona 'q' para salir...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No se pudo acceder a la cámara.")
        break

    # 3. Pasar el frame por el modelo (stream=True para mayor fluidez)
    results = model(frame, stream=True)

    # 4. Procesar las detecciones
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Obtener las coordenadas de la caja de detección
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            # Obtener el nombre del objeto y su nivel de confianza
            cls = int(box.cls[0])
            label_en = model.names[cls]
            conf = float(box.conf[0])

            # Filtro: Solo mostrar si el modelo está más del 55% seguro
            if conf > 0.55:
                # Traducir al español si está en el diccionario; si no, dejar el original
                label_es = traducciones.get(label_en, label_en.capitalize())
                
                # Crear el texto: "Objeto - 85%"
                text = f"{label_es} {conf*100:.0f}%"

                # Dibujar rectángulo llamativo (Color cyan: (255, 255, 0) en BGR)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
                
                # Dibujar fondo para el texto (mejora la legibilidad en el video)
                (w, h), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
                cv2.rectangle(frame, (x1, y1 - 25), (x1 + w, y1), (255, 255, 0), -1)
                
                # Escribir el texto encima del rectángulo (en color negro para contraste)
                cv2.putText(frame, text, (x1, y1 - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    # 5. Mostrar la ventana con el resultado
    cv2.imshow("Deteccion en Tiempo Real", frame)

    # Romper el bucle si presionas la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Limpieza al cerrar
cap.release()
cv2.destroyAllWindows()