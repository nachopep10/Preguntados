import pygame
from datos import lista
from colores import *
import json

pygame.init()

#configuracion de la pantalla 
config_pantalla = [750, 550]
pantalla = pygame.display.set_mode(config_pantalla)


#fondo para el menu principal
imagen_fondo = pygame.image.load("C:/Users/ignac/OneDrive/Escritorio/visual/juego/imagenes/fondo3.png")
imagen_fondo2 = pygame.image.load("C:/Users/ignac/OneDrive/Escritorio/visual/juego/imagenes/fondo1.png")
imagen_fondo3 = pygame.image.load("C:/Users/ignac/OneDrive/Escritorio/visual/juego/imagenes/fondo7.png")

#titulo del juego
pygame.display.set_caption("Preguntados")


#icono del juego
icono = pygame.image.load("C:/Users/ignac/OneDrive/Escritorio/visual/juego/imagenes/icono1.png")
pygame.display.set_icon(icono)

#musica de fondo
pygame.mixer.music.load("C:/Users/ignac/OneDrive/Escritorio/visual/juego/imagenes/musicamenu.mp3")
pygame.mixer.music.play(-1) #-1 para que sea infinito

#icono para el nivel del volumen
mute = pygame.image.load("C:/Users/ignac/OneDrive/Escritorio/visual/juego/imagenes/mute.png")
bajo = pygame.image.load("C:/Users/ignac/OneDrive/Escritorio/visual/juego/imagenes/bajo.png")
intermedio = pygame.image.load("C:/Users/ignac/OneDrive/Escritorio/visual/juego/imagenes/intermedio.png")
alto = pygame.image.load("C:/Users/ignac/OneDrive/Escritorio/visual/juego/imagenes/alto.png")


#sonido de correcto y incorrecto
sonido_correcto = pygame.mixer.Sound("C:/Users/ignac/OneDrive/Escritorio/visual/juego/imagenes/correcto.mp3")
sonido_incorrecto = pygame.mixer.Sound("C:/Users/ignac/OneDrive/Escritorio/visual/juego/imagenes/incorrecto.mp3")

#fuente 
font = pygame.font.SysFont("Arial", 40)
fuente_juego = pygame.font.SysFont("Arial", 25)
fuente_pregunta = pygame.font.SysFont("Arial", 20)
fuente_intentos = pygame.font.SysFont("Arial", 25)


#botones de la pantalla de inicio
boton_jugar = pygame.Rect(10, 50, 200, 45)
boton_puntaje = pygame.Rect(10, 114, 200, 45)
boton_salir = pygame.Rect(10, 180, 200, 45)

texto_jugar = font.render("Jugar", True, NEGRO)
texto_puntaje = font.render("Top", True, NEGRO)
texto_salir = font.render("Salir", True, NEGRO)


#botones de la pantalla de juego 
boton_pregunta = pygame.Rect(390, 470, 200, 60)
boton_reiniciar = pygame.Rect(160, 470, 200, 60)
boton_mostrar_score = pygame.Rect(10, 180, 200, 60)

texto_boton_pregunta = font.render("Pregunta", True, NEGRO)
texto_reiniciar = font.render("Reiniciar", True, NEGRO)


#boton para retroceder 
boton_retroceder = pygame.Rect(640, 10, 100, 60)
texto_retroceder = font.render("Atras", True, NEGRO)

boton_retroceder2 = pygame.Rect(170, 400, 400, 60)
texto_retroceder2 = font.render("Voles al menu principal", True, NEGRO)

#botones para las respuestas
boton_respuesta_a = pygame.Rect(230, 200, 300, 50)
boton_respuesta_b = pygame.Rect(230, 275, 300, 50)
boton_respuesta_c = pygame.Rect(230, 350, 300, 50)

#rectangulo para la pregunta 
rectangulo_pregunta = pygame.Rect(130, 60, 490, 90)

#rectangulo  para el score
rectangulo_score = pygame.Rect(10, 200, 200, 60)
rectangulo_intentos = pygame.Rect(10, 270, 200, 60)

#boton para ingresar el nobre y preguntar el nombre 
pregunta_nombre = pygame.Rect(180, 100, 400, 60)
boton_nombre = pygame.Rect (230, 200, 300, 50)
boton_aceptar = pygame.Rect (280, 400, 200, 55)

texto_nombre = font.render("Ingrese su nombre", True, NEGRO)
texto_aceptar = font.render("Aceptar", True, NEGRO)


