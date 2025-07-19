from time import sleep
import os
import subprocess
import sys
import shutil
import getpass
from pystyle import Colors, Colorate, Center
from colorama import init, Fore
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import time
import threading
import base64
import re
import webbrowser
import random
import string
import nmap


init(autoreset=True) 

os.system('cls' if os.name == 'nt' else 'clear') 
os.system(                        '               title                                      Moon Tool             ' if os.name == 'nt' else '')  

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

banner = '''
                                          
                            .-""""-                                   
                           F   .-'                                    
                          F   J                                       
                         I    I                                       
                          L   `.                                      
                           L    `-._,                                 
                                                     `-.__.-'                                                           
'''

menu_text = '''
                         
                   ┌────────────────────────┐
                   │ ┌────────────────────┐ │
                   │ │Welcome To Moon Tool│ │
                 ┌─│ └────────────────────┘ │─┐
              ┌──└─└────────────────────────┘─┘──┐              
              │                                  │
       ┌──────│        »Tool Made by zocvz        │─────┐
      ┌│      │        »Discord https://discord.gg/Avdxh98Cth         │     │┐
   ┌──└└──────│           │─────┘┘───┐
┌──└──────────┘─────────────────┐────────────────┘──────────┘──┐
│[   1   ]» Discord Spammer     │[   5   ]» Online User Lookup │
│[   2   ]» Port scanning       │[   6   ]» Coordinates Lookup │       
│[   3   ]» Geo ip lookup       │[   7   ]» Rare Usernames     │
│[   4   ]» Id to token         │[   8   ]» Doxing tools       │
└───────────────────────────────┘──────────────────────────────┘

         
                 

'''



def print_banner(banner):
    lines = banner.splitlines()
    colored_lines = [Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(line)) for line in lines]
    for line in colored_lines:
        print(line)
        sleep(0.10)

def print_menu():
    line = Colorate.Vertical(Colors.green_to_blue, Center.XCenter(menu_text))
    print(line)


def display_ascii_logo():
    logo = '''
███╗   ███╗ ██████╗  ██████╗ ███╗   ██╗    ████████╗ ██████╗  ██████╗ ██╗     
████╗ ████║██╔═══██╗██╔═══██╗████╗  ██║    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██╔████╔██║██║   ██║██║   ██║██╔██╗ ██║       ██║   ██║   ██║██║   ██║██║     
██║╚██╔╝██║██║   ██║██║   ██║██║╚██╗██║       ██║   ██║   ██║██║   ██║██║     
██║ ╚═╝ ██║╚██████╔╝╚██████╔╝██║ ╚████║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝     ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                              
    '''
    colored_logo = Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(logo))
    print(colored_logo)

def page2():
    while True:
        clear_screen()
        display_ascii_logo()
        
        menu_text = '''
                   ┌────────────────────────┐
                   │ ┌────────────────────┐ │
                   │ │       Page 2       │ │
                 ┌─│ └────────────────────┘ │─┐
              ┌──└─└────────────────────────┘─┘──┐              
              │                                  │
       ┌──────│        »Tool Made by wock        │─────┐
      ┌│      │        »Discord wock0503         │     │┐
   ┌──└└──────│        »Server .gg/Q2HbQKZXMM    │─────┘┘───┐
┌──└──────────┘─────────────────┐────────────────┘──────────┘──┐
│[   9   ]» Doxing ip           │[   13  ]»                    │
│[   10  ]» Doxing a name       │[   14  ]»                    │       
│[   11  ]» Dox tools           │[   15  ]»                    │
│[   12  ]» Doxin email         │[   0   ]» Back to main menu  │
└───────────────────────────────┘──────────────────────────────┘
        '''

        colored_menu_text = Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu_text))
        print(colored_menu_text)

        choice = input(Colorate.Horizontal(Colors.green_to_blue, "[<>] "))

        if choice == "0":
            break  
        elif choice == "9":
            option9()
        elif choice == "10":
            option10()
        elif choice == "11":
            option11()
        elif choice == "12":
            option12()
            input("\nPress Enter to return to the menu...")  
        else:
            print("Invalid")


