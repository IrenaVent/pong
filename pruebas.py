import pygame as pg #le ponemos un alias, para no escribir tanto

pg.init()

pantalla = pg.display.set_mode((800, 600)) # cogemos módulo display de pygame, devuelve una surface, un rectángulo // set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface

game_over = False

while not game_over:

    eventos = pg.event.get() # procesar los eventos, línea fundamental para que no pete, es como si limpiar la memoria por cada vuelta
    
    for evento in eventos:
        if evento.type == pg.QUIT: # sin "()" es una constante, es decir QUIT es una constatnte
            game_over = True

    pantalla.fill((255, 0, 0))

    pg.display.flip() #hay que hacerlo SIEMPRE, will update the contents of the entire display // updates the whole screen / último mandato del programa

pg.quit() # método (es una función) para finalizar el juego