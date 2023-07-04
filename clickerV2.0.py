import pyautogui, time
pyautogui.PAUSE = 0.0001 #this brokes program

time.sleep(5)
win = 0
lose = 0
startingTime = overallTime = time.time()

enter_battle = pyautogui.position()
print(enter_battle)
for i in range(6000):
    #pyautogui.leftClick(x=1048, y=591)  # enter_battle sim
    pyautogui.leftClick(x=1077, y=591)  # enter_battle jugg
	
    time.sleep(1) #64
    startingTime = time.time()
    while 1: #123
        
        pyautogui.leftClick(x=849, y=445)  # side
        pyautogui.leftClick(x=1197, y=445)# robot
        pyautogui.leftClick(pyautogui.locateOnScreen('rain.png', confidence = 0.80))#skill
        pyautogui.leftClick(x=998, y=445)#aux
        pyautogui.leftClick(x=1300, y=445)#core
        pyautogui.leftClick(x=1021, y=476)#drop
        if(pyautogui.locateOnScreen('exitV1.png') is not None ): # region = (1100,295,100,50)
            win = win + 1
            break
        if(pyautogui.locateOnScreen('exitV2.png') is not None ): # region = (1100,295,100,50)
            win = win + 1
            break
        if(pyautogui.locateOnScreen('exitV3.png') is not None ): # region = (1100,295,100,50)
            win = win + 1
            break
        if(pyautogui.locateOnScreen('exitV4.png') is not None ): # region = (1100,295,100,50)
            win = win + 1
            break
        if(pyautogui.locateOnScreen('exitL1.png') is not None ): # region = (1100,295,100,50)
            lose = lose + 1
            break
        if(pyautogui.locateOnScreen('exitL2.png') is not None ): # region = (1100,295,100,50)
            lose = lose + 1
            break
        if(pyautogui.locateOnScreen('exitL3.png') is not None ): # region = (1100,295,100,50)
            lose = lose + 1
            break
        
    endofbattleTime = time.time()

    for j in range(205, 531, 20):    # y coordinates
        for k in range(700, 1345, 20):
            
            pyautogui.leftClick(x=k, y=j, interval=0)  # end battle
            if(j+160 <= 531):
                pyautogui.leftClick(x=k, y=j+160, interval=0)  # end battle
        if(pyautogui.locateOnScreen('pen.png', confidence = 0.80) is not None ): # region = (1100,295,100,50)
            break
    newTime = time.time()
    endofbattleTime = newTime-endofbattleTime
    time.sleep(5)
    print("\nwins: ",win,"\t","loses: ",lose,"\n","Last Battle Time: ",newTime-startingTime, "\n", "Per hour wins with this time: ", 3600/(newTime - startingTime), "win(s)\n", "End of Battle Time: ",endofbattleTime)
	