def option1():
    clear_screen()  
    

    banner = """
  ┌───────────────────────────────────────────────────────┐                                                          
  │  ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗  │    
  │  ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗ │    
  │  ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║ │    
  │  ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║ │    
  │  ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝ │    
  │  ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝  │     
┌─┘───────────────────────────────────────────────────────┘─────────┐                                                             
│  ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗    │
│  ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗   │
│  ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝   │
│  ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗   │
│  ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║   │
│  ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝   │
└───────────────────────────────────────────────────────────────────┘                                                              
    """

    print(Colorate.Vertical(Colors.green_to_blue, Center.XCenter(banner)))

    token = input('Enter Token: ')
    channel_id = input('Enter Channel ID: ')
    message_content = input('Enter Message: ')
    repeat_count = int(input('Enter Repeat Count (How many times): '))

    def spammer():
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
        headers = {'Authorization': token}
        payload = {'content': message_content}

        for _ in range(repeat_count):
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 204:
                print(f'Message sent successfully!')
            else:
                print(f'Failed to send message. Status code: {response.status_code}')

    thread = threading.Thread(target=spammer)
    thread.start()
    thread.join()

def option2():
    clear_screen()

    header = '''
██████   ██████  ██████  ████████     ███████  ██████  █████  ███    ██ ███    ██ ██ ███    ██  ██████  
██   ██ ██    ██ ██   ██    ██        ██      ██      ██   ██ ████   ██ ████   ██ ██ ████   ██ ██       
██████  ██    ██ ██████     ██        ███████ ██      ███████ ██ ██  ██ ██ ██  ██ ██ ██ ██  ██ ██   ███ 
██      ██    ██ ██   ██    ██             ██ ██      ██   ██ ██  ██ ██ ██  ██ ██ ██ ██  ██ ██ ██    ██ 
██       ██████  ██   ██    ██        ███████  ██████ ██   ██ ██   ████ ██   ████ ██ ██   ████  ██████  
                                                                                                        
                                                                                                        
    '''
    print(Colorate.Vertical(Colors.green_to_blue, Center.XCenter(header)))

    ip = input(Colorate.Horizontal(Colors.green_to_blue, 'Enter the IP address to scan: ')).strip()

    print(Colorate.Horizontal(Colors.green_to_blue, f"\nPlease Wait. Scanning ip"))

    nm = nmap.PortScanner()
    nm.scan(hosts=ip, ports='1-1024', arguments='-sV')


    for host in nm.all_hosts():
        print(Colorate.Horizontal(Colors.green_to_blue, f'\nHost: {host} ({nm[host].hostname()})'))
        print(Colorate.Horizontal(Colors.green_to_blue, f'State: {nm[host].state()}'))

        for proto in nm[host].all_protocols():
            print(Colorate.Horizontal(Colors.green_to_blue, '----------'))
            print(Colorate.Horizontal(Colors.green_to_blue, f'Protocol: {proto}'))

            lport = nm[host][proto].keys()
            for port in sorted(lport):
                port_info = nm[host][proto][port]
                service = port_info.get('name', 'Unknown')
                version = port_info.get('version', 'Unknown')
                product = port_info.get('product', 'Unknown')
                extrainfo = port_info.get('extrainfo', 'Unknown')

                print(Colorate.Horizontal(Colors.green_to_blue, f'Port: {port}\tState: {port_info["state"]}\tService: {service}\tVersion: {version}'))
                print(Colorate.Horizontal(Colors.green_to_blue, f'Product: {product}\tExtra Info: {extrainfo}'))

    input(Colorate.Horizontal(Colors.green_to_blue, "\nPress Enter to return to the port scan menu..."))


