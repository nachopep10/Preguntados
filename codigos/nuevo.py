import pygame
from funciones import *

pygame.init()

config_pantalla = [750, 550]
pantalla = pygame.display.set_mode(config_pantalla)

running = True
menu_inicio = True
jugando = False
top = False
nombre = False
final = False
nombre_usuario = ''
input_box = pygame.Rect(250, 275, 300, 50)
color_inactivo = pygame.Color(VIOLETA)
color_activo = pygame.Color(BLANCO)
color = color_inactivo
activo = False

color_boton_a = BLANCO
color_boton_b = BLANCO
color_boton_c = BLANCO

puntaje_actual = 0
pregunta_actual = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_inicio:
                if boton_jugar.collidepoint(event.pos):
                    menu_inicio = False
                    nombre = True
                elif boton_puntaje.collidepoint(event.pos):
                    menu_inicio = False
                    top = True
                elif boton_salir.collidepoint(event.pos):
                    running = False
                    guardar_puntajes(nombre_usuario, puntaje_actual)
                elif boton_volumen.collidepoint(event.pos):
                    cambiar_volumen()
            elif nombre:
                if input_box.collidepoint(event.pos):
                    activo = not activo
                else:
                    activo = False
                color = color_activo if activo else color_inactivo

            elif jugando:
                if boton_pregunta.collidepoint(event.pos):
                    pregunta_actual += 1
                    preguntas(pregunta_actual)
                elif boton_reiniciar.collidepoint(event.pos):
                    reiniciar()
                    puntaje_actual = 0
                    pregunta_actual = 0
                elif boton_respuesta_a.collidepoint(event.pos):
                    verificar_respuesta('a')
                elif boton_respuesta_b.collidepoint(event.pos):
                    verificar_respuesta('b')
                elif boton_respuesta_c.collidepoint(event.pos):
                    verificar_respuesta('c')
                if pregunta_actual >= len(lista):
                    guardar_puntajes(nombre_usuario)
                    jugando = False
                    final = True

            
            elif final:
                if boton_retroceder2.collidepoint(event.pos):
                    final = False
                    menu_inicio = True
                    reiniciar_completo()
                    menu_inicio = True
                    jugando = False
                    top = False
                    nombre = False
                    final = False
                    nombre_usuario = ''
                    activo = False
                    puntaje_actual = 0
                    pregunta_actual = 0
            elif top:
                if boton_retroceder.collidepoint(event.pos):
                    top = False
                    menu_inicio = True
                    
        if event.type == pygame.KEYDOWN and activo:
            if event.key == pygame.K_RETURN:
                nombre = False
                jugando = True
            elif event.key == pygame.K_BACKSPACE:
                nombre_usuario = nombre_usuario[:-1]
            else:
                nombre_usuario += event.unicode

    if menu_inicio:
        pantalla_inicio()
    elif jugando:
        preguntas(pregunta_actual)
    elif nombre:
        pantalla.fill(ROSA)
        txt_surface = fuente_juego.render(nombre_usuario, True, color)
        width = max(300, txt_surface.get_width() + 10)
        input_box.w = width
        pantalla.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(pantalla, color, input_box, 2)

        texto_titulo = fuente_juego.render("Ingrese su Nombre", True, NEGRO)
        pantalla.blit(texto_titulo, (260, 240))
    elif final:
        pantalla_final(nombre_usuario)
    elif top:
        puntaje()

    pygame.display.flip()

pygame.quit()



