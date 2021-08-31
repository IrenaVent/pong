import pygame as pg
from random import randrange

SIZE = (800,600) # we decided no parmetric screen


class Movil(): #la clase padre, IMPORTANTE de ellas heredan el resto
    
    def __init__(self, x, y, w, h, color=(255,255,255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    @property
    def izquierda(self):
        return self.x

    @izquierda.setter
    def izquierda(self,valor):
        self.x = valor

    @property
    def derecha(self):
        return self.x + self.w
    
    @derecha.setter
    def derecha (self, valor):
        self.x = valor - self.w

    @property
    def arriba(self):
        return self.y

    @arriba.setter
    def arriba(self, valor):
        self.y = valor

    @property
    def abajo(self):
        return self.y + self.h

    @abajo.setter
    def abajo(self, valor):
        self.y = valor - self.h

    def actualizate(self):
        pass

    def procesa_eventos(self, lista_eventos=[]):
        pass

    def dibujate(self, lienzo):
        pg.draw.rect(lienzo, self.color, pg.Rect(self.x, self.y, self.w, self.h))


class Raqueta(Movil):
    def __init__(self, x, y, color=(255,255,255)):
        Movil.__init__(self, x, y, 20, 120, color) #esto es lo mismo que ...otra manera de escribirlo
        self.tecla_arriba = pg.K_UP   # tecla_arriba será K_UP por defecto 
        self.tecla_abajo = pg.K_DOWN  # tecla_abajo será K_DOWN por defecto 

    def procesa_eventos(self, lista_eventos=[]):
        if pg.key.get_pressed()[self.tecla_arriba]:
            self.y -= 5
        
        if self.arriba <= 0:
            self.arriba = 0

        if pg.key.get_pressed()[self.tecla_abajo]:
            self.y += 5
        
        if self.abajo >= SIZE[1]:
            self.abajo = SIZE[1]
        

class Bola(Movil):
    def __init__(self, x, y, color=(255,255,255)):
        super().__init__(x, y, 20, 20, color) #esto es lo mismo que ... otra manera de escribirlo
        
        self.swDerecha = True
        self.swArriba = True

        # self.incremento_x = 5
        # self.incremento_y = 5

    def actualizate(self):

        # movement X (left - right)
        if self.swDerecha:
            self.x += 5
        else:
            self.x -= 5

        if self.derecha >= SIZE [0]: # if self.x + self.w >= SIZE [1]
            self.swDerecha = False 
        
        if self.izquierda <= 0:
            self.swDerecha = True
        
        # movemnent Y (up - down)
        if self.swArriba:
            self.y -= 5
        else:
            self.y += 5

        if self.abajo >= SIZE [1]: # if self.y + self.h >= SIZE [1]
            self.swArriba = True
        
        if self.arriba <= 0:
            self.swArriba = False

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
        self.todos = []

        self.player1 = Raqueta (10, (SIZE[1]-120) //2)
        self.player1.tecla_arriba = pg.K_w #sólo para player1, player dos utiliza K_UP/DOWN - y es en la calse donde se le asigna el valor K_UP
        self.player1.tecla_abajo = pg.K_s #sólo para player1, player dos utiliza K_UP/DOWN - y es en la calse donde se le asigna el valor K_DOWN
        
        self.player2 = Raqueta (SIZE[0]-30, (SIZE[1]-120) //2)
        
        self.todos.append(self.player1)
        self.todos.append(self.player2)

        self.bola = Bola(SIZE[0] // 2 - 10, SIZE[1] // 2 - 10, (255, 255, 0))

        self.todos.append(self.bola)

    def bucleppal(self):

        game_over = False   
        pg.init()

        while not game_over:
            self.reloj.tick(60)                 

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

            for movil in self.todos:
                movil.procesa_eventos()
                movil.actualizate()
            
            self.pantalla.fill((0, 0, 0))
           
            for movil in self.todos:
                movil.dibujate(self.pantalla)

            pg.display.flip() 

        pg.quit()
        

if __name__ == "__main__": # para que no lo ejecute el programa si lo llamamos desde otro archivo  
    juego = Game() #instanciar la clase
    juego.bucleppal() #llamar al método de la calse Game de la instancia juego

