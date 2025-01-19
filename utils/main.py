import typer
import os
import socket
import time
import ctypes

app = typer.Typer()

""" TODO
chksum
cp
du
hostname
mkdir
rm
rmdir
wc
whoami
...others
"""
@app.command()
def cat(filename: str):
    with open(filename, "r") as f:
        print(f.read())

@app.command()
def ls():
    cwd = os.getcwd()
    print(f"{cwd}")

@app.command()
def ping(ipaddr: str):
    resp = os.system(f"ping {ipaddr}") #kind of a hack
    print(f"{resp}")

@app.command()
def curl(ipaddr: str):
    resp = os.system(f"curl {ipaddr}") #kind of a hack
    print(f"{resp}")

@app.command()
def grep(pattern: str, file: str):
    resp = "ay I grepped the file for ya. I'm da grep guy"
    #write a real grep function

    print(f"{resp}")

@app.command() #TODO: fix this
def df(): #Displayed fields: Filesystem, 1K-blocks, Used, Available, Use%, Mounted on 
    vols = os.listvolumes()
    for vol in vols:
        print(f"{vol}")
        print(f"{os.listmounts(vol)}")

@app.command()
def hostname():
    print(f"{socket.gethostname()}")

@app.command()
def tail(filename: str, length: int):
    with open(filename, "r") as f:
        print(f.read()[-length:])

@app.command()
def uptime():
    lib = ctypes.windll.kernel32
    t = lib.GetTickCount64()
    t = int(str(t)[:-3])
    
    mins, sec = divmod(t, 60)
    hour, mins = divmod(mins, 60)
    days, hour = divmod(hour, 24)
    
    uptime = f"{days} days, {hour:02}:{mins:02}:{sec:02}"
    currTimeVerbose = time.localtime()
    if currTimeVerbose.tm_sec <=9:
        sec = f"0{currTimeVerbose.tm_sec}"
    else:
        sec = currTimeVerbose.tm_sec

    currTime = f"{currTimeVerbose.tm_hour}:{currTimeVerbose.tm_min}:{sec}"

    print(f"{currTime}, up {uptime}")

@app.command() #accept -c -m and -l args
def wc(filename: str):
    count = 0
    f = open(filename)
    for line in f:
        print(line)
        for word in line.split(" "):
            word.strip('\n')
            if "\n" in word:
                print(f'{word} is not valid, will not increment')
            elif " " in word:
                print(f'{word} is not valid, will not increment')
            else:
                print(f'{word} --> increment 1')
                count = count + 1
            print("|------------------------|\n")
    print(count)

if __name__ == "__main__":
    app()