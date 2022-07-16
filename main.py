import os
os.system("clear")
os.system("apt install wget php -y") 
os.system("pkg install proot -y")
os.system("pkg install proot resolv-conf -y")
os.system("pkg install figlet -y ")
os.system("clear")
os.system("figlet CF-Installer")
print("Easy cloud Flare Installer by Mr. Onion")
print("Github : https://github.com/mronion420")
print("Telegram : https://t.me/mronion420")
print("")
print("Your Device architecture:") 
os.system("uname -m")
print("MAIN MENU".center(50, "—"))
print("1. aarch64")
print("2. arm64")
print("")
print("If device architecture not found hit 1")
print("")
selection = input("Choose Device Architecture [1/2]:")
if selection == "1":
    import aarch64
elif selection == "2":
    import arm64
