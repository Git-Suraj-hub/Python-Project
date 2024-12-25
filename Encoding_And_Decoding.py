import random
import string
from colorama import Fore, Back, Style,init

init(autoreset = True)
while True:


    print(Fore.BLACK + "Create a New Password: ")
    Password1 = input()

    print(Fore.BLACK + "Enter Again Your Password: ")
    Password2 = input()

    if Password1 == Password2:
        print(Fore.GREEN + "Password Successfully Created ")
        break
    else:
        print( Fore.CYAN      +"Your Password Is Not Same A Older \n please Try again ")
a = input(Fore.LIGHTBLUE_EX + "Write Your Message : ")
words = a.split()
while True:
    if len(words)<=1 and len(words[0])<=1:
        print(Fore.MAGENTA + "Your Message Is Very Short \n write again message")
        a = input(Fore.LIGHTWHITE_EX + "Enter Again Message : " )
        words = a.split()
    else:
        print(Fore.GREEN + "Your Message Accepted ")
        break


for i in range(len(words)):
    if len(words[i])<=2:
        words[i] = words[i][::-1]
a = ' '.join(words)
for i in range (len(words)):
    if len(words[i])>2:
        words[i] = words[i][-1:] + words[i][0:len(words[i])-1]
        words[i] = words[i][::-1]

        words[i] = ''.join(random.choices(string.ascii_letters,
                            k=3)) + words[i] + ''.join(random.choices(string.ascii_letters,
                            k=3))

a=' '.join(words)
print(f"Your Message Is after a encrypted  : {a}")



# decoding 

count=0;
while True:
    passw = input(Fore.LIGHTWHITE_EX + "Enter a Password : ")
    if(passw==Password2):
        print(Fore.LIGHTGREEN_EX+"Message Unlocked")
        for i in range(len(words)):
            if len(words[i])<=2:
                words[i] = words[i][::-1]
        a=' '.join(words)

        for i in range(len(words)):
            if len(words[i])>2:
                words[i] = words[i][3:-3]
                words[i] = words[i][::-1]
                words[i] = words[i][1:] + words[i][0]
        a=" ".join(words);
        print(Fore.LIGHTMAGENTA_EX + f"after the decrypt your message : {a}")
        break
    else:
        print(Fore.RED + "Password Incorrect Please Type Again")
        count+=1
        if count==5:
            print(Fore.MAGENTA + "you Entered 5 times Password Incoorect then wait 5 Sec")
            import time
            print(Fore.LIGHTBLACK_EX + "Timer starts now:")
            for i in range(5, 0, -1):
                print(f"{i} seconds remaining")
                time.sleep(1)
            print(Fore.YELLOW + "TRY AGAIN !")
            count=0
print(Fore.LIGHTCYAN_EX + "Thanks For Using Encoding Service !!!!!!")

