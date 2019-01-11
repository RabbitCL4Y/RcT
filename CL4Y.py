#!/usr/bin/python
#Author : MR.CL4Y
#Contact : 085752481601
import random
import sys
import time
import os,sys
blue = '\033[34;1m'
green = '\033[32;1m'
purple = '\033[35;1m'
cyan = '\033[36;1m'
red = '\033[31;1m'
white = '\033[37;1m'
yellow = '\033[33;1m'
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
mengetik('WELCOME IN MY TOOLS..')
mengetik('.')
mengetik('.')
mengetik('menghubungi MR.CL4Y..')
mengetik ('Please Wait !!')
mengetik ('WELCOME..!!')
mengetik ('kalo gak Tau Username Sama Password Bisa pm = 085752481601')
print
print ("\033[1;32mMasukan UserName&Password")
username = 'MR.CL4Y'
password = 'RcT'

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():
        uname = raw_input("username : ")
        if uname == username:
                pwd = raw_input("password : ")

                if pwd == password:

			os.system('clear')
                else:
                        print "\n\033[1;36mSorry Invalid password !!!\033[00m"
                        print "Back Login\n"
                        restart()

        else:
                print "\n\033[1;36mSorry Invalid Username !!!\033[00m"
                print "Back Login\n"
                restart()

try:
        main()
except KeyboardInterrupt:
        os.system('clear')
        restart()
os.system(" figlet -f slant MR.CL4Y |lolcat")
print(green),"###############################################"
time.sleep(0.23)
print(red),"###############################################"
time.sleep(0.23)
print(cyan),"Author         : MR.CL4Y"
print(purple),"Github       : https://github.com/RabbitCL4Y"
print(red),"Contact         : RabbitCL4Y123@gmail.com"
print(yellow),"Team         : Rabbit Cyber Team"
print(blue),"Team           : 2Easy4Hack Team"
print(green),"###############################################"
time.sleep(0.23)
print(red),"################################################"
print "\033[93mMenu Pilihan"
print '1.)install-MR_CL4Y-Tool'
print '2.)instal-MR-CL4Y'
print '3.)install-Spam-SmS'
print '4.)install-Spam-Whatsapp'
print '5.)install-DDos-MR.CL4Y'
print '6.)install-Tools CL4Yv5'
print '7.)install-brute-webdav-RcT-v2'
print '8.)install-OSIF'
print '9.)install-sqlmap'
print '10.)install-ipcs'
print '0.)Exit'
print(yellow),("[+]------------------------------------------------[-]")
print(green)," Created by  :  ",(blue),"MR.CL4Y"
print(green)," Since       :",(white),"11 januari 2019"
print(green)," Support     :",(yellow),"All Memb Rabbit Cyber Team"
print(green)," Team Cyber  :",(red),"Rabbit Cyber Team"
print(yellow),("[+]------------------------------------------------[-]")
MRCL4Y = input("\033[1;91mPilih \033[1;37m=> ")

if MRCL4Y==1:
    os.system ('clear')
    os.system ('figlet -f future MR.CL4Y |lolcat')
    os.system ('pkg update && pkg upgrade')
    os.system ('pkg install git')
    os.system ('pkg install python2')
    os.system ('pkg install ruby')
    os.system ('pkg install figlet')
    os.system ('gem install lolcat')
    os.system ('pip2 install lolcat')
    os.system ('pip2 install --upgrade pip')
    os.system ('git clone https://github.com/RabbitCL4Y/MR_CL4Y-Tools')
    os.chdir('MR_CL4Y-Tools')
    os.system ('clear')
    os.system ('sh MR_CL4Y-Tools.sh')

if MRCL4Y==2:
   os.system ('clear')
   os.system ('figlet -f future MR.CL4Y |lolcat')
   os.system ('pkg update && pkg upgrade')
   os.system ('pkg install git')
   os.system ('pkg install python2')
   os.system ('pkg install ruby')
   os.system ('pkg install figlet')
   os.system ('gem install lolcat')
   os.system ('pip2 install lolcat')
   os.system ('pip2 install --upgrade pip')
   os.system ('git clone https://github.com/RabbitCL4Y/MR-CL4Y')
   os.chdir ('MR-CL4Y')
   os.system ('clear')
   os.system ('sh MR-CL4Y.sh')

