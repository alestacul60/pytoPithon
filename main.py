import pygame
import random
import math

pygame.init()

WHITE = (255, 255, 255)

class Image(pygame.sprite.Sprite):
    def __init__(self, speed_factor):
        super().__init__()
        original_image = pygame.image.load("imagen.gif").convert_alpha()
        self.image = pygame.Surface((original_image.get_width() // 4, original_image.get_height() // 4), pygame.SRCALPHA)
        self.image.blit(pygame.transform.scale(original_image, (original_image.get_width() // 4, original_image.get_height() // 4)), (0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, 800), random.randint(0, 600))
        self.speed_factor = speed_factor  # Factor de velocidad ajustable
        self.last_clone_time = 0 

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        dx = mouse_pos[0] - self.rect.center[0]
        dy = mouse_pos[1] - self.rect.center[1]
        dist = math.sqrt(dx ** 2 + dy ** 2)

        if dist > 0:
            dx_normalized = dx / dist
            dy_normalized = dy / dist

            dx_adjusted = dx_normalized * self.speed_factor
            dy_adjusted = dy_normalized * self.speed_factor

            self.rect.x += dx_adjusted
            self.rect.y += dy_adjusted

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Imagen sigue al mouse")

all_sprites = pygame.sprite.Group()


image = Image(1) 
all_sprites.add(image)

running = True
while running:
    current_time = pygame.time.get_ticks()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    mouse_pos = pygame.mouse.get_pos()
    collision = any(sprite.rect.collidepoint(mouse_pos) for sprite in all_sprites)
    if collision and current_time - image.last_clone_time > 500:
       
        clone = Image(1) 
        clone.rect.center = (random.randint(0, 800), random.randint(0, 600))
        all_sprites.add(clone)
        image.last_clone_time = current_time  

    all_sprites.update()

    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()