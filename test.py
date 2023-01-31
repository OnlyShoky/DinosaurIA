
import pyautogui
import time

import time
print("Start")  # Press Ctrl+F8 to toggle the breakpoint.

start = time.time()
while time.time() - start < 10:  # Hold Key for 5 Seconds
    print("Jump at", str(time.time() - start))  # Press Ctrl+F8 to toggle the breakpoint.
    pyautogui.press('space')
    time.sleep(1)

print("End ")  # Press Ctrl+F8 to toggle the breakpoint.



#im = pyautogui.screenshot('my_screenshot.png',region=(119,162, 130, 30))

gameOver = pyautogui.locateOnScreen('data/GameOver.png', confidence=0.9)
gameOverLetters = pyautogui.locateOnScreen('data/GameOverLetters.png')
dino = pyautogui.locateOnScreen('data/Dino.png')

print(gameOver)
print(gameOverLetters)
#pyautogui.click('data/GameOver.png')

list_gameOverLetters = list(pyautogui.locateAllOnScreen('data/GameOverLetters.png'))
print(list_gameOverLetters)



start = time.time()
test1 = pyautogui.locateOnScreen('data/Dino.png',region=(804,801,100,100), grayscale=True)
print("Time of execution Region .", str(time.time() - start))


start = time.time()
test2 =pyautogui.locateOnScreen('data/Dino.png', grayscale=True)
print("Time of execution .", str(time.time() - start))

for x in range(20):
    dino = pyautogui.locateOnScreen('data/Dino.png', confidence=0.9, grayscale=True)
    cactus = pyautogui.locateOnScreen('data/cactus.png', confidence=0.9, grayscale=True)


    print("Dino pos :", dino)
    print("Cactus pos :", cactus)