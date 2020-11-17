import time
import io
bestand = open("kaboem.txt", "r")
inhoud = bestand.read()
countDown = 1000
while (countDown >= 0):
    print(countDown)
    countDown = countDown - 1
    time.sleep(0.0)
    if countDown == 0:
        print("KABOEM!!")
        print(inhoud)
        break
    
        
