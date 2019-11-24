from cmu_112_graphics import *
from tkinter import *
import random
from PIL import Image


class SplashScreenMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_text(mode.width / 2, 150, text='This demos a ModalApp!', font=font)
        canvas.create_text(mode.width / 2, 200, text='This is a modal splash screen!', font=font)
        canvas.create_text(mode.width / 2, 250, text='Press any key for the game!', font=font)

    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.gameMode)


class GameMode(Mode):
    def appStarted(mode):
        mode.score = 0
        mode.scrollX = 0
        mode.player = Player(mode)
        mode.dots = []
        mode.dotSet = set()
        mode.maxX = 3000
        mode.draggingDot = None
        numberOfNormalStonks = 0
        for _ in range(30):
            newDot = Dot(mode,
                         random.randint(0, mode.maxX),
                         random.randint(0, mode.height)
                         )
            mode.dots.append(newDot)

    def keyPressed(mode, event):
        mode.player.move(event.key)

    # def mouseMoved(mode, event):
    #     mode.cursorPos = [event.x, event.y]

    def mousePressed(mode, event):
        for dot in mode.dots:
            if dot.containsPoint(event.x + mode.scrollX, event.y):  # there is no mode.scrollY so we good
                mode.draggingDot = dot

    def mouseReleased(mode, event):
        mode.draggingDot = None

    def mouseDragged(mode, event):
        if mode.draggingDot is not None:
            mode.draggingDot.cx = event.x + mode.scrollX
            mode.draggingDot.cy = event.y
            mode.player.getDots()
        # mode.cursorPos = [event.x, event.y]

    def redrawAll(mode, canvas):
        # canvas.create_image(mode.cursorPos[0], cursorPos[1], image=ImageTk.PhotoImage(mode.cursorImage))
        mode.player.draw(canvas)
        for stonk in mode.dots: dot.draw(canvas)
        canvas.create_text(mode.width // 2, 30, text=str(mode.score))


class Player(object):

    def appStarted(self):
        self.playerX = self.app.width // 2
        self.playerY = self.app.height // 2
        self.scrollX = 0
        self.scrollMargin = 50
        self.playerX = self.app.width // 2  # player's center
        self.dots = []
        # for i in range(100):
        #     self.mode.dots.append(Dot(random.randint(0,20)))

        url = 'https://www.trzcacak.rs/myfile/full/441-4411625_parrot-sprite-sheet-bird-transparency.png'
        spritestrip = self.loadImage(url)  # .transpose(Image.FLIP_LEFT_RIGHT)

        # x, y = spritestrip.size
        # numSpritesX = 5
        # numSpritesY = 3
        # xSpace = x // numSpritesX
        # ySpace = y // numSpritesY
        self.sprites = []
        for j in range(2):
            for i in range(3):
                sprite = spritestrip.crop((342 * i, 0 + 300 * j, 342 + 342 * i, 265 + 300 * j))
                sprite = self.scaleImage(sprite, 1 / 3)
                self.sprites.append(sprite)
        self.spriteCounter = 0
        # self.app.timerDelay = 300

    def makePlayerVisible(self):
        # scroll to make player visible as needed
        if (self.playerX < self.scrollX + self.scrollMargin):
            self.scrollX = self.playerX - self.scrollMargin
        if (self.playerX > self.scrollX + self.app.width - self.scrollMargin):
            self.scrollX = self.playerX - self.app.width + self.scrollMargin

    def movePlayer(self, dx, dy):
        self.playerX += dx
        self.playerY += dy
        self.makePlayerVisible()
        self.playerX -= self.scrollX

    def keyPressed(self, event):
        if (event.key == "Left"):
            self.movePlayer(-10, 0)
        elif (event.key == "Right"):
            self.movePlayer(+10, 0)
        elif (event.key == "Up"):
            self.movePlayer(0, -10)
        elif (event.key == "Down"):
            self.movePlayer(0, +10)

    def timerFired(self):
        self.spriteCounter = (1 + self.spriteCounter) % len(self.sprites)

    def draw(self, canvas):
        sprite = self.sprites[self.spriteCounter]
        canvas.create_image(self.playerX, self.playerY, image=ImageTk.PhotoImage(sprite))
        # canvas.create_image


class Dots(object):
    def __init__(self, mode, x, y):
        self.x = x
        self.y = y
        self.mode = mode

    def draw(self):
        drawX = self.x - self.mode.scrollX
        drawY = self.y
        canvas.create_oval(drawX - 5, drawY - 5, drawX + 5, drawY + 5, fill='yellow')


class HelpMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_text(mode.width / 2, 150, text='This is the help screen!', font=font)
        canvas.create_text(mode.width / 2, 250, text='(Insert helpful message here)', font=font)
        canvas.create_text(mode.width / 2, 350, text='Press any key to return to the game!', font=font)


class MyModalApp(ModalApp):
    def appStarted(app):
        app.splashScreenMode = SplashScreenMode()
        app.gameMode = GameMode()
        app.helpMode = HelpMode()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 50


# def runCreativeSideScroller():
MyModalApp(width=500, height=500)
