import pygame
import random
import time
import threading

# Inicializa o Pygame
pygame.init()

# Tamanho da tela
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h  # Tamanho total da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME | pygame.FULLSCREEN)  # Tela cheia e sem bordas
pygame.display.set_caption('mainPYTHON')

# Cor de fundo
background_color = (0, 0, 0)

# Classe para a bola que quica e se multiplica
class BouncingBall:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        # Move a bola
        self.x += self.speed_x
        self.y += self.speed_y

        # Rebate nas bordas
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.speed_x = -self.speed_x  # Inverte a direção no eixo X
            self.create_ball()  # Cria uma nova bola

        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.speed_y = -self.speed_y  # Inverte a direção no eixo Y
            self.create_ball()  # Cria uma nova bola

    def create_ball(self):
        # Multiplica a bola, criando uma nova em uma posição aleatória
        new_radius = random.randint(10, 30)
        new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        new_speed_x = random.choice([-1, 1]) * random.randint(3, 5)
        new_speed_y = random.choice([-1, 1]) * random.randint(3, 5)
        balls.append(BouncingBall(self.x, self.y, new_radius, new_color, new_speed_x, new_speed_y))

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Lista de bolas
balls = []

# Função para fazer a tela "tremer" (deslocando aleatoriamente)
def screen_shake():
    for _ in range(60):  # Duração do tremor
        shake_x = random.randint(-20, 20)
        shake_y = random.randint(-20, 20)
        screen.fill(background_color)
        pygame.display.update()
        screen.fill(background_color)
        pygame.display.update()
        time.sleep(0.05)

# Função para o efeito "túnel" (multiplicação de quadrados)
def tunnel_effect():
    center = (WIDTH // 2, HEIGHT // 2)
    max_size = max(WIDTH, HEIGHT)  # Para cobrir toda a tela
    for i in range(max_size, 0, -20):  # O quadrado vai diminuir
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.rect(screen, color, pygame.Rect(center[0] - i // 2, center[1] - i // 2, i, i), 2)
        pygame.display.update()
        time.sleep(0.1)

# Função para distorcer as cores da tela
def color_distortion():
    for _ in range(60):  # Efeito de distorção de cor
        screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        pygame.display.update()
        time.sleep(0.1)

# Função para distorcer a tela (efeito de "duplicação")
def screen_multiplication():
    for i in range(10):  # Distorção com cópias da tela
        # Distorção criando cópias da tela com diferentes escalas e posições
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.rect(screen, color, pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), 100, 100))
        pygame.display.update()
        time.sleep(0.1)

# Função principal que chama os efeitos simultaneamente
def main_effects():
    # Efeitos simultâneos de falha (todos os efeitos ao mesmo tempo)
    threads = []
    threads.append(threading.Thread(target=screen_shake))
    threads.append(threading.Thread(target=tunnel_effect))
    threads.append(threading.Thread(target=color_distortion))
    threads.append(threading.Thread(target=screen_multiplication))

    # Inicia os threads
    for t in threads:
        t.start()

    # Espera os threads terminarem
    for t in threads:
        t.join()

# Função para rodar o jogo continuamente
def start_game():
    # Inicializa a tela com efeitos visuais
    screen.fill(background_color)
    pygame.display.update()

    # Cria uma bola inicial
    balls.append(BouncingBall(WIDTH // 2, HEIGHT // 2, 30, (255, 0, 0), 5, 5))

    # Loop principal do jogo
    running = True
    while running:
        # Checar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Fecha o jogo se a janela for fechada
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Fecha o jogo se pressionar ESC
                    running = False

        # Limpa a tela
        screen.fill(background_color)

        # Chama os efeitos principais (simultâneos)
        main_effects()

        # Mover e desenhar todas as bolas
        for ball in balls[:]:
            ball.move()  # Move a bola
            ball.draw()  # Desenha a bola

        # Atualiza a tela
        pygame.display.update()

# Função principal
if __name__ == "__main__":
    start_game()  # Inicia os efeitos diretamente
    pygame.quit()  # Finaliza o Pygame quando o jogo terminar

