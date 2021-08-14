import pygame as pg

SIZE = (800,600) # we decided no parmetric screen

class Bola():
    def __init__(self, x, y, w, h, color=(255,255,255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        
        self.derecha = True
        self.arriba = True

        # self.incremento_x = 5
        # self.incremento_y = 5

    def actualizate(self):

        # movement X (left - right)
        if self.derecha:
            self.x += 5
        else:
            self.x -= 5

        if self.x + self.w >= SIZE [0]:
            self.derecha = False 
        
        if self.x <= 0:
            self.derecha = True
        
        # movemnent Y (up - down)
        if self.arriba:
            self.y -= 5
        else:
            self.y += 5

        if self.y + self.h >= SIZE [1]:
            self.arriba = True
        
        if self.y <= 0:
            self.arriba = False

        # solución MON
        # self.x += self.incremento_x
        # self.y += self.incremento_y

        # if self.x + self.w > SIZE [0] or self.x < 0:
        #     self.incremento_x *= -1
        
        # if self.y + self.h > SIZE [1] or self.y < 0:
        #     self.incremento_y *= -1


class Game(): # el bucle principal lo convertimos en una clase 
    def __init__(self):
        self.pantalla = pg.display.set_mode((SIZE))
        self.reloj = pg.time.Clock()

    def bucleppal(self):

        bola = Bola (SIZE[0]//2-10, SIZE[1]//2-10, 20, 20)
        game_over = False   
        pg.init()

        while not game_over:
            self.reloj.tick(60)

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

            self.pantalla.fill((0, 0, 0))
            pg.draw.rect(self.pantalla, bola.color, pg.Rect(bola.x, bola.y, bola.w, bola.h))

            bola.actualizate()

            pg.display.flip() 

        pg.quit()
        

if __name__ == "__main__": # para que no lo ejecute el programa si lo llamamos desde otro archivo  
    juego = Game() #instanciar la clase
    juego.bucleppal() #llamar al método de la calse Game de la instancia juego

