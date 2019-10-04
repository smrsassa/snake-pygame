import pygame
from random import randrange

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()

largura = 320
altura = 280 # + 40 pixes para o placar
tamanho = 10
placar = 40

relogio = pygame.time.Clock()
fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")

def texto(msg, cor, tam, x, y):
    fonte = pygame.font.SysFont(None, tam)
    texto1 = fonte.render(msg, True, cor)
    fundo.blit(texto1, [x, y])

def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, black, [XY[0], XY[1], tamanho, tamanho])

def maca(maca_x, maca_y):
    pygame.draw.rect(fundo, red, [maca_x, maca_y, tamanho, tamanho])

def jogo():
    sair = True
    fimdejogo = False
    pos_x = randrange(0, largura-tamanho, 10)
    pos_y = randrange(0, altura-tamanho-placar, 10)
    maca_x = randrange(0, largura-tamanho, 10)
    maca_y = randrange(0, altura-tamanho-placar, 10)
    velocidade_x = 0
    velocidade_y = 0
    CobraXY = list()
    Cobralvl = 1
    pontos = 0
    while sair:
        while fimdejogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                            sair = True
                            fimdejogo = False
                            pos_x = randrange(0, largura-tamanho, 10)
                            pos_y = randrange(0, altura-tamanho-placar, 10)
                            maca_x = randrange(0, largura-tamanho, 10)
                            maca_y = randrange(0, altura-tamanho-placar, 10)
                            velocidade_x = 0
                            velocidade_y = 0
                            CobraXY = list()
                            Cobralvl = 1
                            pontos = 0
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > 45 and y > 120 and x < 180 and y < 147:
                        sair = True
                        fimdejogo = False
                        pos_x = randrange(0, largura-tamanho, 10)
                        pos_y = randrange(0, altura-tamanho-placar, 10)
                        maca_x = randrange(0, largura-tamanho, 10)
                        maca_y = randrange(0, altura-tamanho-placar, 10)
                        velocidade_x = 0
                        velocidade_y = 0
                        CobraXY = list()
                        Cobralvl = 1
                        pontos = 0
                    if x > 190 and y > 120 and x < 265 and y < 147:
                        sair = False
                        fimdejogo = False
            fundo.fill(white)
            texto('Fim de Jogo', red, 50, 65, 30)
            texto('Pontuação final: '+str(pontos), black, 30, 70, 80)
            pygame.draw.rect(fundo, black, [45, 120, 135, 27])
            texto('Continuar(C)', white, 30, 50, 125)
            pygame.draw.rect(fundo, black, [190, 120, 75, 27])
            texto('Sair(S)', white, 30, 195, 125)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho
                if event.key == pygame.K_SPACE:
                    Cobralvl += 1
                    pontos += 1
        if sair:
            fundo.fill(white)
            pos_x += velocidade_x
            pos_y += velocidade_y

            if pos_x == maca_x and pos_y == maca_y:
                maca_x = randrange(0, largura-tamanho, 10)
                maca_y = randrange(0, altura-tamanho-placar, 10)
                Cobralvl += 1
                pontos += 1
        
            #if pos_x + tamanho > largura:
            #    pos_x = 0
            #if pos_x < 0:
            #    pos_x = largura-tamanho
            #if pos_y + tamanho > altura - placar:
            #    pos_y = 0
            #if pos_y < 0:
            #    pos_y = altura-tamanho-placar
            if pos_x + tamanho > largura:
                fimdejogo = True
            if pos_x < 0:
                fimdejogo = True
            if pos_y + tamanho > altura - placar:
                fimdejogo = True
            if pos_y < 0:
                fimdejogo = True

            CobraInicio = list()
            CobraInicio.append(pos_x)
            CobraInicio.append(pos_y)
            CobraXY.append(CobraInicio)
            if len(CobraXY) > Cobralvl:
                del CobraXY[0]
            if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
                fimdejogo = True
            
            pygame.draw.rect(fundo, black, [0, altura - placar, largura, placar])
            texto("Pontuação:"+str(pontos), white, 20, 10, altura - 30)
            cobra(CobraXY)
            maca(maca_x, maca_y)
            pygame.display.update()
            relogio.tick(12)


jogo()

pygame.quit()
