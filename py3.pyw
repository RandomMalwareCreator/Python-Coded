import pygame
import random
import time

# Inicializando o pygame
pygame.init()

# Definindo as dimensões da janela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GDI+ Window")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Variáveis de controle
circle_radius = 20  # Raio do círculo
circle_x, circle_y = 0, 0  # Posição inicial do círculo
clones = []  # Lista para armazenar clones do círculo
square_x, square_y = 100, 100  # Posição inicial do quadrado
square_size = 100  # Tamanho inicial do quadrado
dragging = False  # Controle para saber se estamos arrastando
dragging_corner = None  # Qual canto do quadrado estamos arrastando
screen_offset_x, screen_offset_y = 0, 0  # Controle do tremor
background_color = (255, 255, 255)  # Cor inicial de fundo

# Função para gerar uma cor aleatória
def cor_aleatoria():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Função para desenhar o quadrado com a opção de redimensionamento
def desenhar_quadrado():
    pygame.draw.rect(screen, (0, 0, 0), (square_x, square_y, square_size, square_size), 3)  # Borda do quadrado
    pygame.draw.rect(screen, (255, 0, 0), (square_x + square_size - 10, square_y + square_size - 10, 10, 10))  # Ponto de redimensionamento

# Função para mudar a cor de fundo
def mudar_cor_fundo():
    global background_color
    background_color = cor_aleatoria()

# Função para fazer a tela tremer (deslocando ligeiramente)
def tremer_tela():
    global screen_offset_x, screen_offset_y
    screen_offset_x = random.randint(-5, 5)
    screen_offset_y = random.randint(-5, 5)

# Função para desenhar o círculo e seus clones
def desenhar_circulo():
    global circle_x, circle_y
    pygame.draw.circle(screen, cor_aleatoria(), (circle_x, circle_y), circle_radius)
    
    # Desenhar clones do círculo
    for clone in clones:
        pygame.draw.circle(screen, clone['color'], (clone['x'], clone['y']), circle_radius)

# Função para criar clones do círculo quando ele atingir os limites
def criar_clone_circulo():
    global circle_x, circle_y, clones
    if circle_x > width - circle_radius or circle_y > height - circle_radius or circle_x < circle_radius or circle_y < circle_radius:
        clones.append({
            'x': random.randint(0, width),
            'y': random.randint(0, height),
            'color': cor_aleatoria()
        })

# Função principal
def main():
    global square_x, square_y, square_size, dragging, dragging_corner, circle_x, circle_y, clones, background_color
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill(background_color)  # Preenche o fundo com a cor aleatória

        # Lidar com os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Detecta o clique do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Verifica se o clique foi dentro do quadrado e se está no ponto de redimensionamento
                if square_x + square_size - 10 <= mouse_x <= square_x + square_size and square_y + square_size - 10 <= mouse_y <= square_y + square_size:
                    dragging = True
                    dragging_corner = "bottom_right"

            # Detecta o movimento do mouse
            if event.type == pygame.MOUSEMOTION:
                if dragging:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Arrasta a ponta do quadrado e altera o tamanho
                    if dragging_corner == "bottom_right":
                        square_size = max(30, mouse_x - square_x)
                        square_size = max(30, mouse_y - square_y)

                # Move o círculo com o mouse
                circle_x, circle_y = pygame.mouse.get_pos()

            # Detecta quando o mouse é solto
            if event.type == pygame.MOUSEBUTTONUP:
                dragging = False
                dragging_corner = None

        # Chama a função para tremer a tela
        tremer_tela()

        # Desenha o círculo e seus clones
        desenhar_circulo()

        # Criar clones do círculo quando atinge o limite da tela
        criar_clone_circulo()

        # Desenha o quadrado com as bordas e ponto de redimensionamento
        desenhar_quadrado()

        # Quando o quadrado atingir o tamanho mínimo, muda a cor de fundo
        if square_size <= 30:
            mudar_cor_fundo()

        # Atualiza a tela com o deslocamento para o tremor
        pygame.display.update()

        # Controla o FPS (frames por segundo)
        clock.tick(60)

# Executar o programa
if __name__ == "__main__":
    main()
    pygame.quit()