if MRCL4Y==3:
   os.system ('clear')
   os.system ('figlet -f future MR.CL4Y |lolcat')
   os.system ('pkg update && pkg upgrade')
   os.system ('pkg install git')
   os.system ('pkg install python2')
   os.system ('pkg install ruby')
   os.system ('pkg install figlet')
   os.system ('gem install lolcat')
   os.system ('pip2 install lolcat')
   os.system ('pkg install php')
   os.system ('pip2 install --upgrade pip')
   os.system ('git clone https://github.com/RabbitCL4Y/SmS-Spam')
   os.chdir ('SmS-Spam')
   os.system ('clear')
   os.system ('php SmS.php')


if MRCL4Y==4:
   os.system ('clear')
   os.system ('figlet -f future MR.CL4Y |lolcat')
   os.system ('pkg update && pkg upgrade')
   os.system ('pkg install git')
   os.system ('pkg install php')
   os.system ('git clone https://github.com/RabbitCL4Y/RCTSpammer')
   os.chdir ('RCTSpammer')
   os.system ('clear')
   os.system ('php RCTspammer.php')

if MRCL4Y==5:
   os.system ('clear')
   os.system ('figlet -f future MR.CL4Y |lolcat')
   os.system ('pkg update && pkg upgrade')
   os.system ('pkg install git')
   os.system ('pkg install python2')
   os.system ('git clone https://github.com/RabbitCL4Y/CL4y-DDoS')
   os.chdir ('Cl4y-DDoS')
   os.system ('clear')
   os.system ('python2 CL4y-DDoS.py')

if MRCL4Y==6:
   os.system ('clear')
   os.system ('figlet -f future MR.CL4Y |lolcat')
   os.system ('pkg update && pkg upgrade')
   os.system ('pkg install git')
   os.system ('pkg install python2')
   os.system ('pkg install ruby')
   os.system ('pkg install figlet')
   os.system ('gem install lolcat')
   os.system ('pip2 install lolcat')
   os.system ('pip2 install --upgrade pip')
   os.system ('git clone https://github.com/RabbitCL4Y/CL4Yv5')
   os.chdir ('CL4Yv5')
   os.system ('clear')
   os.system ('sh CL4Y-v5.sh')

if MRCL4Y==7:
   os.system ('clear')
   os.system ('figlet -f future MR.CL4Y |lolcat')
   os.system ('pkg update && pkg upgrade')
   os.system ('pkg install git')
   os.system ('pkg install curl')
   os.system ('pkg install python2')
   os.system ('pkg install ruby')
   os.system ('pkg install figlet')
   os.system ('gem install lolcat')
   os.system ('pip2 install lolcat')
   os.system ('pip2 install --upgrade pip')
   os.system ('git clone https://github.com/RabbitCL4Y/brute-webdav')
   os.chdir ('brute-webdav')
   os.system ('clear')
   os.system ('sh Brute-webdav-RcT.sh')

if MRCL4Y==8:
   os.system ('clear')
   os.system ('figlet -f future MR.CL4Y |lolcat')
   os.system ('apt update && apt upgrade')
   os.system ('pip2 install --upgrade pip')
   os.system ('pip2 install requests mechanize')
   os.system ('git clone https://github.com/CiKu370/OSIF')
   os.chdir ('OSIF')
   os.system ('pip2 install -r requirements.txt')
   os.system ('clear')
   print(red),('ketik token (untuk login fb)')
   time.sleep(1.0)
   print(red),('ketik help (untuk melihat bantuan)')
   time.sleep(1.5)

if MRCL4Y==9:
   os.system ('clear')
   os.system ('figlet -f future MR.CL4Y |lolcat')
   os.system ('apt update && apt upgrade')
   os.system ('git clone https://github.com/sqlmapproject/sqlmap.git')
   os.chdir ('sqlmap')
   os.system ('chmod +x sqlmap.py && chmod +x sqlmap.py')
   os.system ('clear')
   print(blue),('jalankan dg perintah:')
   time.sleep (1.7)
   print(blue),('cd sqlmap')
   print(blue),('python2 sqlmap.py -u <web vuln>')

if MRCL4Y==10:
    os.system ('clear')
    os.system ('figlet -f future MR.CL4Y |lolcat')
    os.system ('apt update && apt upgrade')
    os.system ('pip2 install requests')
    os.system ('git clone https://github.com/kancotdiq/ipcs')
    os.chdir ('ipcs')
    os.system ('clear')
    os.system ('python2 scan.py')

if MRCL4Y==0:
   time.sleep(0.5)
mengetik ('Terima Kasih Sudah Memakai Tools Saya')
mengetik ('Jangan Lupa Follow Github,instagram,and Youtube')
mengetik ('My Github : https://github.com/RabbitCL4Y')
mengetik ('My Instagram : https://www.instagram.com/muhammadrafli_337')
mengetik ('Youtube Team : Rabbit Cyber Team')
mengetik ("ScriptKiddies")
