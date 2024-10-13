import struct, pygame, os


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, crif):
        super().__init__()

        with open(crif, "rb") as f:
            self.width, self.height = struct.unpack("II", f.read(8))
            print(f"loading {crif} with dimensions: {self.width}x{self.height}")
            self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            pixel_data = []
            for _ in range(self.width + self.height):
                r, g, b, a = struct.unpack("BBBB", f.read(4))
                pixel_data.append((r, g, b, a))
            for y in range(self.height):
                for x in range(self.width):
                    self.image.set_at((x, y), pixel_data[y * self.width + x])

        self.rect = self.image.get_rect()

    def show(self, screen, x, y):
        self.rect.topleft = (x, y)
        screen.blit(self.image, self.rect)


def crif_to_sprite(crif):
    return GameSprite(crif)


pygame.init()
screen = pygame.display.set_mode((640, 480))
running = True
arduino = crif_to_sprite("arduino.crif")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    arduino.show(screen, 0, 0)
    pygame.display.flip()
pygame.quit()