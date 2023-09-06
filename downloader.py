import subprocess
import os
import re

os.system('cls' if os.name == 'nt' else 'clear')
print("1 - yt-dlp")
print("2 - gallery-dl")
print("3 - aria2c")
print('Use "--aliases" to see command aliases I have added\n')
dl = input("Downloader to use: ")

if dl == "--aliases":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("yt-dlp aliases:\n"
          "-d : --downloader\n"
          "-ws : --write-subs\n"
          "-was : --write-auto-subs\n"
          "\ngallery-dl: aliases:\n"
          "-z : --zip\n"
          "\nno current aliases for aria2c"
          )
    os.system('pause')

elif dl == "1":
    
    os.system('cls' if os.name == 'nt' else 'clear')
    mode = input("Mode: ")
    
    if mode.startswith("-h"):
        run = f"yt-dlp -h"
        subprocess.run(run, shell=True)
        os.system('pause')
    
    elif mode.startswith("-U"):
        run = f"yt-dlp -U"
        subprocess.run(run, shell=True)
        os.system('pause')
    
    elif mode.startswith("-F"):
        url = input("Url: ")
        #print(f"yt-dlp -F {url}")
        run = f"yt-dlp -F {url}"
        subprocess.run(run, shell=True)
        os.system('pause')
    
    elif mode.startswith("-x"):
        audform = input("Audio Format (best (default), aac, alac, flac, m4a, mp3, opus, vorbis, wav): ")
        moreops = input("Additional options: ")
        replacements = { #to make alias' for any other commands just follow the format
            #"shortalias" : "full command"
            "-ws" : "--write-subs",
            "-was" : "--write-auto-subs",
        }
        #make it look for "-d" standalone (things like --dump-settings wont count)
        removeD = r'(^|\s)-d($|\s)'
        
        #function to replace and keep spaces
        def replace_with_spaces(match):
            option = match.group(0)
            replacement = replacements.get(option, option)
            return ' ' + replacement + ' '
        
        #replace and keep spaces (to add another alias (example -zs) just add it like this "|-zs" ex: '(-ws|-was)' -> '(-ws|-was|-zs)')
        moreops = re.sub(r'(-ws|-was)', replace_with_spaces, moreops)
        
        #split input into separate options
        options = moreops.split()
        
        #process each option individually
        for i in range(len(options)):
            if options[i] == '-d':
                options[i] = '--downloader'
        
        #join options back together
        moreops = ' '.join(options)
                
        url = input("Url: ")
    
        if audform.startswith("best"):
            #print(f"yt-dlp -x {moreops} {url}")
            run = f"yt-dlp -x {moreops} {url}"
            subprocess.run(run, shell=True)
            os.system('pause')
        else:
            #print(f"yt-dlp -x --audio-format {audform} {moreops} {url}")
            run = f"yt-dlp -x --audio-format {audform} {moreops} {url}"
            subprocess.run(run, shell=True)
            os.system('pause')
    
    elif mode.startswith("-f"):
        vidform = input("Video format: ")
        moreops = input("Additional options: ")
        replacements = {
            "-ws" : "--write-subs",
            "-was" : "--write-auto-subs",
        }
        removeD = r'(^|\s)-d($|\s)'

        def replace_with_spaces(match):
            option = match.group(0)
            replacement = replacements.get(option, option)
            return ' ' + replacement + ' '
        
        moreops = re.sub(r'(-ws|-was)', replace_with_spaces, moreops)

        options = moreops.split()
        for i in range(len(options)):
            if options[i] == '-d':
                options[i] = '--downloader'
        
        moreops = ' '.join(options)
        
        url = input("Url: ")
        #print(f"yt-dlp -f {vidform} {moreops} {url}")
        run = f"yt-dlp -f {vidform} {moreops} {url}"
        subprocess.run(run, shell=True)
        os.system('pause')

elif dl == "2":
    os.system('cls' if os.name == 'nt' else 'clear')
    mode = input("Commands (not required): ")

    if mode.startswith("-h"):
        run = f"gallery-dl -h"
        subprocess.run(run, shell=True)
        os.system('pause')
        
    pattern = r'(^|\s)-z($|\s)'

    def replace_with_spaces(match):
        option = match.group(0)
        return ' --zip ' if option.strip() == '-z' else option
    mode = re.sub(pattern, replace_with_spaces, mode)

    url = input("Url: ")

    #print(f"gallery-dl {mode} {url}")
    run = f"gallery-dl {mode} {url}"
    subprocess.run(run, shell=True)
    os.system('pause')

elif dl == "3": #add aria2c
    os.system('cls' if os.name == 'nt' else 'clear')
    ariaoptions = input("Options for aria2c: ")
    url = input("Url: ")
    print(f"aria2c {ariaoptions} {url}")
    run = f"aria2c {ariaoptions} {url}"
    subprocess.run(run, shell=True)
    os.system('pause')