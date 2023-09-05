import subprocess
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("1 - yt-dl")
print("2 - gallery-dl")
print("3 - aria2c\n")
dl = input("Downloader to use: ")

if dl == "1":
    os.system('cls' if os.name == 'nt' else 'clear')
    mode = input("Mode: ")
    
    if mode.startswith("-F"):
        url = input("Url: ")
        #print(f"yt-dlp -F {url}")
        run = f"yt-dlp -F {url}"
        subprocess.run(run, shell=True)
        os.system('pause')
    elif mode.startswith("-x"):
        audform = input("Audio Format (best (default), aac, alac, flac, m4a, mp3, opus, vorbis, wav): ")
        if audform.startswith("best"):
            url = input("url: ")
            #print(f"yt-dlp -x {url}")
            run = f"yt-dlp -x {url}"
            subprocess.run(run, shell=True)
            os.system('pause')
        else:
            moreops = input("Additional options: ")
            url = input("Url: ")
            if "-d" in moreops:
                addaria = "--downloader aria2c"
            else:
                addaria = ""
            print(f"yt-dlp -x --audio-format {audform} {addaria} {url}")
            #run = f"yt-dlp -x --audio-format {audform} {addaria} {url}"
            #subprocess.run(run, shell=True)
            os.system('pause')
    elif mode.startswith("-f"):
        vidform = input("Video format: ")
        moreops = input("Additional options: ") #make it remove -d if inputted
        if "-d" in moreops:
            addaria = "--downloader aria2c"
        else:
            addaria = ""
        if "-wt" in moreops:
            addthumb = "--write-thumbnail"
        else:
            addthumb = ""
        url = input("Url: ")
        print(f"yt-dlp -f {vidform} {addaria} {addthumb} {moreops} {url}")
        #run = f"yt-dlp -f {vidform} {addaria} {url}"
        #subprocess.run(run, shell=True)