def ip_geolocation_lookup():

    clear_screen()
    header = '''
 ██████╗ ███████╗ ██████╗     ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██╔════╝ ██╔════╝██╔═══██╗    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
██║  ███╗█████╗  ██║   ██║    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
██║   ██║██╔══╝  ██║   ██║    ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
╚██████╔╝███████╗╚██████╔╝    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
 ╚═════╝ ╚══════╝ ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                                                 
    '''
    print(Colorate.Horizontal(Colors.green_to_blue, header))
    
    prompt = Colorate.Horizontal(Colors.green_to_blue, "Enter the IP address: ")
    ip_address = input(prompt).strip()
    if not ip_address:
        ip_address = requests.get('https://api.ipify.org').text
    
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()
        data = response.json()
        
        info = f'''
╔══════════════════════════════════════════════════════════╗
║ IP Address: {data.get('ip', 'N/A'):<45}║
║ Hostname: {data.get('hostname', 'N/A'):<46} ║
║ City: {data.get('city', 'N/A'):<50} ║
║ Region: {data.get('region', 'N/A'):<48} ║
║ Country: {data.get('country', 'N/A'):<47} ║
║ Location: {data.get('loc', 'N/A'):<46} ║
╚══════════════════════════════════════════════════════════╝
        '''
        colored_info = Colorate.Horizontal(Colors.green_to_blue, info)
        print(colored_info)
    except requests.RequestException as e:
        print(Colorate.Horizontal(Colors.green_to_blue, f"Error: {str(e)}"))
    input("\nPress Enter to return to the main menu...")
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def option05():
    clear_screen()

    header = '''
 ▒█████    ██████  ██▓ ███▄    █ ▄▄▄█████▓     ██████ ▓█████ ▄▄▄       ██▀███   ▄████▄   ██░ ██ 
▒██▒  ██▒▒██    ▒ ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒   ▒██    ▒ ▓█   ▀▒████▄    ▓██ ▒ ██▒▒██▀ ▀█  ▓██░ ██▒
▒██░  ██▒░ ▓██▄   ▒██▒▓██  ▀█ ██▒▒ ▓██░ ▒░   ░ ▓██▄   ▒███  ▒██  ▀█▄  ▓██ ░▄█ ▒▒▓█    ▄ ▒██▀▀██░
▒██   ██░  ▒   ██▒░██░▓██▒  ▐▌██▒░ ▓██▓ ░      ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██▀▀█▄  ▒▓▓▄ ▄██▒░▓█ ░██ 
░ ████▓▒░▒██████▒▒░██░▒██░   ▓██░  ▒██▒ ░    ▒██████▒▒░▒████▒▓█   ▓██▒░██▓ ▒██▒▒ ▓███▀ ░░▓█▒░██▓
░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒   ▒ ░░      ▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ░▒ ▒  ░ ▒ ░░▒░▒
  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░    ░       ░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░  ░▒ ░ ▒░  ░  ▒    ▒ ░▒░ ░
░ ░ ░ ▒  ░  ░  ░   ▒ ░   ░   ░ ░   ░         ░  ░  ░     ░    ░   ▒     ░░   ░ ░         ░  ░░ ░
    ░ ░        ░   ░           ░                   ░     ░  ░     ░  ░   ░     ░ ░       ░  ░  ░
                                                                               ░               
    '''
    print(Colorate.Vertical(Colors.green_to_blue, Center.XCenter(header)))

    username = input(Colorate.Horizontal(Colors.green_to_blue, 'enter username')).strip()

    platforms = {
        "YouTube": f"https://www.youtube.com/@{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Amazon": f"https://www.amazon.com/profile/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Roblox": f"https://www.roblox.com/users/{username}/profile",
         "Facebook": f"https://www.facebook.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Twitch": f"https://www.twitch.tv/{username}",
        "GitHub": f"https://github.com/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Flickr": f"https://www.flickr.com/people/{username}/",
        "Tumblr": f"https://{username}.tumblr.com",
        "Dribbble": f"https://dribbble.com/{username}",
        "VK": f"https://vk.com/{username}",
        "Quora": f"https://www.quora.com/profile/{username}",
        "WordPress": f"https://{username}.wordpress.com",
        "Blogger": f"https://{username}.blogspot.com",
        "Goodreads": f"https://www.goodreads.com/{username}",
        "Last.fm": f"https://www.last.fm/user/{username}",
        "Patreon": f"https://www.patreon.com/{username}",
        "AngelList": f"https://angel.co/{username}",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "PayPal.Me": f"https://www.paypal.me/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Meetup": f"https://www.meetup.com/members/{username}",
        "Mixcloud": f"https://www.mixcloud.com/{username}",
        "Flipboard": f"https://flipboard.com/@{username}",
        "Keybase": f"https://keybase.io/{username}",
        "Tinder": f"https://tinder.com/@{username}",
        "ZoomInfo": f"https://www.zoominfo.com/p/{username}",
        "ReverbNation": f"https://www.reverbnation.com/{username}",
        "Weibo": f"https://weibo.com/{username}",
        "OKCupid": f"https://www.okcupid.com/profile/{username}",
    }

    for platform, url in platforms.items():
        if platform == "YouTube":
            check_youtube_username(url, platform)
        else:
            check_username(url, platform)

    input(Colorate.Horizontal(Colors.green_to_blue, "Press Enter to return to the main menu..."))