#pantalla final 
final_rect = pygame.Rect(170, 40, 400, 60)
fianl_score = pygame.Rect(40, 150, 300, 60)
final_nombre = pygame.Rect(40, 250, 300, 60)


#variables globales
pregunta_actual = 0
puntaje_actual = 0
intentos_restantes = 2



def pantalla_inicio():
    """
    Configura la pantalla de inicio del juego y realiza las siguintes acciones:
    - Pone una imagen como fondo.
    - Pone el titulo y lo ubica.
    - Dibuja los botones de "Jugar", "Ver Puntajes" y "Salir" en la pantalla.
    - Pone el texto en donde corresponde.
    """
    pantalla.fill(FONDO)
    pantalla.blit(imagen_fondo, (0, 0))

    titulo = font.render("Preguntados", True, NEGRO)
    pantalla.blit(titulo, (270, 20))
    
    pygame.draw.rect(pantalla, BLANCO, boton_jugar)
    pygame.draw.rect(pantalla, BLANCO, boton_puntaje)
    pygame.draw.rect(pantalla, BLANCO, boton_salir)
    
    pantalla.blit(texto_jugar, (boton_jugar.x + 20, boton_jugar.y - 4))
    pantalla.blit(texto_puntaje, (boton_puntaje.x + 30, boton_puntaje.y - 4))
    pantalla.blit(texto_salir, (boton_salir.x + 25, boton_salir.y - 4))


def preguntas():
    global pregunta_actual, puntaje_actual, intentos_restantes
    """
    Configura y muestra la pantalla de preguntas del juego Preguntados.
    Esta función realiza las siguientes acciones:
    - Usa variables globales para mantener el estado del juego a través de diferentes funciones.
    - Pone una imagen como fondo.
    - Muestra la pregunta actual y sus posibles respuestas.
    - Dibuja los rectángulos para las preguntas, respuestas y retroceder.
    - Pone el texto en donde corresponde.
    - Muestra el puntaje actual y los intentos restantes.
    -
    """
    pantalla.fill(FONDO)
    pantalla.blit(imagen_fondo2, (0, 0))

    if pregunta_actual < len(lista):
        pregunta = lista[pregunta_actual]
        texto_preguntas = fuente_pregunta.render(pregunta['pregunta'], True, NEGRO)

        texto_respuesta_1 = fuente_juego.render(f"A-{pregunta['a']}", True, NEGRO)
        texto_respuesta_2 = fuente_juego.render(f"b-{pregunta['b']}", True, NEGRO)
        texto_respuesta_3 = fuente_juego.render(f"c-{pregunta['c']}", True, NEGRO)

        pygame.draw.rect(pantalla, BLANCO, rectangulo_pregunta)
        pygame.draw.rect(pantalla, BLANCO, boton_pregunta)
        pygame.draw.rect(pantalla, BLANCO, boton_reiniciar)
        pygame.draw.rect(pantalla, BLANCO, boton_respuesta_a)
        pygame.draw.rect(pantalla, BLANCO, boton_respuesta_b)
        pygame.draw.rect(pantalla, BLANCO, boton_respuesta_c)
        pygame.draw.rect(pantalla, BLANCO, boton_retroceder) 
        pygame.draw.rect(pantalla, CELESTE, rectangulo_score)
        pygame.draw.rect(pantalla, CELESTE, rectangulo_intentos)
    
        pantalla.blit(texto_preguntas, (rectangulo_pregunta.x +5, rectangulo_pregunta.y +25))
        pantalla.blit(texto_boton_pregunta, (boton_pregunta.x + 20, boton_pregunta.y + 10))
        pantalla.blit(texto_reiniciar, (boton_reiniciar.x + 40, boton_reiniciar.y + 10))
        pantalla.blit(texto_respuesta_1, (boton_respuesta_a.x + 10, boton_respuesta_a.y + 6))
        pantalla.blit(texto_respuesta_2, (boton_respuesta_b.x + 10, boton_respuesta_b.y + 6))
        pantalla.blit(texto_respuesta_3, (boton_respuesta_c.x + 10, boton_respuesta_c.y + 6))
        pantalla.blit(texto_retroceder, (boton_retroceder.x + 10, boton_retroceder.y + 10))

    texto_puntaje = font.render(f"Puntaje: {puntaje_actual}", True, NEGRO)
    pantalla.blit(texto_puntaje, (rectangulo_score.x + 10, rectangulo_score.y + 10))
    texto_intentos = fuente_intentos.render(f"Intentos restantes: {intentos_restantes}", True, NEGRO)
    pantalla.blit(texto_intentos, (rectangulo_intentos.x + 10, rectangulo_intentos.y + 10))


