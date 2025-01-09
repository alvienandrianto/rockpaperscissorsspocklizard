import pygame, random

class BG():

    def __init__(self):
        self.width = 1200
        self.height = 750
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Rock-Paper-Scissors!')
        self.bg = pygame.image.load('./imgs/Bg.jpg')
        self.img1 = pygame.image.load('./imgs/Rock.png')
        self.img2 = pygame.image.load('./imgs/Paper.png')
        self.img3 = pygame.image.load('./imgs/Scissors.png')
        self.img4 = pygame.image.load('./imgs/Spock.png')
        self.img5 = pygame.image.load('./imgs/Lizard.png')
        self.img6 = pygame.image.load('./imgs/question/null.png')
        self.choice_rock = pygame.transform.scale2x(self.img1)
        self.choice_paper = pygame.transform.scale2x(self.img2)
        self.choice_scissors = pygame.transform.scale2x(self.img3)
        self.choice_spock = pygame.transform.scale2x(self.img4)
        self.choice_lizard = pygame.transform.scale2x(self.img5)
        self.font = pygame.font.SysFont('Arial', 50, bold = True, italic = True)
        self.sfont = pygame.font.SysFont('Arial', 25, bold = True, italic = True)
        self.period = 0
        

    def background(self):
        self.screen.blit(self.bg, (0, 0))

    def WaitP2(self):
        if self.period > 5:
            self.period = 0
        text = 'Waiting player2' + '.' * self.period
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        self.screen.blit(textsurface,(390, 25))

    def DoConnect(self):
        text = 'Connect'
        textsurface = self.sfont.render(text, False, (255, 0, 0))
        self.screen.blit(textsurface,(980, 150))

    def P2Join(self):
        if self.period > 5:
            self.period = 0
        text = 'Player2 Join Game' + '.' * self.period
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        self.screen.blit(textsurface,(390, 25))

    def DoCheck(self):
        text = 'Waiting P2 Check'
        textsurface = self.sfont.render(text, False, (255, 0, 0))
        self.screen.blit(textsurface,(920, 150))

    def DoGame(self):
        text = 'Start Game'
        textsurface = self.sfont.render(text, False, (255, 0, 0))
        self.screen.blit(textsurface,(960, 150))

    def WaitingPuch(self):
        if self.period > 5:
            self.period = 0
        text = 'throw' + '.' * self.period
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        self.screen.blit(textsurface,(500, 25))

    def Ready(self):
        text = 'Ready'
        textsurface = self.sfont.render(text, False, (255, 0, 0))
        self.screen.blit(textsurface,(985, 150))

    def win(self):
        text = "Win!!!"
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        self.screen.blit(textsurface,(500, 25))

    def loss(self):
        text = "Lose..."
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        self.screen.blit(textsurface,(500, 25))

    def darw(self):
        text = "Darw"
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        self.screen.blit(textsurface,(500, 25))

    def again(self):
        text = 'Again'
        textsurface = self.sfont.render(text, False, (255, 0, 0))
        self.screen.blit(textsurface,(985, 150))

class Player1(BG):
    def __init__(self):
        super().__init__()
        self.Stage = None
        self.player1_rock = pygame.transform.flip(self.choice_rock, True, False)
        self.player1_paper = pygame.transform.flip(self.choice_paper, True, False)
        self.player1_scissors = pygame.transform.flip(self.choice_scissors, True, False)
        self.player1_spock = pygame.transform.flip(self.choice_spock, True, False)
        self.player1_lizard = pygame.transform.flip(self.choice_lizard, True, False)
        self.x = 320
        self.y = 150

    def Rock(self):
        self.screen.blit(self.player1_rock, (self.x, self.y))
    def Paper(self):
        self.screen.blit(self.player1_paper, (self.x, self.y))
    def Scissors(self):
        self.screen.blit(self.player1_scissors, (self.x, self.y))
    def Spock(self):
        self.screen.blit(self.player1_spock, (self.x, self.y))
    def Lizard(self):
        self.screen.blit(self.player1_lizard, (self.x, self.y))

    def unknown(self):
        test = random.randint(1,5)
        if test == 1:
            self.Rock()
        if test == 2:
            self.Paper()
        if test == 3:
            self.Scissors()
        if test == 4:
            self.Spock()
        if test == 5:
            self.Lizard()

    def choice(self, i):
        if i == "Rock":
            self.Rock()
        if i == "Paper":
            self.Paper()
        if i == "Scissors":
            self.Scissors()
        if i == "Spock":
            self.Spock()
        if i == "Lizard":
            self.Lizard()
        if i == None:
            pass

