#!/usr/bin/env python
#coding: utf-8

#Author: Mateus Ferreira Silva
#Data: 11/02/2013

import curses
import random
import string

class wordkill():
    def __init__(self):
        curses.initscr() # Inicia janela
        curses.start_color() # Habilita cor
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK) # Par cor 1
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) # Par cor 2
        curses.noecho() # desabilita a impressão do getch()
        curses.curs_set(0) # setar um cursos na tela
        self.win = curses.newwin(17, 30, 0, 0) # Nova janela de 30 linhas 17 colunas começando em x 0 e y 0
        self.win.keypad(0)
        self.win.nodelay(1)
        self.win.border(0) # Borda default
        self.win.addstr(0, 9, '|')
        self.win.addstr(0, 20, '|')
        self.win.addstr(0, 10, ' WORDKILL ', curses.color_pair(1))

    def start(self):  
        key = 0
        score = 0
        timeout = 200
        lifes = 5
        pos_y = 1
        pos_x = random.randrange(1, 15)
        letters = string.lowercase
        letter = random.randrange(0, 27)
        while key != 27:
            self.win.timeout(timeout)
            self.win.addstr(16, 3, ' Letras: ')
            self.win.addstr(16, 10, ' {} '.format(score), curses.color_pair(1))
            self.win.addstr(16, 18, ' Vidas: ')
            self.win.addstr(16, 24, ' {} '.format(lifes), curses.color_pair(1))
            
            #Captura tecla clicada
            key = self.win.getch()
            
            # Verifica possição da letra e a atualiza
            if pos_y < 16:
                if pos_y != 1:
                    self.win.addch(pos_y-1, pos_x, ' ') # remove caracter anterior
                self.win.addch(pos_y, pos_x, letters[letter], curses.color_pair(2)) # adiciona caracter
                pos_y += 1 # atualiza posição da letra
            else:
                self.win.addch(pos_y-1, pos_x, ' ') # remove caracter anterior
                pos_y = 1 # reseta a pos Y
                pos_x = random.randrange(1, 29) # atualiza a pos X
                letter = random.randrange(0, 26) # busca nova letra
                lifes -= 1 # diminui life
                # verifica se acabou as vidas
                if lifes == 0:
                    break
            
            #Compara o clique com a letra da vez
            if key == ord(letters[letter]):
                score += 1 # Aumenta o Score
                if timeout > 50:
                    timeout -= 2 # Diminui o delay para cada acerto
                # A cada 20 letras o jogador ganha 1 vida
                if score > 0 and score % 20 == 0:
                    lifes += 1
                self.win.addch(pos_y-1, pos_x, ' ') # remove caracter anterior
                pos_y = 1 # reseta a pos Y
                pos_x = random.randrange(1, 29) # atualiza a pos X
                letter = random.randrange(0, 26) # busca nova letra
        curses.endwin() # Finaliza janela
        print 'Você acertou {} letras.'.format(score)

if __name__ == "__main__":
    try:
        wk = wordkill()
        wk.start()
    except:
        curses.endwin() # Finaliza janela
