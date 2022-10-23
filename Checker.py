#Written by Zack00e
#https://github.com/Zack00e

import requests
import time
from colorama import init, Fore
init()               
time.sleep(2)
print(Fore.GREEN + 'Good lines.')
print(Fore.YELLOW + 'Good lines but already in use.')
print(Fore.RED + 'Wrong credentials.')
print(Fore.MAGENTA + 'Dead host or too slow.')
time.sleep(2)
print('\n')
print(Fore.CYAN + '[!] Caution: If the checker returns errors or stuck on the same cline for a long time, it might due to the website clines checking issues, try again in a few hours, and it should work :)')
print('\033[39m')
time.sleep(5)
print('\n')
with open('list.txt', 'r') as f:
   for line in f:
        url = 'https://www.clinetest.net/cam.php'
        cookies = {
            'key': '10' }
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.clinetest.net',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://www.clinetest.net/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'TE': 'trailers' }
        data = {
            'gidecek': line,
            'cevap': '10' }
        r = requests.post(url=url, headers=headers, data=data, cookies=cookies, stream=True)
        print(r.text.replace("   <lu style='color: red'>", Fore.RED + '').replace(' </lu><br />', '').replace("   <lu style='color: green'>", Fore.GREEN + '').replace("   <lu style='color: #575863'>", Fore.MAGENTA + '').replace("   <lu style='color: #f5b72f'>", Fore.YELLOW + '').replace("Could not connect to the database u811598088_GmaCj :SQLSTATE[HY000] [1226] User 'u811598088_nlX2Z' has exceeded the 'max_user_connections' resource (current value: 15)", 'Unknown Error'))
        

   if not line:
    pass            


 
