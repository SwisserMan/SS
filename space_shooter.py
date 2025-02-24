import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 20
player_speed = 7

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemies = []

# Bullet settings
bullet_width = 5
bullet_height = 15
bullet_speed = 7
bullets = []

# Score
score = 0
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, [x, y, player_width, player_height])

def draw_enemy(enemy):
    pygame.draw.rect(screen, RED, enemy)

def draw_bullet(bullet):
    pygame.draw.rect(screen, WHITE, bullet)

def move_enemies(enemies):
    for enemy in enemies:
        enemy.move_ip(0, enemy_speed)

def move_bullets(bullets):
    for bullet in bullets:
        bullet.move_ip(0, -bullet_speed)

def remove_off_screen_bullets(bullets):
    return [bullet for bullet in bullets if bullet.bottom > 0]

def check_collision(bullets, enemies):
    global score
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                return

# Game loop
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append(pygame.Rect(player_x + player_width // 2 - bullet_width // 2, player_y, bullet_width, bullet_height))

    if random.randint(1, 50) == 1:
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemies.append(pygame.Rect(enemy_x, 0, enemy_width, enemy_height))

    move_enemies(enemies)
    move_bullets(bullets)
    bullets = remove_off_screen_bullets(bullets)
    check_collision(bullets, enemies)

    draw_player(player_x, player_y)
    for enemy in enemies:
        draw_enemy(enemy)
    for bullet in bullets:
        draw_bullet(bullet)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
