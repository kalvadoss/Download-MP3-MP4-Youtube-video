print("---------------------------------------------")
print(" _   __  ___   _     _   _  ___   " )
print("| | / / / _ \ | |   | | | |/ _ \  " )
print("| |/ / / /_\ \| |   | | | / /_\ \ ")
print("|    \ |  _  || |   | | | |  _  |")
print("| |\  \| | | || |___\ \_/ / | | |")
print("\_| \_/\_| |_/\_____/\___/\_| |_/")
print("______ _____   _____ _____       ")
print("|  _  \  _  | /  ___/  ___|      ")
print("| | | | | | | \ `--.\ `--.       ")
print("| | | | | | |  `--. \`--. \      ")
print("| |/ /\ \_/ / /\__/ /\__/ /      ")
print("|___/  \___/  \____/\____/       ")
print("----------------------------------------------")
                            
from pafy import new 
url = input("Youtube link  :")
video = new(url)
print("download Format :: \n press 1 for mp3 \n press 2 for mp4   ")
rep0=input()
if(rep0=='2'):
    stream = video.streams
    j=0
    print("choose your quality : \n  ")
    for i in stream :
        print("press ",j," to download with ",i,"quality ")
        j+=1
    rep =int(input())
    rep2=str(stream[rep])
    print("confirm your choice O/N download with \n",rep2[-4:])
    rep3 =input()
    if(rep3 == 'o'):
        stream[rep].download()
        print("download success")
    else:
        print(" not confirmed  !!!!!  ")
elif(rep0=='1'):
    audio = video.audiostreams
    print("confirm your choice O/N download mp3 \n")
    rep3 =input()
    if(rep3 == 'o'):
        audio[0].download()
        print("download success")
    else:
        print(" not confirmed !!!!  ")
else:
    print("choice not match !!!!")