class Player2(BG):
    def __init__(self):
        super().__init__()
        self.Stage = None
        self.x = 630
        self.y = 150

    def Rock(self):
        self.screen.blit(self.choice_rock, (self.x, self.y))
    def Paper(self):
        self.screen.blit(self.choice_paper, (self.x, self.y))
    def Scissors(self):
        self.screen.blit(self.choice_scissors, (self.x, self.y))
    def Spock(self):
        self.screen.blit(self.choice_spock, (self.x, self.y))
    def Lizard(self):
        self.screen.blit(self.choice_lizard, (self.x, self.y))

    def unknown(self):
        test = random.randint(1,5)
        if test == 1:
            self.Rock()
        if test == 2:
            self.Paper()
        if test == 3:
            self.Scissors()
        if test == 4:
            self.Spock()
        if test == 5:
            self.Lizard()

    def choice(self, i):
        if i == "Rock":
            self.Rock()
        if i == "Paper":
            self.Paper()
        if i == "Scissors":
            self.Scissors()
        if i == "Spock":
            self.Spock()
        if i == "Lizard":
            self.Lizard()
        if i == None:
            pass

class Button(Player1):
    def __init__(self):
        super().__init__()
        self.button_sound = pygame.mixer.Sound('./sound/bottle.wav')
        self.Button_start = pygame.image.load('./imgs/Start_gb.png')
        self.Button_rock = pygame.image.load('./imgs/Rock_gb.png')
        self.Button_paper = pygame.image.load('./imgs/Paper_gb.png')
        self.Button_scissors = pygame.image.load('./imgs/Scissors_gb.png')
        self.Button_spock = pygame.image.load('./imgs/Spock_gb.png')
        self.Button_lizard = pygame.image.load('./imgs/Lizard_gb.png')
        self.Button_start_click = pygame.image.load('./imgs/Start_yb.png')
        self.Button_rock_click = pygame.image.load('./imgs/Rock_yb.png')
        self.Button_paper_click = pygame.image.load('./imgs/Paper_yb.png')
        self.Button_scissors_click = pygame.image.load('./imgs/Scissors_yb.png')
        self.Button_spock_click = pygame.image.load('./imgs/Spock_yb.png')
        self.Button_lizard_click = pygame.image.load('./imgs/Lizard_yb.png')
    def ButtonStart(self):
        self.start_rect = self.screen.blit(self.Button_start, (920, 200))
    def ButtonStartClick(self):
        self.start_rect = self.screen.blit(self.Button_start_click, (920, 200))
        
    def ButtonRock(self):
        self.rock_rect = self.screen.blit(self.Button_rock, (100, 550))
    def ButtonRockClick(self):
        self.screen.blit(self.Button_rock_click, (100, 550))
        
    def ButtonPaper(self):
        self.paper_rect = self.screen.blit(self.Button_paper, (100, 420))
    def ButtonPaperClick(self):
        self.screen.blit(self.Button_paper_click, (100, 420))
        
    def ButtonScissors(self):
        self.scissors_rect = self.screen.blit(self.Button_scissors, (100, 290))
    def ButtonScissorsClick(self):
        self.screen_rect = self.screen.blit(self.Button_scissors_click, (100, 290))
        
    def ButtonSpock(self):
        self.spock_rect = self.screen.blit(self.Button_spock, (100, 160))
    def ButtonSpockClick(self):
        self.screen_rect = self.screen.blit(self.Button_spock_click, (100, 160))
        
    def ButtonLizard(self):
        self.lizard_rect = self.screen.blit(self.Button_lizard, (100, 30))
    def ButtonLizardClick(self):
        self.screen_rect = self.screen.blit(self.Button_lizard_click, (100, 30))