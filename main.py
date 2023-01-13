import pygame

# Inicializar pygame
pygame.init()

# Establecer tamaño de la pantalla
screen = pygame.display.set_mode((400, 300))

# Establecer título de la ventana
pygame.display.set_caption("Mover cuadrado con flechas")

# Crear cuadrado
x = 50
y = 50
width = 50
height = 50
vel = 50
rect = pygame.Rect(x, y, width, height)

# Crear grilla
grid_size = 50
grid_color = (200, 200, 200)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Obtener tecla presionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.x -= vel
                rect.x = max(rect.x, 0)
            if event.key == pygame.K_RIGHT:
                rect.x += vel
                rect.x = min(rect.x, 400-width)
            if event.key == pygame.K_UP:
                rect.y -= vel
                rect.y = max(rect.y, 0)
            if event.key == pygame.K_DOWN:
                rect.y += vel
                rect.y = min(rect.y, 300-height)

    # Llenar pantalla de color blanco
    screen.fill((255, 255, 255))

    # Dibujar grilla
    for i in range(0, 400, grid_size):
        pygame.draw.line(screen, grid_color, (i, 0), (i, 300))
    for i in range(0, 300, grid_size):
        pygame.draw.line(screen, grid_color, (0, i), (400, i))

    # Dibujar cuadrado
    pygame.draw.rect(screen, (255, 0, 0), rect)

    # Actualizar pantalla
    pygame.display.update()

# Finalizar pygame
pygame.quit()

#https://www.linkedin.com/in/leoparada/
