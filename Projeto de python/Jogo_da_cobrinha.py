import tkinter as tk
import random
import sys

# Configurações do jogo
LARGURA = 600
ALTURA = 400
TAMANHO_CELULA = 20
VELOCIDADE = 100  # milissegundos entre movimentos

# Cores
COR_FUNDO = "#000000"
COR_COBRA = "#00FF00"
COR_MACA = "#FF0000"

class JogoCobrinha:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Cobrinha 🐍")
        self.canvas = tk.Canvas(master, width=LARGURA, height=ALTURA, bg=COR_FUNDO)
        self.canvas.pack()
        
        self.direcao = "Direita"
        self.cobra = [(100, 100), (80, 100), (60, 100)]  # posição inicial
        self.maca = self.criar_maca()

        self.master.bind("<KeyPress>", self.mudar_direcao)
        self.atualizar_jogo()

    def criar_maca(self):
        while True:
            x = random.randint(0, (LARGURA - TAMANHO_CELULA) // TAMANHO_CELULA) * TAMANHO_CELULA
            y = random.randint(0, (ALTURA - TAMANHO_CELULA) // TAMANHO_CELULA) * TAMANHO_CELULA
            if (x, y) not in self.cobra:
                return (x, y)

    def mudar_direcao(self, evento):
        tecla = evento.keysym
        if tecla == "Up" and self.direcao != "Baixo":
            self.direcao = "Cima"
        elif tecla == "Down" and self.direcao != "Cima":
            self.direcao = "Baixo"
        elif tecla == "Left" and self.direcao != "Direita":
            self.direcao = "Esquerda"
        elif tecla == "Right" and self.direcao != "Esquerda":
            self.direcao = "Direita"

    def mover_cobra(self):
        x, y = self.cobra[0]
        if self.direcao == "Cima":
            