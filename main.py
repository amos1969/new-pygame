#!/usr/bin/python3
import sys
import pygame
import random

pygame.init()


def main():
    setupGame()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                dealWithMouseClick(x, y)
        displayScreen()


def setupGame():
    global turn
    global screen
    global player1Name
    global player2Name
    global diceScore
    global subGo
    global redLeftPos
    global redRightPos
    global blackLeftPos
    global blackRightPos
    global mover
    global winner
    diceScore = 0
    player1Name = "Player 1"
    player2Name = "Player 2"
    screen = "Main Menu"
    turn = "Player 1"
    subGo = "A"
    mover = False
    createObjects()
    redLeftPos = 1
    redRightPos = 1
    blackLeftPos = 1
    blackRightPos = 1
    winner = ""
    setCounterPos()


def displayScreen():
    DISPLAYSURF.blit(background, backgroundRect)
    if screen == "Main Menu":
        displayMainMenu()
    elif screen == "Enter Names":
        displayEnterNames()
    elif screen == "Play Game":
        setCounterPos()
        displayPlayGame()
    pygame.display.flip()


def setCounterPos():
    global redCounterLeftRect
    global redCounterRightRect
    global blackCounterLeftRect
    global blackCounterRightRect
    redCounterLeftRect.x = 200
    redCounterLeftRect.y = 650 - (50 * redLeftPos)
    redCounterRightRect.x = 250
    redCounterRightRect.y = 650 - (50 * redRightPos)
    blackCounterLeftRect.x = 300
    blackCounterLeftRect.y = 650 - (50 * blackLeftPos)
    blackCounterRightRect.x = 350
    blackCounterRightRect.y = 650 - (50 * blackRightPos)


def displayMainMenu():
    line1 = myFont.render(player1Name, 0, (255, 255, 255))
    line1Rect = line1.get_rect()
    line1Rect.x = 20
    line1Rect.y = 20
    line2 = myFont.render(player2Name, 0, (255, 255, 255))
    line2Rect = line2.get_rect()
    line2Rect.x = 20
    line2Rect.y = 50
    DISPLAYSURF.blit(line1, line1Rect)
    DISPLAYSURF.blit(line2, line2Rect)
    DISPLAYSURF.blit(btnPlayGame, btnPlayGameRect)
    DISPLAYSURF.blit(btnEnterNames, btnEnterNamesRect)
    DISPLAYSURF.blit(btnQuitGame, btnQuitGameRect)


def displayEnterNames():
    line1 = myFont.render("Please go to the Python Shell to", 0, (255, 255, 255))
    line1Rect = line1.get_rect()
    line1Rect.centerx = backgroundRect.centerx
    line1Rect.y = 100
    DISPLAYSURF.blit(line1, line1Rect)
    line2 = myFont.render("enter player names.", 0, (255, 255, 255))
    line2Rect = line1.get_rect()
    line2Rect.centerx = backgroundRect.centerx
    line2Rect.y = 150
    DISPLAYSURF.blit(line2, line2Rect)
    pygame.display.flip()
    enterPlayerNames()


def enterPlayerNames():
    global player1Name
    global player2Name
    global screen
    player1Name = input("Please enter a name for Player 1:")
    player2Name = input("Please enter a name for Player 2:")
    screen = "Main Menu"


def displayPlayGame():
    if subGo == "Z":
        pass
    else:
        line1 = myFont.render(player1Name, 0, (255, 255, 255))
        line1Rect = line1.get_rect()
        line1Rect.x = 20
        line1Rect.y = 20
        line2 = myFont.render(player2Name, 0, (255, 255, 255))
        line2Rect = line2.get_rect()
        line2Rect.x = 20
        line2Rect.y = 50
        if subGo == "A":
            goA()
        if subGo == "B":
            goB()
        DISPLAYSURF.blit(line1, line1Rect)
        DISPLAYSURF.blit(line2, line2Rect)
        DISPLAYSURF.blit(board, boardRect)
        DISPLAYSURF.blit(redCounterLeft, redCounterLeftRect)
        DISPLAYSURF.blit(redCounterRight, redCounterRightRect)
        DISPLAYSURF.blit(blackCounterLeft, blackCounterLeftRect)
        DISPLAYSURF.blit(blackCounterRight, blackCounterRightRect)


