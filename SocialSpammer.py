import pyautogui
from time import sleep

intro = """
 ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝                                                        
                         By Daniewskyy

"""

print(intro)

text = input("Wiadomość którą chcesz spamić: ")

time = 0
while time !=5:
    time +=1
    sleep(1)
    print("Uruchamianie za:  " + str(time))
def spam(msg, maxMsg):
    count = 0
    while count !=maxMsg:
        count += 1
        print("Wyslano wiadomość - " + str(count))
        pyautogui.write(msg)
        pyautogui.press("enter")
    
spam(text, 250)

print("===========================")
print("Spam zakończony")

input()
print()
