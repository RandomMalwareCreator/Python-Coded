import pygame
import random
import math
import sys
import time

# Inicializa o Pygame
pygame.init()

# Definir a largura e altura da tela
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("GDI+")

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Função para distorcer a tela com quadrados aleatórios
def distort_screen():
    for _ in range(50):
        rect_width = random.randint(20, 100)
        rect_height = random.randint(20, 100)
        rect_x = random.randint(0, screen_width - rect_width)
        rect_y = random.randint(0, screen_height - rect_height)
        pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (rect_x, rect_y, rect_width, rect_height))

# Função para o efeito de derretimento da tela
def melt_screen():
    for y in range(0, screen_height, 10):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.line(screen, color, (0, y), (screen_width, y), random.randint(1, 10))

# Função para o efeito de "túnel MEMZ"
def memz_tunnel():
    center_x, center_y = screen_width // 2, screen_height // 2
    max_radius = min(screen_width, screen_height) // 2
    for radius in range(0, max_radius, 10):
        pygame.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (center_x, center_y), radius, 5)
        pygame.display.update()
        time.sleep(0.05)  # Dá um pequeno delay para o efeito de "túnel"

# Função para a tela se mover e "flutuar"
def move_screen():
    move_x, move_y = random.randint(-5, 5), random.randint(-5, 5)
    for _ in range(100):
        screen.fill(WHITE)
        distort_screen()
        pygame.display.update()
        pygame.time.delay(50)
        pygame.display.update()
        time.sleep(0.05)

# Função principal que simula os efeitos
def main():
    clock = pygame.time.Clock()
    running = True
    start_time = time.time()

    while running:
        screen.fill(WHITE)  # Limpa a tela
        # Simulando efeitos diferentes
        if time.time() - start_time < 5:
            distort_screen()
        elif time.time() - start_time < 10:
            melt_screen()
        elif time.time() - start_time < 15:
            memz_tunnel()
        elif time.time() - start_time < 20:
            move_screen()
        else:
            # Reiniciar o ciclo após 20 segundos
            start_time = time.time()

        # Atualiza a tela
        pygame.display.flip()

        # Detecção de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Limitar FPS
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