def verificar_respuesta(opcion):
    global pregunta_actual, puntaje_actual, intentos_restantes
    """
    Verifica si la opción seleccionada por el jugador es correcta y actualiza el estado del juego.
    Esta función realiza las siguientes acciones:
    - Usa variables globales para mantener el estado del juego a través de diferentes funciones.
    - Verifica si la respuesta seleccionada es correcta.
    - Actualiza el puntaje y el número de intentos restantes según la respuesta del jugador.
    - Reproduce un sonido dependiendo si la respuesta es correcta o incorrecta.
    - Llama a la función preguntas() para actualizar la pantalla de preguntas.   
    """
    pregunta = lista[pregunta_actual]
    respuesta_correcta = pregunta['correcta']
    if opcion == respuesta_correcta:
        puntaje_actual += 10
        sonido_correcto.play()
        pregunta_actual += 1
        intentos_restantes = 2
    else:
        intentos_restantes -= 1
        sonido_incorrecto.play()
        if intentos_restantes == 0:
            pregunta_actual += 1
            intentos_restantes = 2
            puntaje_actual -= 10
            
        else:
            puntaje_actual -= 10
    preguntas()


def pantalla_final():
    """
    Configura la pantalla final del juego.

    Esta función realiza las siguientes acciones:
    - Ponel un color de fondo determinado.
    - Dibuja rectángulos para el mensaje final, el puntaje final, el nombre del jugador y un botón para retroceder.
    - Muestra el texto final del juego, el nombre del jugador y el puntaje que obtuvo.
    """
    pantalla.fill(ROSA)

    pygame.draw.rect(pantalla, BLANCO, final_rect)
    pygame.draw.rect(pantalla,BLANCO, fianl_score)
    pygame.draw.rect(pantalla,BLANCO, final_nombre)
    pygame.draw.rect(pantalla, BLANCO, boton_retroceder2) 


    texto_final = font.render(f"Fin del juego", True, NEGRO)
    texto_nombre = font.render(f"Jugador: {nombre_usuario}", True, NEGRO)
    texto_puntaje = font.render(f"Tu puntaje es: {puntaje_actual}", True, NEGRO)

    pantalla.blit(texto_final, (final_rect.x + 100, final_rect.y + 10))
    pantalla.blit(texto_nombre, (final_nombre.x + 20, final_nombre.y + 10))
    pantalla.blit(texto_puntaje, (fianl_score.x + 20, fianl_score.y + 7))
    pantalla.blit(texto_retroceder2, (boton_retroceder2.x + 10, boton_retroceder2.y + 10))


nombre_usuario = ""
ingreso_usuario = False
def ingreso_nombre():
    """
    Configura la pantalla en la cual el jugador ingresa su nombre.

    Esta función realiza las siguientes acciones:
    - Ponel un color de fondo determinado.
    - Dibuja rectángulos para el botón de aceptar, la pregunta del nombre y otro para el ingreso del nombre.
    - Muestra el texto del botón de aceptar y la pregunta del nombre.
    - Muestra el nombre ingresado por el usuario.
    """
    pantalla.fill(GRIS)
    pygame.draw.rect(pantalla, BLANCO, boton_aceptar)
    pygame.draw.rect(pantalla, BLANCO, pregunta_nombre)
    pygame.draw.rect(pantalla, BLANCO, boton_nombre)
    
    pantalla.blit(texto_aceptar, (boton_aceptar.x +40, boton_aceptar.y + 5))
    pantalla.blit(texto_nombre, (pregunta_nombre.x +60, pregunta_nombre.y +5 ))
    
    texto_ingresado = fuente_juego.render(nombre_usuario, True, NEGRO)
    pantalla.blit(texto_ingresado, (boton_nombre.x + 10, boton_nombre.y + 10))


def reiniciar():
    global pregunta_actual, puntaje_actual, intentos_restantes, botones_habilitados, color_respuesta_a, color_respuesta_b, color_respuesta_c
    """
    Reinicia el juego a los valores iniciales.
    Esta función realiza las siguientes acciones:
    - Usa variables globales para modificar el estado del juego a través de diferentes funciones.
    - Restablece los contadores a los valores originales.
    """
    pregunta_actual = 0
    puntaje_actual = 0
    intentos_restantes = 2
    botones_habilitados = True



