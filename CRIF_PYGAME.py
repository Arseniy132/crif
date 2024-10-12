import struct
import pygame


class CrifSprite(pygame.sprite.Sprite):
    def __init__(self, crif):
        super().__init__()
        with open(crif, "rb") as f:
            width, height = struct.unpack("II", f.read(8))
            self.image = pygame.Surface((width, height), pygame.SRCALPHA)
            pixel_data = []
            for _ in range(width * height):
                r, g, b, a = struct.unpack("BBBB", f.read(4))
                pixel_data.append((r, g, b, a))

            for y in range(height):
                for x in range(width):
                    self.image.set_at((x, y), pixel_data[y * width + x])

        self.rect = self.image.get_rect()

def crif_sprite(crif):
    return CrifSprite(crif)

pygame.init()
sprite = crif_sprite("crif.crif")
width = sprite.rect.width
height = sprite.rect.height
screen = pygame.display.set_mode((width, height))
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite)
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()