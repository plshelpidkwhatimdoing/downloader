while True:
    import subprocess
    import os
    import re
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""1 - yt-dlp
2 - gallery-dl
3 - aria2c
4 - update script
Use "-h" to see command aliases I have added\n""")
    dl = input("Downloader to use: ")
    
    if dl == "-h":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""The "-h/--help" command works with all three, just enter that at the first prompt
    
yt-dlp aliases:
-d : --downloader
-ws : --write-subs
-was : --write-auto-subs
-sd : --skip-download
"-nd" : --no-download
"-ec" : --embed-chapters
"-ac" : --add-chapters
"-wc" : --write-comments

gallery-dl: aliases:
-z : --zip
    
aria2c aliases:
-fan : --file-allocation=none
-fa= : --file-allocation= (just enter your preferred method without a space, ex: -fa=prealloc)\n""")
        input("Press Enter to continue...")
    
    elif dl == "1":
        
        os.system('cls' if os.name == 'nt' else 'clear')
        mode = input("Mode (type 'modhelp' if not sure what this means): ")
        
        if mode.startswith("-h") or mode == "--help":
            run = f"yt-dlp -h"
            subprocess.run(run, shell=True)
            input("Press Enter to continue...")
        
        if mode == "modhelp":
            print("""This is where you would put the first argument like "-F" or "-U"
here is a list of everything supported here so far:
    
-h (show help)
-U (update yt-dlp)
-F (possible formats, recommend using this before -f)
-x (download audio)
-f (format, enter format at next prompt)
alt, other, options (run anything else not shown here)""")
            input("Press Enter to continue...")
        
        if mode.startswith("-U") or mode == "--update":
            run = f"yt-dlp -U"
            subprocess.run(run, shell=True)
            input("Press Enter to continue...")
        
        elif mode.startswith("-F") or mode == "--list-formats":
            moreops = input("Additional Options: ")
            url = input("Url: ")
            #print(f"yt-dlp -F {url}")
            run = f"yt-dlp -F {moreops} {url}"
            subprocess.run(run, shell=True)
            input("Press Enter to continue...")
        
        elif mode.startswith("-x") or mode == "--extract-audio":
            audform = input("Audio Format (best (default), aac, alac, flac, m4a, mp3, opus, vorbis, wav): ")
            moreops = input("Additional options: ")
            replacements = { #to make alias' for any other commands just follow the format
                #"shortalias" : "full command"
                "-ws" : "--write-subs",
                "-was" : "--write-auto-subs",
                "-sd" : "--skip-download",
                "-nd" : "--no-download",
                "-ec" : "--embed-chapters",
                "-ac" : "--add-chapters",
                "-wc" : "--write-comments"
            }
            #make it look for "-d" standalone (things like --dump-settings wont count)
            removeD = r'(^|\s)-d($|\s)'
            
            #function to replace and keep spaces
            def replace_with_spaces(match):
                option = match.group(0)
                replacement = replacements.get(option, option)
                return ' ' + replacement + ' '
            
            #replace and keep spaces (to add another alias (example -zs) just add it like this "|-zs" ex: '(-ws|-was)' -> '(-ws|-was|-zs)')
            moreops = re.sub(r'(-ws|-was|-sd|-nd|-ec|-ac|-wc)', replace_with_spaces, moreops)
            
            #split input into separate options
            options = moreops.split()
            
            #process -d individually
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
                input("Press Enter to continue...")
            else:
                #print(f"yt-dlp -x --audio-format {audform} {moreops} {url}")
                run = f"yt-dlp -x --audio-format {audform} {moreops} {url}"
                subprocess.run(run, shell=True)
                input("Press Enter to continue...")
        
        elif mode.startswith("-f"):
            vidform = input("Video format: ")
            moreops = input("Additional options: ")
            replacements = {
                "-ws" : "--write-subs",
                "-was" : "--write-auto-subs",
                "-sd" : "--skip-download",
                "-nd" : "--no-download",
                "-ec" : "--embed-chapters",
                "-ac" : "--add-chapters",
                "-wc" : "--write-comments"
            }
            removeD = r'(^|\s)-d($|\s)'
    
            def replace_with_spaces(match):
                option = match.group(0)
                replacement = replacements.get(option, option)
                return ' ' + replacement + ' '
            
            moreops = re.sub(r'(-ws|-was|-sd|-nd|-ec|-ac|-wc)', replace_with_spaces, moreops)
    
            options = moreops.split()
            for i in range(len(options)):
                if options[i] == '-d':
                    options[i] = '--downloader'
            
            moreops = ' '.join(options)
            
            url = input("Url: ")
            #print(f"yt-dlp -f {vidform} {moreops} {url}")
            run = f"yt-dlp -f {vidform} {moreops} {url}"
            subprocess.run(run, shell=True)
            input("Press Enter to continue...")
        
        elif mode == "alt" or mode == "other" or mode == "options":
            options = input("Custom options: ")
            
            replacements = {
                "-ws" : "--write-subs",
                "-was" : "--write-auto-subs",
                "-sd" : "--skip-download",
                "-nd" : "--no-download",
                "-ec" : "--embed-chapters",
                "-ac" : "--add-chapters",
                "-wc" : "--write-comments"
            }
            removeD = r'(^|\s)-d($|\s)'
    
            def replace_with_spaces(match):
                option = match.group(0)
                replacement = replacements.get(option, option)
                return ' ' + replacement + ' '
            
            options = re.sub(r'(-ws|-was|-sd|-nd|-ec|-ac|-wc)', replace_with_spaces, options)
    
            options = options.split()
            for i in range(len(options)):
                if options[i] == '-d':
                    options[i] = '--downloader'
            
            options = ' '.join(options)
            
            url = input("Url: ")
            #print(f"yt-dlp {options} {url}")
            run = f"yt-dlp {options} {url}"
            subprocess.run(run, shell=True)
            input("Press Enter to continue...")            
    
    elif dl == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        mode = input("Commands (not required): ")
    
        if mode.startswith("-h") or mode == "--help":
            run = f"gallery-dl -h"
            subprocess.run(run, shell=True)
            input("Press Enter to continue...")
        
        else:
            
            pattern = r'(^|\s)-z($|\s)'
    
            def replace_with_spaces(match):
                option = match.group(0)
                return ' --zip ' if option.strip() == '-z' else option
            mode = re.sub(pattern, replace_with_spaces, mode)
    
            url = input("Url: ")
    
            #print(f"gallery-dl {mode} {url}")
            run = f"gallery-dl {mode} {url}"
            subprocess.run(run, shell=True)
            input("Press Enter to continue...")
    
    elif dl == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        mode = input("Options for aria2c (not required): ")
        
        if mode.startswith("-h") or mode == "--help":
            run = f"aria2c -h"
            subprocess.run(run, shell=True)
            input("Press Enter to continue...")
        
        else:
            
            url = input("""Url ("" are not added to the url, so add them if need be): """)
            replacements = {
                "-fan" : "--file-allocation=none",
                "-fa=" : "--file-allocation="
                }
            
            def replace_with_spaces(match):
                option = match.group(0)
                replacement = replacements.get(option, option)
                if option == "-fa=":
                    return replacement
                else:
                    return ' ' + replacement + ' '
            
            mode = re.sub(r'(-fan|-fa=)', replace_with_spaces, mode)
            
            options = mode.split()
            
            mode = ' '.join(options)

        #print(f"aria2c {mode} {url}")
        run = f"aria2c {mode} {url}"
        subprocess.run(run, shell=True)
        input("Press Enter to continue...")
    
    elif dl == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        subprocess.call(['python', "update.py"], shell=True)