def check_youtube_username(url, platform):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.find('meta', {'name': 'title'})
            about = soup.find('meta', {'name': 'description'})
            subscribers = soup.find('yt-formatted-string', {'id': 'subscriber-count'})
            video_count = soup.find('span', {'class': 'style-scope yt-formatted-string'})

            title_text = title['content'] if title else "Unknown"
            about_text = about['content'] if about else "No description available"
            subscribers_text = subscribers.text if subscribers else "Subscriber count hidden"
            video_count_text = video_count.text if video_count else "Video count hidden"

            print(Colorate.Horizontal(Colors.green_to_blue, f"\n1 user found with the username on {platform}."))
            print(Colorate.Horizontal(Colors.green_to_blue, f"Channel Name: {title_text}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"Subscribers: {subscribers_text}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"Videos: {video_count_text}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"About: {about_text}\n"))
        elif response.status_code == 404:
            print(Colorate.Horizontal(Colors.red_to_white, f"\nNo user found with the username on {platform}.\n"))
        else:
            print(Colorate.Horizontal(Colors.yellow_to_red, f"Unexpected error occurred while checking {platform}."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"An error occurred while checking {platform}: {str(e)}"))

def check_facebook_username(url, platform):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            name = soup.find('meta', {'property': 'og:title'})
            description = soup.find('meta', {'name': 'description'})

            name_text = name['content'] if name else "Unknown"
            description_text = description['content'] if description else "No description available"

            print(Colorate.Horizontal(Colors.green_to_blue, f"\n1 user found with the username on {platform}."))
            print(Colorate.Horizontal(Colors.green_to_blue, f"Name: {name_text}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"Description: {description_text}\n"))
        elif response.status_code == 404:
            print(Colorate.Horizontal(Colors.red_to_white, f"\nNo user found with the username on {platform}.\n"))
        else:
            print(Colorate.Horizontal(Colors.yellow_to_red, f"Unexpected error occurred while checking {platform}."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"An error occurred while checking {platform}: {str(e)}"))

def check_linkedin_username(url, platform):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            name = soup.find('title')
            description = soup.find('meta', {'name': 'description'})

            name_text = name.text.strip() if name else "Unknown"
            description_text = description['content'] if description else "No description available"

            print(Colorate.Horizontal(Colors.green_to_blue, f"\nCODE 200 [?] USERNAME FOUND {platform}."))
            print(Colorate.Horizontal(Colors.green_to_blue, f"Name: {name_text}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"Description: {description_text}\n"))
        elif response.status_code == 404:
            print(Colorate.Horizontal(Colors.red_to_white, f"\nERROR [?] ERROR {platform}.\n"))
        else:
            print(Colorate.Horizontal(Colors.yellow_to_red, f"Unexpected error occurred while checking {platform}."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"An error occurred while checking {platform}: {str(e)}"))


def check_twitter_username(url, platform):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            name = soup.find('title')
            description = soup.find('meta', {'name': 'description'})
            followers = soup.find('span', {'class': 'ProfileNav-value'})

            name_text = name.text.strip() if name else "Unknown"
            description_text = description['content'] if description else "No description available"
            followers_text = followers.text.strip() if followers else "Follower count hidden"

            print(Colorate.Horizontal(Colors.green_to_blue, f"\n1 user found with the username on {platform}."))
            print(Colorate.Horizontal(Colors.green_to_blue, f"Name: {name_text}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"Description: {description_text}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"Followers: {followers_text}\n"))
        elif response.status_code == 404:
            print(Colorate.Horizontal(Colors.red_to_white, f"\nNo user found with the username on {platform}.\n"))
        else:
            print(Colorate.Horizontal(Colors.yellow_to_red, f"Unexpected error occurred while checking {platform}."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"An error occurred while checking {platform}: {str(e)}"))


def check_instagram_username(url, platform):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            name = soup.find('title')
            description = soup.find('meta', {'name': 'description'})
            followers = soup.find('meta', {'name': 'description'})['content'].split('-')[0]

            name_text = name.text.strip() if name else "Unknown"
            description_text = description['content'] if description else "No description available"
            followers_text = followers.strip() if followers else "Follower count hidden"

            print(Colorate.Horizontal(Colors.green_to_blue, f"\n1 user found with the username on {platform}."))
            print(Colorate.Horizontal(Colors.green_to_blue, f"Name: {name_text}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"Description: {description_text}"))
            print(Colorate.Horizontal(Colors.green_to_blue, f"Followers: {followers_text}\n"))
        elif response.status_code == 404:
            print(Colorate.Horizontal(Colors.red_to_white, f"\nNo user found with the username on {platform}.\n"))
        else:
            print(Colorate.Horizontal(Colors.yellow_to_red, f"Unexpected error occurred while checking {platform}."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"An error occurred while checking {platform}: {str(e)}"))

def check_username(url, platform):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(Colorate.Horizontal(Colors.green_to_blue, f"\nCODE 200 [?] USERNAME FOUND {platform}.\n"))
        elif response.status_code == 404:
            print(Colorate.Horizontal(Colors.red_to_white, f"\nERROR CODE 404 [?] NO USERNAME FOUND {platform}.\n"))
        else:
            print(Colorate.Horizontal(Colors.yellow_to_red, f"ERROR {platform}."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"ERROR {platform}: {str(e)}"))


def option06():
    
    header_logo = '''
┌─────────────────────────────────────────────────────────┐
│                ,,ggddY"""Ybbgg,,                        │
│            ,agd888b,_ "Y8, ___`""Ybga,                  │
│         ,gdP""88888888baa,.""8b    "888g,               │
│       ,dP"     ]888888888P'  "Y     `888Yb,             │
│     ,dP"      ,88888888P"  db,       "8P""Yb,           │
│    ,8"       ,888888888b, d8888a           "8,          │
│   ,8'        d88888888888,88P"' a,          `8,         │
│  ,8'         88888888888888PP"  ""           `8,        │
│  d'          I88888888888P"                   `b        │
│  8           `8"88P""Y8P'                      8        │
│  8            Y 8[  _ "                        8        │
│  8              "Y8d8b  "Y a                   8        │
│  8                 `""8d,   __                 8        │
│  Y,                    `"8bd888b,             ,P        │
│  `8,                     ,d8888888baaa       ,8'        │
│   `8,                    888888888888'      ,8'         │
│    `8a                   "8888888888I      a8'          │
│     `Yba                  `Y8888888P'    adP'           │
│       "Yba                 `888888P'   adY"             │
│         `"Yba,             d8888P" ,adP"'               │
│            `"Y8baa,      ,d888P,ad8P"'                  │
│                 ``""YYba8888P""''                       │
└─────────────────────────────────────────────────────────┘               
    '''
    print(Colorate.Vertical(Colors.green_to_blue, Center.XCenter(header_logo)))

    try:
        latitude = float(input(Colorate.Horizontal(Colors.green_to_blue, "enter latitude[!] ").strip()))
        longitude = float(input(Colorate.Horizontal(Colors.green_to_blue, "enter longitude[!] ").strip()))

        earth_url = f"https://earth.google.com/web/search/{latitude},{longitude}"

        webbrowser.open(earth_url)
        print(Colorate.Horizontal(Colors.green_to_blue, f"OPENING GOOGLE [!] {latitude}, {longitude}"))

    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_white, "INVALID [?]"))
    

def generate_rare_usernames(length=4, count=100):
    usernames = []
    for _ in range(count):
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        usernames.append(username)
    return usernames

def check_username_availability(username, platform):
    url = ""

    if platform == "Instagram":
        url = f"https://www.instagram.com/{username}/"
    elif platform == "TikTok":
        url = f"https://www.tiktok.com/@{username}"
    elif platform == "Facebook":
        url = f"https://www.facebook.com/{username}"
    elif platform == "Twitch":
        url = f"https://www.twitch.tv/{username}"
    elif platform == "Steam":
        url = f"https://steamcommunity.com/id/{username}"
    elif platform == "Spotify":
        url = f"https://open.spotify.com/user/{username}"
    elif platform == "Github":
        url = f"https://github.com/{username}"
    elif platform == "SoundCloud":
        url = f"https://soundcloud.com/{username}"

    try:
        response = requests.get(url)
        if response.status_code == 404:
            return True  
        elif response.status_code == 200:
            return False  
        else:
            print(Colorate.Horizontal(Colors.yellow_to_red, f"Unexpected error occurred while checking {platform}."))
            return None
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"An error occurred while checking {platform}: {str(e)}"))
        return None

def option07():
    header = '''
███╗   ██╗ █████╗ ███╗   ███╗███████╗███████╗
████╗  ██║██╔══██╗████╗ ████║██╔════╝██╔════╝
██╔██╗ ██║███████║██╔████╔██║█████╗  ███████╗
██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║
██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗███████║
╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝
                                             
    '''
    print(Colorate.Horizontal(Colors.green_to_blue, header))
    
    print(Colorate.Horizontal(Colors.green_to_blue, "Looking for rare usernames"))
    
    rare_usernames = generate_rare_usernames()
    
    platforms = ["Instagram", "TikTok", "Facebook", "Twitch", "Steam", "Spotify", "Github", "SoundCloud",]
    
    available_usernames = {platform: [] for platform in platforms}
    
    for username in rare_usernames:
        for platform in platforms:
            is_available = check_username_availability(username, platform)
            if is_available:
                status = "VALID"
                available_usernames[platform].append(username)
            else:
                status = "TAKEN"
            print(Colorate.Horizontal(Colors.green_to_blue if is_available else Colors.red_to_white,
                                      f"{platform} Username: {username} - STATUS: {status}"))

    for platform in platforms:
        print(Colorate.Horizontal(Colors.green_to_blue, f"\nAvailable Usernames on {platform}:"))
        if available_usernames[platform]:
            for username in available_usernames[platform]:
                print(Colorate.Horizontal(Colors.green_to_blue, f"- {username}"))
        else:
            print(Colorate.Horizontal(Colors.red_to_white, f"No available usernames found on {platform}."))
    
def option9():
    guide_text = '''
    ---------------------
    IP loggers are tools that take the IP of someone who’s clicked a link and sends it to your email. A lot of the time you’ll need good SE’ing skills when IP logging someone. I’ll include some messages below that have made my IP logging a lot easier. There’s one IP logger site that I know which gives you a free IP logger and sends the IPs to your emails once clicked. It’s free and easy to use. All you have to do is head over to http://whatstheirip.com/. Once you’re on WhatsTheirIP, enter your email in the box that says “Your Email Address:”. I recommend using a throwaway email like on 10minutemail.com or just a random disposable Outlook (better than Gmail as you don’t have to verify most of the time). Now, we have an IP logging link. What’s that? It looks very suspicious? Of course! It’s an IP logger! That’s why we’re going to hide the link in a link shorter like https://bitly.com/ so it looks safer. They’ll never know they’re running into an IP logger.
    1. Take your IP logger link and head over to https://bitly.com/ to shorten your link.
    2. There should be a box that says “Paste a link to shorten it”, paste your link there and click SHORTEN.
    3. Take the shortened link and send it in the message you were sending to the target as a replacement over your regular IP logger. This makes it look a lot safer and legit than your actual IP logger link.
    ---------------------
    Link Shortening Sites:
    - https://bitly.com/ - My personal favorite. Easy to use and most people fall for it.
    - https://goo.gl/ - Google’s link shortening tool. They’ll probably assume a link from Google is safe and click it. I recommend Bitly however.
    - https://tinyurl.com/
    - http://ow.ly/url/shorten-url - Looks really suspicious but is a link shortener so here it is.
    ---------------------
    Tip: Make your IP logger believable. Here is an example of making it look realistic.
    Scenario = Scaring your target: “LOL you fucking retard I can’t believe you were this easy to dox. Look at your shitty house and mom’s picture (insert ip logger shortened here). Some spas like you doesn’t belong on the internet lmao.” - This always works for me. I’ve never failed using this as most people are eager to look to see if it’s really their information.
    Scenario = SEing a random: “Yo, do you know this kid? He was fucking with me so I posted his information online. If he’s your friend I don’t wanna fuck with him so just to be sure (insert logger here shortened).”
    Just be creative with it. Don’t sound like a complete moron who’s just trying to dox with absolutely no knowledge. You need to make sure you sound realistic and make sure your story is believable. Guess we’re eWhoring now.
    ---------------------
    Doxing IP:
    ---------------------
    Using the target’s IP address can be very useful when doxing. I won’t go over ISP doxing in this part as there is a section for doxing in the next one. I’ll be telling you how to find their general location, hostname, ISP, ISP organization, etc. in the first method. In the second I’ll be telling you how to look the IP up on lookup sites to see who has it, kind of like a phone number lookup on Whitepages. The third method I’ll be explaining is IP2Skype, the opposite but just as useful version of Skype2 IP. It’ll give you any Skype associated with the IP, pretty useful right?
    ---------------------
    Geolocating The IP For Location:
    First, we’re going to go over using the IP for general location, hostname, and stuff like that. I’m going to list a few IP Geolocation tools but I’m going to demonstrate my favorite as it proves to be the most accurate for me. I used to use infosniper.net but it seemed a bit off like wrong city but I’ll still list it just in case it was just me experiencing that. Anyways my favorite is ipaddress.com as it tells you a lot on the IP including hostname, ISP, ISP organization, city, state, zip code, timezone, etc. with no problem at all.
    ---------------------
    IP Geolocation Tools:
    - http://ipaddress.com
    - http://infosniper.net
    - (List other IP geolocation tools here)
    ---------------------
    Tip: Remember, using someone’s IP for doxing can lead to legal consequences depending on your jurisdiction. Be cautious and responsible.
    ---------------------
    '''

    colored_text = Colorate.Horizontal(Colors.green_to_blue, guide_text)
    print(colored_text)
    input("\nPress Enter to return to the previous menu...")


def option10():
    guide_text = '''
Doxing A Name
---------------------
Using the target’s name is also very helpful. If you have their name then you can possibly find out where they live, what their number is, relatives, etc., which could really be beneficial in a dox. We’re going to be searching the targets on Whitepages and other sites, as a lot of people don’t think to remove their information on Whitepages or simply don’t know how. Their ignorance will be their mistake.

First, go to one of these sites below:
- http://10digits.us (Really good)
- http://thatsthem.com (Also really good)
- http://www.yellowpages.com (Good for just last name and location)
- http://www.whitepages.com (Average)
- http://www.ussearch.com/ (Average)
- http://www.pipl.com/
- http://www.canada411.ca/ (Canadian People)
- http://www.peekyou.com/united_kingdom (UK People)
- http://webmii.com/ (UK People)
- http://www.ratsit.se/BC/SearchPerson.aspx (Swedish People)
- http://www.dgs.dk (Danish People)
- https://find-person-germany.com/ (German People)
- https://www.goyellow.de/ (German People)

Tip: You can probably find a lookup in your area by searching Google for "(enter country here) lookup sites)" and try as many as you can to see which one gives you the best results. The ones I listed are usually accurate and work for the areas they say they’re in. The ones without a specific country beside them are for the US primarily.

Now, we’re going to be using 10digits in the demonstration as it’s my favorite. Make sure you’re on the name tab and enter their first and last name in the first box. In the box on the right, enter their city and state or their zip code. If you want their city and state but have their zip code, there’s a section teaching that below too. Now when you’ve filled out the boxes, press the Search icon, and it’ll display whatever results it finds. I suggest searching through all that pop up if there aren’t too many to see which one is correct. Use this search for example - http://10digits.us/n/Susan_Banks/location/San_Diego%252C_California

There are three results. Click +More on the first one and you’ll receive her address. How hard was that? It’s actually one of the easiest things when doxing.

We can search our target’s number just as we did with the target’s name. There are many sites to use and I’ll list my favorites. I prefer to use 10digits.us as it’s always brought me the best results and never let me down.

First, go to one of the sites below:
- http://www.10digits.us
- http://www.reversemobile.com/index.php
- http://thatsthem.com
- http://www.numberway.com
- http://www.phonenumber.com
- http://www.fonefinder.net
- http://www.whitepages.com
- http://www.pipl.com/
- http://www.canada411.ca/ (Canadian People)
- https://www.goyellow.de/ (German People)
- http://www.dgs.dk (Danish People)

I’m demonstrating 10digits in this example but you can use whatever site you want. Now that we’re on 10digits, click on the Phone button, input their number, and press the Search icon. It’ll display results just like the name search did. You can get the owner’s name, address, state, etc., with just a search.

Tip: Most of the time if it displays multiple results it’s for two adults living in the house.
'''

    colored_text = Colorate.Horizontal(Colors.green_to_blue, guide_text)
    print(colored_text)
    input("\nPress Enter to return to the previous menu...")

def option11():
    guide_text = '''
    https://intelx.io
    https://leakpeek.com
    https://leak-lookup.com
    https://snusbase.com/search
    https://haveibeenpwned.com
    https://www.dehashed.com/
    https://cybernews.com/personal-data-leak-check
    https://breachdirectory.com/search
    https://breachdirectory.org
    https://leakcheck.net
    https://breachdbsztfykg2fdaq2gnqnxfsbj5d....onion.pet
    https://checkleaked.cc
    https://namescan.io/freeemailcompromisedcheck
    https://monitor.firefox.com
    https://www.fasterbroadband.co.uk/tools/...ach-search
    https://www.hotsheet.com/inoitsu
    https://checkashleymadison.com
    https://surfshark.com
    https://tragercop.1password.com
    https://ghostproject.fr
    https://saverudata.online/ (RussinLeak DB search)
    '''

    colored_text = Colorate.Horizontal(Colors.blue_to_purple, guide_text)
    print(colored_text)
    input("\nPress Enter to return to the previous menu...")

def option12():
    guide_text = '''
Doxing An Email
---------------------
Using the target’s email is an amazing thing when doxing.
Doxing with an email makes doxing simple to be honest. You can
use a target’s email for a bunch of things and I’m gonna list
a few methods that you can use when doxing someone’s email. This is usually
a lot more effective and brings more results than doxing with an alias or name.

Finding Facebook -
You can get your target’s Facebook with their email. It takes a few steps and isn’t hard at all.
1. Head over to Facebook.com
2. Select the “Forgot your password?” option
3. In the box in the middle of the page, put the target’s email.
4. It should give you the target’s name, picture, and sometimes it may even give you the last 4 digits of their number.
5. Use the name they just gave you and/or picture and put it in the dox. We’ll use them later.
Tip: You can also use https://www.facebook.com/search.php?q=(email here) to find their Facebook.
Tip X2: This can also work with a phone number, hence why entering a phone number is also an option.
Tip X3:
https://whoisology.com/email/archive_10/
(email here) can also help you find any websites associated with an email. See the Using
Target’s Website section for what you can do with their website. You can basically get their full dox with their website in most cases.

Finding Skype -
You can easily get your target’s Skype with their email as well. You can do this
within Skype itself or you can use an Email2Skype tool. I’ll show you how to use both.

Using Skype To Find Skype -
1. Go to the Skype search bar. It’s usually above all your contacts.
2. For the search field, instead of entering their Skype, you’re going to enter their email.
3. Wait a few seconds for results. If there are none, maybe he doesn’t use the email on Skype or you can try the next method. It always works when else fails.

Using Email2Skype Tools -
Email2Skype tools basically give you any Skype account connected to an email.
1. Go to http://mostwantedhf.info/email.php
2. Now you’re going to want to enter the target’s email in the Email box and click Submit.
3. There you go. You just found their Skype.
Tip: If both methods don’t work, maybe they don’t use Skype or have multiple emails.
'''

    colored_text = Colorate.Horizontal(Colors.purple_to_red, guide_text)
    print(colored_text)
    input("\nPress Enter to return to the previous menu...")

def main():
    while True:
        clear_screen()
        print_banner(banner)
        print_menu()
        choice = input(Colorate.Horizontal(Colors.blue_to_red, "\n\n» "))

        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            ip_geolocation_lookup()

        elif choice == '4':
            userid = input(" Enter in somones id  ")
            encodedBytes = base64.b64encode(userid.encode("utf-8"))
            encodedStr = str(encodedBytes, "utf-8")
            print(f'\n [token]   {encodedStr}')
            os.system('pause >nul')

        elif choice == '5':
            option05()
        elif choice == "6":
            option06()
        elif choice == '7':
            option07()
        elif choice == "8":
            page2()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
            input("Press Enter to continue")
if __name__ == "__main__":
    main()