def guardar_puntajes(nombre, puntaje):
    """
    Guarda el nuevo puntaje en un archivo json.
    Esta función realiza las siguientes acciones:
    - Intenta cargar los puntajes existentes desde un archivo json.
    - Si el json no existe, inicializa una lista vacía.
    - Añade el nombre y el puntaje a la lista.
    - Ordena la lista de puntajes de mayor a menor según el puntaje.
    - Guarda la lista ordenada de puntajes de nuevo en el archivo json.
    """
    try:
        with open("C:/Users/ignac/OneDrive/Escritorio/visual/puntajes.json", "r") as archivo:
            puntajes = json.load(archivo)
    except FileNotFoundError:
        puntajes = []

    puntajes.append({"nombre": nombre, "puntaje": puntaje})
    puntajes = sorted(puntajes, key=lambda x: x["puntaje"], reverse=True)

    with open("puntajes.json", "w") as archivo:
        json.dump(puntajes, archivo,indent=4)



def puntaje():
    """
    Muestra los puntajes más altos guardados en un JSON.
    Esta función realiza las siguientes acciones:
    - Pone una imagen como fondo.
    - Dibuja un botón de retroceso en la pantalla.
    - Muestra los tres puntajes más altos y los nombres de los jugadores con estos puntajes.
    Los puntajes se cargan desde un archivo JSON ubicado en la ruta especificada.
    """
    pantalla.fill(FONDO)
    pantalla.blit(imagen_fondo3, (0, 0))
    
    pygame.draw.rect(pantalla, BLANCO, boton_retroceder) 
    pantalla.blit(texto_retroceder, (boton_retroceder.x + 10, boton_retroceder.y + 10))

    with open("C:/Users/ignac/OneDrive/Escritorio/visual/puntajes.json", "r") as archivo:
        puntajes = json.load(archivo)
        
        texto_top = font.render("Top 3 Puntajes:", True, ROJO)
        pantalla.blit(texto_top, (260, 40))
        
        top_puntajes = sorted(puntajes, key=lambda x: x["puntaje"], reverse=True)[:3]
        
        posiciones = [(300, 280), (190, 310), (470, 325)]
        
        for i, item in enumerate(top_puntajes):
            texto_nombre_puntaje = fuente_juego.render(f"{i+1}. {item['nombre']}: {item['puntaje']}", True, NEGRO)
            x, y = posiciones[i]  
            pantalla.blit(texto_nombre_puntaje, (x, y))

    pygame.draw.rect(pantalla, BLANCO, boton_retroceder) 
    pantalla.blit(texto_retroceder, (boton_retroceder.x + 10, boton_retroceder.y + 10))


running = True
menu_inicio = True
nombres = False
jugando = False
top = False

final = False
ingreso_usuario = False
nombre_usuario = ""

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_inicio:
                if boton_jugar.collidepoint(event.pos): 
                    menu_inicio = False
                    nombres = True
                elif boton_puntaje.collidepoint(event.pos):
                    menu_inicio = False
                    top = True
                elif boton_salir.collidepoint(event.pos):
                    running = False

            elif nombres:
                if boton_aceptar.collidepoint(event.pos) and nombre_usuario:
                    nombres = False
                    jugando = True

            elif jugando:
                if boton_pregunta.collidepoint(event.pos):
                    preguntas()
                    pregunta_actual += 1
                elif boton_reiniciar.collidepoint(event.pos):
                    reiniciar()
                elif boton_respuesta_a.collidepoint(event.pos):
                    verificar_respuesta('a')
                elif boton_respuesta_b.collidepoint(event.pos):
                    verificar_respuesta('b')
                elif boton_respuesta_c.collidepoint(event.pos):
                    verificar_respuesta('c')
                elif boton_retroceder.collidepoint(event.pos):
                    jugando = False
                    menu_inicio = True 
                if pregunta_actual >= len(lista):
                    jugando = False
                    final = True
                    guardar_puntajes(nombre_usuario, puntaje_actual)

            elif final:
                if boton_retroceder2.collidepoint(event.pos):
                    final = False
                    menu_inicio = True
                    reiniciar()

            elif top:
                if boton_retroceder.collidepoint(event.pos):
                    top = False
                    menu_inicio = True

        if nombres and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                ingreso_usuario = True
            elif event.key == pygame.K_BACKSPACE:
                nombre_usuario = nombre_usuario[:-1]
            else:
                nombre_usuario += event.unicode

    if menu_inicio:
        pantalla_inicio()
    elif nombres:
        ingreso_nombre()
    elif jugando:
        preguntas()
    elif final:
        pantalla_final()
    elif top:
        puntaje()
    
    pygame.display.flip() 

pygame.quit()  