def goA():
    if turn == "Player 1":
        whosGo = myFont.render(player1Name + " please roll", 0, (255, 255, 255))
    else:
        whosGo = myFont.render(player2Name + " please roll", 0, (255, 255, 255))
    whosGoRect = whosGo.get_rect()
    whosGoRect.x = 300
    whosGoRect.y = 20
    whosGo2 = myFont.render("the dice", 0, (255, 255, 255))
    whosGo2Rect = whosGo2.get_rect()
    whosGo2Rect.x = 300
    whosGo2Rect.y = 50
    DISPLAYSURF.blit(whosGo, whosGoRect)
    DISPLAYSURF.blit(whosGo2, whosGo2Rect)
    DISPLAYSURF.blit(btnRollDice, btnRollDiceRect)


def goB():
    global mover
    if turn == "Player 1":
        whosGo = myFont.render(player1Name + " you scored:", 0, (255, 255, 255))
    else:
        whosGo = myFont.render(player2Name + " you scored:", 0, (255, 255, 255))
    whosGoRect = whosGo.get_rect()
    whosGoRect.x = 300
    whosGoRect.y = 20
    whosGo2 = diceFont.render(str(diceScore), 0, (0, 255, 255))
    whosGo2Rect = whosGo2.get_rect()
    whosGo2Rect.x = 500
    whosGo2Rect.y = 70
    DISPLAYSURF.blit(whosGo, whosGoRect)
    DISPLAYSURF.blit(whosGo2, whosGo2Rect)
    firstLine = messageFont.render("You can move a counter:", 0, (0, 255, 255))
    firstLineRect = firstLine.get_rect()
    firstLineRect.x = 420
    firstLineRect.y = 150
    message = messageFont.render(diceMessage(), 0, (0, 255, 255))
    messageRect = message.get_rect()
    messageRect.x = 420
    messageRect.y = 180
    DISPLAYSURF.blit(firstLine, firstLineRect)
    DISPLAYSURF.blit(message, messageRect)
    if canThePlayerMove():
        mover = True
        chooseACounter = messageFont.render("Please choose a counter to move:", 0, (0, 255, 255))
        chooseACounterRect = chooseACounter.get_rect()
        chooseACounterRect.x = 410
        chooseACounterRect.y = 250
        DISPLAYSURF.blit(chooseACounter, chooseACounterRect)
        if turn == "Player 1":
            if canRedLeftMove():
                DISPLAYSURF.blit(btnLeft, btnLeftRect)
            else:
                DISPLAYSURF.blit(btnLeftNo, btnLeftRect)
            if canRedRightMove():
                DISPLAYSURF.blit(btnRight, btnRightRect)
            else:
                DISPLAYSURF.blit(btnRightNo, btnRightRect)
        else:
            if canBlackLeftMove():
                DISPLAYSURF.blit(btnLeft, btnLeftRect)
            else:
                DISPLAYSURF.blit(btnLeftNo, btnLeftRect)
            if canBlackRightMove():
                DISPLAYSURF.blit(btnRight, btnRightRect)
            else:
                DISPLAYSURF.blit(btnRightNo, btnRightRect)
    else:
        mover = False
        noMoveAvailable = messageFont.render("No valid move is possible.", 0, (255, 0, 0))
        noMoveAvailableRect = noMoveAvailable.get_rect()
        noMoveAvailableRect.x = 410
        noMoveAvailableRect.y = 250
        DISPLAYSURF.blit(noMoveAvailable, noMoveAvailableRect)
        DISPLAYSURF.blit(btnEndGo, btnEndGoRect)


def canThePlayerMove():
    if turn == "Player 1":
        if canRedLeftMove() or canRedRightMove():
            return True
    else:
        if canBlackLeftMove() or canBlackRightMove():
            return True
    return False


def canRedLeftMove():
    if diceScore < 4:
        if redLeftPos == 11:
            return False
        trialPos = redLeftPos + diceScore
        if trialPos == redRightPos:
            if trialPos == 5 or trialPos >= 11:
                return True
            else:
                return False
        else:
            return True
    else:
        if redLeftPos == 1:
            return False
        trialPos = redLeftPos - 1
        if trialPos == redRightPos:
            if trialPos == 5 or trialPos <= 1:
                return True
            else:
                return False
        else:
            return True


def canRedRightMove():
    if diceScore < 4:
        if redRightPos == 11:
            return False
        trialPos = redRightPos + diceScore
        if trialPos == redLeftPos:
            if trialPos == 5 or trialPos >= 11:
                return True
            else:
                return False
        else:
            return True
    else:
        if redRightPos == 1:
            return False
        trialPos = redRightPos - 1
        if trialPos == redLeftPos:
            if trialPos == 5 or trialPos <= 1:
                return True
            else:
                return False
        else:
            return True


