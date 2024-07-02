import pygame
from datos import lista
from colores import *
from funciones import *



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