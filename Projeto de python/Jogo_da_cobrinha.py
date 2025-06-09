import tkinter as tk
import random

# Tamanho da grade
LARGURA = 600
ALTURA = 400
TAMANHO_CELULA = 20

# Direções
DIRECOES = {
    "cima": (0, -1),
    "baixo": (0, 1),
    "esquerda": (-1, 0),
    "direita": (1, 0)
}

class JogoCobrinha:
    def __init__(self, master):
        self.master = master
        self.master.title("🐍 Jogo da Cobrinha")

        self.canvas = tk.Canvas(master, width=LARGURA, height=ALTURA, bg="black")
        self.canvas.pack()

        self.resetar_jogo()
        self.master.bind("<KeyPress>", self.mudar_direcao)
        self.atualizar_jogo()

    def resetar_jogo(self):
        self.direcao = "direita"
        self.cobrinha = [(5, 5), (4, 5), (3, 5)]
        self.maca = self.gerar_maca()
        self.jogo_ativo = True

    def desenhar_celula(self, x, y, cor):
        x1 = x * TAMANHO_CELULA
        y1 = y * TAMANHO_CELULA
        x2 = x1 + TAMANHO_CELULA
        y2 = y1 + TAMANHO_CELULA
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=cor, outline="")

    def desenhar(self):
        self.canvas.delete("all")
        for segmento in self.cobrinha:
            self.desenhar_celula(*segmento, cor="green")
        self.desenhar_celula(*self.maca, cor="red")

    def mover_cobrinha(self):
        dx, dy = DIRECOES[self.direcao]
        cabeca_x, cabeca_y = self.cobrinha[0]
        nova_cabeca = (cabeca_x + dx, cabeca_y + dy)

        # Verificar colisões
        if (
            nova_cabeca in self.cobrinha or
            nova_cabeca[0] < 0 or
            nova_cabeca[1] < 0 or
            nova_cabeca[0] * TAMANHO_CELULA >= LARGURA or
            nova_cabeca[1] * TAMANHO_CELULA >= ALTURA
        ):
            self.jogo_ativo = False
            return

        self.cobrinha.insert(0, nova_cabeca)

        # Comer a maçã
        if nova_cabeca == self.maca:
            self.maca = self.gerar_maca()
        else:
            self.cobrinha.pop()

    def gerar_maca(self):
        while True:
            x = random.randint(0, (LARGURA // TAMANHO_CELULA) - 1)
            y = random.randint(0, (ALTURA // TAMANHO_CELULA) - 1)
            if (x, y) not in self.cobrinha:
                return (x, y)

    def mudar_direcao(self, event):
        tecla = event.keysym
        opostos = {"cima": "baixo", "baixo": "cima", "esquerda": "direita", "direita": "esquerda"}
        nova = {
            "Up": "cima",
            "Down": "baixo",
            "Left": "esquerda",
            "Right": "direita"
        }.get(tecla, self.direcao)

        if nova != opostos.get(self.direcao, ""):
            self.direcao = nova

    def atualizar_jogo(self):
        if self.jogo_ativo:
            self.mover_cobrinha()
            self.desenhar()
            self.master.after(100, self.atualizar_jogo)
        else:
            self.canvas.create_text(LARGURA//2, ALTURA//2, text="FIM DE JOGO", fill="white", font=("Arial", 24))

# Iniciar o jogo
root = tk.Tk()
jogo = JogoCobrinha(root)
root.mainloop()

            