def canBlackLeftMove():
    if diceScore < 4:
        if blackLeftPos == 11:
            return False
        trialPos = blackLeftPos + diceScore
        if trialPos == blackRightPos:
            if trialPos == 5 or trialPos >= 11:
                return True
            else:
                return False
        else:
            return True
    else:
        if blackLeftPos == 1:
            return False
        trialPos = blackLeftPos - 1
        if trialPos == blackRightPos:
            if trialPos == 5 or trialPos <= 1:
                return True
            else:
                return False
        else:
            return True
    return False


def canBlackRightMove():
    if diceScore < 4:
        if blackRightPos == 11:
            return False
        trialPos = blackRightPos + diceScore
        if trialPos == blackLeftPos:
            if trialPos == 5 or trialPos >= 11:
                return True
            else:
                return False
        else:
            return True
    else:
        if blackRightPos == 1:
            return False
        trialPos = blackRightPos - 1
        if trialPos == blackLeftPos:
            if trialPos == 5 or trialPos <= 1:
                return True
            else:
                return False
        else:
            return True


def diceMessage():
    theMessage = ""
    if diceScore == 1:
        theMessage = "1 space closer to the FINISH"
    elif diceScore == 2:
        theMessage = "2 spaces closer to the FINISH"
    elif diceScore == 3:
        theMessage = "3 spaces closer to the FINISH"
    elif diceScore == 4:
        theMessage = "1 space closer to the START"
    return theMessage


def dealWithMouseClick(theX, theY):
    global screen
    global subGo
    if screen == "Main Menu":
        if btnPlayGameRect.collidepoint(theX, theY):
            screen = "Play Game"
        elif btnEnterNamesRect.collidepoint(theX, theY):
            screen = "Enter Names"
        elif btnQuitGameRect.collidepoint(theX, theY):
            pygame.quit()
            sys.exit()
    if screen == "Play Game":
        if subGo == "A":
            if btnRollDiceRect.collidepoint(theX, theY):
                rollTheDice()
        if mover:
            if turn == "Player 1":
                if canRedLeftMove():
                    if btnLeftRect.collidepoint(theX, theY):
                        moveRedLeft()
                if canRedRightMove():
                    if btnRightRect.collidepoint(theX, theY):
                        moveRedRight()
            else:
                if canBlackLeftMove():
                    if btnLeftRect.collidepoint(theX, theY):
                        moveBlackLeft()
                if canBlackRightMove():
                    if btnRightRect.collidepoint(theX, theY):
                        moveBlackRight()
                pass
        else:
            if btnEndGoRect.collidepoint(theX, theY):
                changeTurn()


def moveRedLeft():
    global redLeftPos
    global blackLeftPos
    global blackRightPos
    if diceScore < 4:
        trialPos = redLeftPos + diceScore
        if trialPos > 11:
            redLeftPos = 11
        else:
            redLeftPos = trialPos
    else:
        redLeftPos = redLeftPos - 1
    if redLeftPos == 1 or redLeftPos == 5 or redLeftPos == 11:
        pass
    else:
        if blackLeftPos == redLeftPos:
            blackLeftPos = 1
        if blackRightPos == redLeftPos:
            blackRightPos = 1
    hasRedWon()
    changeTurn()


def moveRedRight():
    global redRightPos
    global blackLeftPos
    global blackRightPos
    if diceScore < 4:
        trialPos = redRightPos + diceScore
        if trialPos > 11:
            redRightPos = 11
        else:
            redRightPos = trialPos
    else:
        redRightPos = redRightPos - 1
    if redRightPos == 1 or redRightPos == 5 or redRightPos == 11:
        pass
    else:
        if blackLeftPos == redRightPos:
            blackLeftPos = 1
        if blackRightPos == redRightPos:
            blackRightPos = 1
    hasRedWon()
    changeTurn()


def moveBlackLeft():
    global blackLeftPos
    global redLeftPos
    global redRightPos
    if diceScore < 4:
        trialPos = blackLeftPos + diceScore
        if trialPos > 11:
            blackLeftPos = 11
        else:
            blackLeftPos = trialPos
    else:
        blackLeftPos = blackLeftPos - 1
    if blackLeftPos == 1 or blackLeftPos == 5 or blackLeftPos == 11:
        pass
    else:
        if redLeftPos == blackLeftPos:
            redLeftPos = 1
        if redRightPos == blackLeftPos:
            redRightPos = 1
    hasBlackWon()
    changeTurn()


