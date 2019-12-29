#!/usr/bin/python

def openJson(file):
    with open(file, 'r') as myfile:
        datafile=myfile.read()
    global data
    data = json.loads(datafile)

def main():
    for file in os.listdir("input"):
        print "\n[*] Opening " + file
        inFile = "input/" + file
        openJson(inFile)

        outFile = "output/" + file[:-5] + ".txt"
        o = open(outFile, 'w')

        for video in data:
            id = video["contentDetails"]["videoId"]
            o.write("https://www.youtube.com/watch?v=" + id + "\n")
        print "[+] " + file + " Complete!"

    
    openJson("subs.json")
    outFile = "subs.txt"
    print "\n[*] Opening subs.json"
    o = open(outFile, 'w')

    for channel in data:
        id = channel["snippet"]["resourceId"]["channelId"]
        o.write("https://www.youtube.com/channel/" + id + "\n")
    print "[+] subs.json Complete!"
    print "\n"

if __name__ == "__main__":
    import os
    import json
    main()
