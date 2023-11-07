import requests
from bs4 import BeautifulSoup
import os

def get_webpage_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def compare_webpage_and_file_content(url, file_path):
    webpage_content = get_webpage_content(url)
    
    if webpage_content is None:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return
    
    with open(file_path, "r") as file:
        file_content = file.read()
    
    if webpage_content == file_content:
        print("Nothing to update.")
    else:
        print("Updating...")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(webpage_content)
        print("Script updated.")

url = "https://raw.githubusercontent.com/plshelpidkwhatimdoing/downloader/main/downloader.py"
downloader = "downloader.py"

print("Checking if script exists")
if os.path.exists(downloader):
    print("Checking for updates")
    compare_webpage_and_file_content(url, downloader)
else:
    newdl = input(f"{downloader} does not exist, please type the name of the script: ")
    
    if newdl:
        downloader = newdl

if not os.path.exists(downloader):
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")
        
        text = soup.get_text()

        with open(downloader, "w", encoding="utf-8") as file:
            file.write(text)

        print("Script downloaded and updated.")
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

input("Press Enter to continue...")