def moveBlackRight():
    global blackRightPos
    global redLeftPos
    global redRightPos
    if diceScore < 4:
        trialPos = blackRightPos + diceScore
        if trialPos > 11:
            blackRightPos = 11
        else:
            blackRightPos = trialPos
    else:
        blackRightPos = blackRightPos - 1
    if blackRightPos == 1 or blackRightPos == 5 or blackRightPos == 11:
        pass
    else:
        if redLeftPos == blackRightPos:
            redLeftPos = 1
        if redRightPos == blackRightPos:
            redRightPos = 1
    hasBlackWon()
    changeTurn()


def hasRedWon():
    global winner
    global subGo
    global mover
    if redLeftPos == 11 and redRightPos == 11:
        mover = False
        winner = "Red"
        subGo = "Z"


def hasBlackWon():
    global winner
    global subGo
    global mover
    if blackLeftPos == 11 and blackRightPos == 11:
        mover = False
        winner = "Black"
        subGo = "Z"


def changeTurn():
    global turn
    global subGo
    if turn == "Player 1":
        turn = "Player 2"
    else:
        turn = "Player 1"
    subGo = "A"


def rollTheDice():
    global subGo
    global diceScore
    subGo = "B"
    diceScore = random.randint(1, 4)


def createObjects():
    global background
    global backgroundRect
    global board
    global boardRect
    global btnPlayGame
    global btnPlayGameRect
    global btnEnterNames
    global btnEnterNamesRect
    global btnQuitGame
    global btnQuitGameRect
    global DISPLAYSURF
    global myFont
    global diceFont
    global messageFont
    global redCounterLeft
    global redCounterLeftRect
    global redCounterRight
    global redCounterRightRect
    global blackCounterLeft
    global blackCounterLeftRect
    global blackCounterRight
    global blackCounterRightRect
    global btnRollDice
    global btnRollDiceRect
    global btnLeft
    global btnLeftRect
    global btnLeftNo
    global btnRight
    global btnRightNo
    global btnRightRect
    global btnEndGo
    global btnEndGoRect

    background = pygame.image.load("background.png")
    backgroundRect = background.get_rect()

    board = pygame.image.load("board.png")
    boardRect = board.get_rect()
    boardRect.x = 100
    boardRect.y = 100

    redCounterLeft = pygame.image.load("red-counter.png")
    redCounterLeftRect = redCounterLeft.get_rect()

    redCounterRight = pygame.image.load("red-counter.png")
    redCounterRightRect = redCounterRight.get_rect()

    blackCounterLeft = pygame.image.load("black-counter.png")
    blackCounterLeftRect = blackCounterLeft.get_rect()

    blackCounterRight = pygame.image.load("black-counter.png")
    blackCounterRightRect = blackCounterRight.get_rect()

    btnPlayGame = pygame.image.load("play-game-button.png")
    btnPlayGameRect = btnPlayGame.get_rect()
    btnPlayGameRect.x = 200
    btnPlayGameRect.y = 150

    btnEnterNames = pygame.image.load("enter-names-button.png")
    btnEnterNamesRect = btnEnterNames.get_rect()
    btnEnterNamesRect.x = 200
    btnEnterNamesRect.y = 250

    btnQuitGame = pygame.image.load("quit-game-button.png")
    btnQuitGameRect = btnQuitGame.get_rect()
    btnQuitGameRect.x = 200
    btnQuitGameRect.y = 350

    btnRollDice = pygame.image.load("roll-dice.png")
    btnRollDiceRect = btnRollDice.get_rect()
    btnRollDiceRect.x = 450
    btnRollDiceRect.y = 70

    btnRight = pygame.image.load("right.png")
    btnRightNo = pygame.image.load("right-no.png")
    btnRightRect = btnRight.get_rect()
    btnRightRect.x = 520
    btnRightRect.y = 300

    btnLeft = pygame.image.load("left.png")
    btnLeftNo = pygame.image.load("left-no.png")
    btnLeftRect = btnLeft.get_rect()
    btnLeftRect.x = 450
    btnLeftRect.y = 300

    btnEndGo = pygame.image.load("end-turn.png")
    btnEndGoRect = btnEndGo.get_rect()
    btnEndGoRect.x = 450
    btnEndGoRect.y = 300

    DISPLAYSURF = pygame.display.set_mode(background.get_size())
    pygame.display.set_caption("LuBiDaDo")

    messageFont = pygame.font.SysFont("Arial", 20)
    myFont = pygame.font.SysFont("Arial", 30)
    diceFont = pygame.font.SysFont("Arial", 50)


if __name__ == "__main__":
    main()
