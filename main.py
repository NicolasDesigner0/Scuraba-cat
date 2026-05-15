import math
import cv2
import mediapipe as mp

# Configuración de MediaPipe para la detección de manos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.8,  # confianza mínima para detectar
    min_tracking_confidence=0.8,  # confianza mínima para rastrear
)
mp_draw = mp.solutions.drawing_utils

# Ruta del video y configuración de la cámara
video_path = "gato.mp4"  # Video del gato
cap_cat = None
cap = cv2.VideoCapture(0)  # abrir la camara web
video_encendido = False


# Función para verificar si dos puntos están cerca en el espacio de la mano
def puntos_cerca(p1, p2, umbral=0.1):
    distancia = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    return distancia < umbral


# Verificar si la mano está en un puño cerrado
def verificar_puno(lm):
    puntas = [8, 12, 16, 20]  # puntas de los dedos
    base_palma = lm[0]  # muñeca
    cerrados = [puntos_cerca(lm[p], base_palma, 0.25) for p in puntas]
    return all(cerrados)


# Verificar si la palma está completamente abierta
def verificar_palma_abierta(lm):
    # puntas y bases de los dedos
    puntas_bases = [(8, 6), (12, 10), (16, 14), (20, 18)]
    return all([lm[p].y < lm[b].y for p, b in puntas_bases])

#Bucle principal para la deteccion de gestos y control del video
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)  # Voltear la imagen para efecto espejo
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = hands.process(frame_rgb) #procesar la imagen con MediaPipe
    
    hay_puño = False
    hay_palma = False
    
    #si se detectan manos,procesar los gestos
    if resultados.multi_hand_landmarks:
        for hand_landmarks in resultados.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm = hand_landmarks.landmark
            
            #verificar si es puño o una palma abierta
            if verificar_puno(lm):
                hay_puño = True
            elif verificar_palma_abierta(lm):
                hay_palma = True
    
    #controlar el video: abrir cuando hace puño, cerrar cuando no (pero cámara siempre abierta)
    if hay_puño and not video_encendido:
        cap_cat = cv2.VideoCapture(video_path) #abrir el video
        if cap_cat.isOpened():
            video_encendido = True
            print("Puño detectado! gato ON.")
    
    elif not hay_puño and video_encendido:
        video_encendido = False #cerrar solo el video
        if cap_cat: 
            cap_cat.release()
            cap_cat = None
        cv2.destroyWindow("Scubacat") #cerrar la ventana del video
        print("Gesto terminado. Gato OFF.")
    
    #mostrar el video si esta encendido
    if video_encendido and cap_cat and cap_cat.isOpened():
        ret_v, frame_cat = cap_cat.read()
        if not ret_v:
            cap_cat.set(cv2.CAP_PROP_POS_FRAMES, 0) #reiniciar el video
            ret_v, frame_cat = cap_cat.read()
        
        if ret_v:
            frame_cat = cv2.resize(frame_cat, (400, 400)) #redimensionar el video
            cv2.imshow("Scubacat", frame_cat) #mostrar el video
    
    #mostrar la cámara siempre abierta
    cv2.imshow("Camara principal", frame)
    
    #salir del bucle con la tecla 'esc'
    if cv2.waitKey(1) & 0xFF == 27:
        break
 
#liberar recursos al salir
cap.release()
if cap_cat: cap_cat.release()
cv2.destroyAllWindows()