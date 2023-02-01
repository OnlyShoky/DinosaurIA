from IATools import *
import time
import pyautogui


def get_ROI():
    """This function returns the region of interest"""

    dino = pyautogui.locateOnScreen('data/Dino.png')
    score = pyautogui.locateOnScreen('data/score0.png',confidence = 0.9)

    x= dino[0]
    y= dino[1]
    width = (score[0]+score[2]) - dino[0]
    heigth = dino[3]

    region = (x,y,width,heigth)

    return region

def calcul_distance(first_object,second_object):
    """This function returns the distance of two objects"""
    position_FO = pyautogui.center(first_object)
    position_SO = pyautogui.center(second_object)

    return position_SO.x - position_FO.x

def getLineOfpixels(im, xy, width):
    """
    Returns the lists of pixels values at a given position.

    :param xy: The coordinate, given as (x, y). See
       :ref:`coordinate-system`.
    :returns: The pixel value.  If the image is a multi-layer image,
       this method returns a tuple.
    """

    listsPixels = []

    for i in range(width):
        listsPixels.append(im.getpixel( (xy[0]+i,xy[1]) ))

    return listsPixels

def detectTypeOfObject(listLow,listHigh):
    blackZoneLow = False
    blackZoneHigh = False

    whitePixel = (255,255,255)

    nbBulks = 0
    nbCactus = 0
    for i in range(listLow.__len__()):

        if(listLow[i] != whitePixel and blackZoneLow != True):
            blackZoneLow = True

        if (listHigh[i] != whitePixel and blackZoneHigh != True):
            blackZoneHigh = True

        if(listLow[i] == whitePixel and blackZoneLow == True):
            blackZoneLow = False
            if(blackZoneHigh!= True):
                nbBulks = nbBulks +1
            else:
                nbCactus = nbCactus + 1

        if (listHigh[i] == whitePixel and blackZoneHigh == True and blackZoneLow == False):
            blackZoneHigh = False

    return round(nbBulks/2),nbCactus



def stateMachine_Detections():
    print("detection state machine")
    sensorLow = pyautogui.position(x=1627, y=870)
    sensorHigh = pyautogui.position(x=1627, y=848)

    width = 700

    while(1):

        im = pyautogui.screenshot()

        l_pxSensorLow = getLineOfpixels(im,(sensorLow[0] - width , sensorLow[1]) , width)
        l_pxSensorHigh = getLineOfpixels(im,(sensorHigh[0] - width , sensorHigh[1]) , width)

        nbBulks,nbCactus = detectTypeOfObject(l_pxSensorLow,l_pxSensorHigh)

        print("Number of bulks = "+ str(nbBulks) +" Number of Cactus = "  + str(nbCactus))


def update(region,state):

    while(1):

        #First state game not launched yet
        if(state == -1):
            print("Start of the game ! ")
            state = 0
            dino = pyautogui.locateOnScreen('data/Dino.png', confidence=0.8, grayscale=True,region=region)
            score = pyautogui.locateOnScreen('data/score0.png', confidence=0.9)
            detector = (pyautogui.center(score)[0], pyautogui.center(dino)[1])
            print(dino)


        if(state == 0):
            print("First jump : GO !")
            action(state,dino)
            state = 1

        if(state == 1):
            print("Searching new pos of Dino on movement")
            cactus = pyautogui.locateOnScreen('data/cactus.png', confidence=0.5, grayscale=True,region=region)
            dino = pyautogui.locateOnScreen('data/Dino.png', confidence=0.9, grayscale=True,region=region)
            if(cactus != None ):
                print("Waiting first cactus")
                state = 2

        if (state == 3):
            im = pyautogui.screenshot(region = (detector[0],detector[1],1,1))
            px = im.getpixel((0, 0))
            if (px != (255, 255, 255)):
                print("First cactus detected")
                state = 2

        if (state == 2):
            list_cactus = list(pyautogui.locateAllOnScreen('data/cactus.png', confidence=0.97, grayscale=True))
            nb_cactus = list_cactus.__len__()

            distance_D_C = calcul_distance(dino,list_cactus[0])
            print("Game started !")
            print("Info : Nb Cactus = "+ nb_cactus + " Distance Dino Cactus = " + distance_D_C )
            time.sleep(1)

    return state






def action(state,object):

    if(state ==0):
        if(object!=None):
            pyautogui.click(object[0], object[1])
            print("Jump at", str(time.time()))  # Press Ctrl+F8 to toggle the breakpoint.
            pyautogui.press('space')






