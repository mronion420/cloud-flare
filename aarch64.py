import os
os.system("wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm")
os.system("chmod 777 cloudflared-linux-arm")
os.system("mv cloudflared-linux-arm cf")
os.system("rm -rf $PREFIX/bin/cf")
os.system("mv cf $PREFIX/bin/")
os.system("chmod 777 $PREFIX/bin/cf")
os.system("clear")
os.system("figlet Done")
print("Cloud Flare Successfully Installed")
print("Github : https://github.com/mronion420")
print("Telegram : https://t.me/mronion420")
print("Note: To repair run script again")
print("Instalation successful".center(40, "—"))
print ("")
print (" Type: cf --help ")
print ("")
