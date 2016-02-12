from pygamehelper import *
from pygame import *
from pygame.locals import *
from Player import Player
from Enemy import Enemy
from vec2d import *
from Particles import *
import random

class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 500
        self.player = Player()
        self.health = 10
        self.gameover = False

        self.screenshakex = 0
        self.screenshakey = 0
        self.shaking = False
        self.shake_time = 0


        self.score = 0

        self.enemies = []

        self.particles = []

        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))

        self.font = pygame.font.SysFont("monospace", 40)
        self.label = self.font.render("Game Over(ENTER TO RESTART)", 1, (0,0,0))
        self.scorelabel = self.font.render(str(self.score), 1, (0,0,0))

    def update(self):
        self.player.update()

        for e in self.enemies:
            e.update()
            if e.y > 500:
                self.health -= 1
                self.enemies.remove(e)
                self.shaking = True
                self.shake_time += 30
                
                if self.health < 1:
                    self.gameover = True

            for b in self.player.bullets:
                bcenterx = b.x+4
                bcentery = b.y+4

                ecenterx = e.x+0.5*e.radius
                ecentery = e.y+0.5*e.radius

                if vec2d(bcenterx, bcentery).get_distance(vec2d(ecenterx, ecentery)) <= 8+e.radius:
                    self.enemies.remove(e)
                    self.particles.append(Particles(e.x, e.y, e.color))
                    self.score += random.randint(100,150)
                    self.player.bullets.remove(b)
                    

        rnd = random.randint(1, 100)
        if rnd == 50:
            self.enemies.append(Enemy()) 

        for ps in self.particles:
            ps.update()
            if ps.removepls:
                self.particles.remove(ps)

        for b in self.player.bullets:
            if b.y < 0:
                self.player.bullets.remove(b)

        self.screenshake_update()

    def keyUp(self, key):
        if key == K_d:
            if self.player.moving == "r":
                self.player.moving = "No"
        elif key == K_a:
            if self.player.moving == "l":
                self.player.moving = "No"

    def keyDown(self, key):
        if key == K_d:
            self.player.moving = "r"

        elif key == K_a:
            self.player.moving = "l"

        elif key == K_SPACE:
            self.player.shoot()

        elif key == K_RETURN and self.gameover:
            self.player = Player()
            self.enemies = []
            self.health = 10
            self.score = 0
            self.gameover = False
            screenshakex = 0
            screenshakey = 0

    def screenshake_update(self):
        if self.shake_time < 1:
            self.screenshakex = 0
            self.screenshakey = 0
            return
        
        self.screenshakex = random.randint(-20, 20)
        self.screenshakey = random.randint(-20, 20)

        self.shake_time -= 1

    def draw(self):
        self.screen.fill((255,255,255))

        ox = int(self.screenshakex)
        oy = int(self.screenshakey)


        if not self.gameover:            

            pygame.draw.circle(self.screen, (30, 20, 100), (self.player.x+ox, self.player.y+oy), 32)

            for ps in self.particles:
                for p in ps.particles:
                    pygame.draw.circle(self.screen, ps.color, (p.x+ox, p.y+oy), 2)

            for b in self.player.bullets:
                pygame.draw.circle(self.screen, (0, 0, 0), (int(b.x)+ox, b.y+oy), 8)

            for e in self.enemies:
                pygame.draw.circle(self.screen, e.color, (e.x+ox, e.y+oy), e.radius)

            for i in range(1, self.health):
                pygame.draw.circle(self.screen, (200, 50, 50), (i*10, 450), 4)

            self.scorelabel = self.font.render(str(self.score), 1, (0,0,0))
            self.screen.blit(self.scorelabel, (600, 425))

        else:
            self.screen.blit(self.label, (50, 250))


s = Starter()
s.mainLoop(60)