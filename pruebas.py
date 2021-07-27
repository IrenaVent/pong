import pygame as pg #le ponemos un aleas

pg.init()

pantalla = pg.display.set_mode((800, 600))

game_over = False
while not game_over:

    eventos = pg.event.get() # línea fundamental para que no pete
    for evento in eventos:
        if evento.type == pg.QUIT: # sin "()"" es una constante
            game_over = True

    pantalla.fill((255, 0, 0))

    pg.display.flip() #hay que hacerlo SIEMPRE

pg.quit()