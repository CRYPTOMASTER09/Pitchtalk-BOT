import requests
import json
import random
import os
import urllib.parse
from colorama import *
from datetime import datetime, timezone
import time
import pytz

wib = pytz.timezone('Asia/Jakarta')

class PitchTalk:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'api.pitchtalk.app',
            'Origin': 'https://webapp.pitchtalk.app',
            'Pragma': 'no-cache',
            'Referer': 'https://webapp.pitchtalk.app/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }
        self.slugs = ['share-x', 'share-tiktok']
        self.current_slug_index = 0

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Pitch Talk - BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<CRYPTO MASTER>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def load_data(self, query: str) -> dict:
        parsed_query = urllib.parse.parse_qs(query)
        user_data = json.loads(parsed_query['user'][0])
        
        data = {
            "hash": query,
            "photoUrl": "",
            "referralCode": "3dbacc",
            "telegramId": str(user_data['id']),
            "username": str(user_data['username'])
        }

        return data

    def auth(self, query: str, retries=5):
        url = 'https://api.pitchtalk.app/v1/api/auth'
        data = json.dumps(self.load_data(query))
        self.headers.update({
            'Content-Type': 'application/json',
            'X-Telegram-Hash': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}Request Timeout{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def claim_refferal(self, token: str, query: str, retries=5):
        url = 'https://api.pitchtalk.app/v1/api/users/claim-referral'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'X-Telegram-Hash': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}Request Timeout{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def farmings(self, token: str, query: str, retries=5):
        url = 'https://api.pitchtalk.app/v1/api/farmings'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'X-Telegram-Hash': query
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers, timeout=10)
                if not response.text.strip():
                    return None
                
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}Request Timeout{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def create_farming(self, token: str, query: str, retries=5):
        url = 'https://api.pitchtalk.app/v1/api/users/create-farming'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'X-Telegram-Hash': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}Request Timeout{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def claim_farming(self, token: str, query: str, retries=5):
        url = 'https://api.pitchtalk.app/v1/api/users/claim-farming'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'X-Telegram-Hash': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}Request Timeout{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def tasks(self, token: str, query: str, retries=5):
        url = 'https://api.pitchtalk.app/v1/api/tasks'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'X-Telegram-Hash': query
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}Request Timeout{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def start_tasks(self, token: str, query: str, task_id: str, retries=5):
        url = f'https://api.pitchtalk.app/v1/api/tasks/{task_id}/start'
        data = {}
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'X-Telegram-Hash': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, json=data, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}Request Timeout{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None

    def verify_tasks(self, token: str, query: str, retries=5):
        url = 'https://api.pitchtalk.app/v1/api/tasks/verify'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'X-Telegram-Hash': query
        })

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}Request Timeout{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def upgrade_level(self, token: str, query: str, retries=5):
        url = 'https://api.pitchtalk.app/v1/api/users/upgrade'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'X-Telegram-Hash': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, timeout=10)
                if response.status_code == 400:
                    return response.json()
                
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}Request Timeout{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def upgrade_speed(self, token: str, query: str, retries=5):
        url = 'https://api.pitchtalk.app/v1/api/users/upgrade-speed'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'X-Telegram-Hash': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, timeout=10)
                if response.status_code == 500:
                    return response.json()
                
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}Request Timeout{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def upgrade_capacity(self, token: str, query: str, retries=5):
        url = 'https://api.pitchtalk.app/v1/api/users/upgrade-capacity'
        self.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'Content-Length': '0',
            'X-Telegram-Hash': query
        })

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, timeout=10)
                if response.status_code == 500:
                    return response.json()
                
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, requests.Timeout, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}Request Timeout{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(2)
                else:
                    return None
        
    def question(self):
        while True:
            upgrade_level = input("Upgrade User Level? [y/n] -> ").strip().lower()
            if upgrade_level in ["y", "n"]:
                upgrade_level = upgrade_level == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to upgrade or 'n' to skip.{Style.RESET_ALL}")
        
        while True:
            upgrade_speed = input("Auto Upgrade Speed Booster Level? [y/n] -> ").strip().lower()
            if upgrade_speed in ["y", "n"]:
                upgrade_speed = upgrade_speed == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to upgrade or 'n' to skip.{Style.RESET_ALL}")
        
        while True:
            upgrade_capacity = input("Auto Upgrade Time Booster Level? [y/n] -> ").strip().lower()
            if upgrade_capacity in ["y", "n"]:
                upgrade_capacity = upgrade_capacity == "y"
                break
            else:
                print(f"{Fore.RED+Style.BRIGHT}Invalid Input.{Fore.WHITE+Style.BRIGHT} Choose 'y' to upgrade or 'n' to skip.{Style.RESET_ALL}")

        
        return upgrade_level, upgrade_speed, upgrade_capacity
        
    def process_query(self, query, upgrade_level: bool, upgrade_speed: bool, upgrade_capacity: bool):
        account = self.auth(query)
        if not account:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.RED + Style.BRIGHT} Query Id Isn't Valid {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return

        if account:
            token = account['accessToken']
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {account['user']['username']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {account['user']['coins']} $PITCH {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}] [ Ticket{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {account['user']['tickets']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}] [ Level{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {account['user']['level']} {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
            time.sleep(1)

            daily_reward = account['dailyRewards']
            if daily_reward['isNewDay'] and daily_reward:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Daily Login{Style.RESET_ALL}"
                    f"{Fore.GREEN + Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} {daily_reward['coins']} $PITCH {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} {daily_reward['tickets']} Ticket {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Streak{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} {daily_reward['loginStreak']} Day {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Daily Login{Style.RESET_ALL}"
                    f"{Fore.YELLOW + Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Streak{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} {daily_reward['loginStreak']} Day {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            refferal = account['user']['referralRewards']
            if refferal != 0:
                claim = self.claim_refferal(token, query)
                if claim:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                        f"{Fore.GREEN + Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}] [ Reward{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {account['user']['referralRewards']} $PITCH {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                    f"{Fore.YELLOW + Style.BRIGHT} No Available $PITCH to Claim {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            farm = self.farmings(token, query)
            if not farm:
                create = self.create_farming(token, query)
                if create:
                    end_farm_utc = datetime.strptime(create['farming']['endTime'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
                    end_farm_wib = end_farm_utc.astimezone(wib).strftime('%x %X %Z')
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.GREEN + Style.BRIGHT} Is Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {end_farm_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Isn't Started {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )

            else:
                now = datetime.now(timezone.utc)
                end_farm_utc = datetime.strptime(farm['endTime'], '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc)
                end_farm_wib = end_farm_utc.astimezone(wib).strftime('%x %X %Z')

                if now >= end_farm_utc:
                    claim = self.claim_farming(token, query)
                    if claim:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.GREEN + Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}] [ Balance{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {claim['coins']} $PITCH {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                            f"{Fore.RED + Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Farming{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Not Time to Claim {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}] [ Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT} {end_farm_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(1)

            tasks = self.tasks(token, query)
            if tasks:
                completed = False
                for task in tasks:
                    task_id = task['id']
                    title = task['template']['title']
                    reward_coin = task['template']['rewardCoins']
                    reward_ticket = task['template']['rewardTickets']
                    status = task['status']

                    if task and status in ["INITIAL", "VERIFY_REJECTED"]:
                        start = self.start_tasks(token, query, task_id)
                        if start and start['status'] == "VERIFY_REQUESTED":
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ General Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.GREEN + Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )    
                            time.sleep(3)

                            verify = self.verify_tasks(token, query)
                            if verify:
                                status = verify[0]['status']
                                if status == "COMPLETED_CLAIMED":
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ General Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                        f"{Fore.GREEN + Style.BRIGHT}Is Verified{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reward{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {reward_coin} $PITCH {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}-{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {reward_ticket} Ticket {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ General Task{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                        f"{Fore.RED + Style.BRIGHT}Isn't Verified{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                                        f"{Fore.WHITE + Style.BRIGHT} Not Eligible {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )                         
                            else:
                                self.log(
                                    f"{Fore.MAGENTA + Style.BRIGHT}[ General Task{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                    f"{Fore.RED + Style.BRIGHT}Isn't Verified{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                                    f"{Fore.WHITE + Style.BRIGHT} Response Data Is None {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                )                            
                        else:
                            self.log(
                                f"{Fore.MAGENTA + Style.BRIGHT}[ General Task{Style.RESET_ALL}"
                                f"{Fore.WHITE + Style.BRIGHT} {title} {Style.RESET_ALL}"
                                f"{Fore.RED + Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                            )
                    else:
                        completed = True

                if completed:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ General Task{Style.RESET_ALL}"
                        f"{Fore.GREEN + Style.BRIGHT} Is Completed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )                 
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ General Task{Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            if upgrade_level:
                upgrade = self.upgrade_level(token, query)
                if upgrade:
                    level = account['user']['level'] + 1
                    if not 'message' in upgrade:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Farming Multiplier{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} Level {level} {Style.RESET_ALL}"
                            f"{Fore.GREEN + Style.BRIGHT}Is Upgraded{Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Farming Multiplier{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} Level {level} {Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT}Isn't Upgraded{Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {upgrade['message']} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Farming Multiplier{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Farming Multiplier{Style.RESET_ALL}"
                    f"{Fore.YELLOW + Style.BRIGHT} Upgrade Is Skipped {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            if upgrade_speed:
                upgrade = self.upgrade_speed(token, query)
                if upgrade:
                    level = account['user']['speedBoostLevel'] + 1
                    if not 'message' in upgrade:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Boost Speed{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} Level {level} {Style.RESET_ALL}"
                            f"{Fore.GREEN + Style.BRIGHT}Is Upgraded{Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                        )
                    else:
                        error_message = upgrade['message']
                        if "BadRequestException:" in error_message:
                            error_message = error_message.split("BadRequestException:")[1].strip()
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Boost Speed{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} Level {level} {Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT}Isn't Upgraded{Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {error_message} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Boost Speed{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Boost Speed{Style.RESET_ALL}"
                    f"{Fore.YELLOW + Style.BRIGHT} Upgrade Is Skipped {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
            time.sleep(1)

            if upgrade_capacity:
                upgrade = self.upgrade_capacity(token, query)
                if upgrade:
                    level = account['user']['timeBoostLevel'] + 1
                    if not 'message' in upgrade:
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Boost Time{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} Level {level} {Style.RESET_ALL}"
                            f"{Fore.GREEN + Style.BRIGHT}Is Upgraded{Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT} ]{Style.RESET_ALL}"
                        )
                    else:
                        error_message = upgrade['message']
                        if "BadRequestException:" in error_message:
                            error_message = error_message.split("BadRequestException:")[1].strip()
                        self.log(
                            f"{Fore.MAGENTA + Style.BRIGHT}[ Boost Time{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} Level {level} {Style.RESET_ALL}"
                            f"{Fore.YELLOW + Style.BRIGHT}Isn't Upgraded{Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                            f"{Fore.WHITE + Style.BRIGHT} {error_message} {Style.RESET_ALL}"
                            f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Boost Time{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Boost Time{Style.RESET_ALL}"
                    f"{Fore.YELLOW + Style.BRIGHT} Upgrade Is Skipped {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )
       
    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            upgrade_level, upgrade_speed, upgrade_capacity = self.question()

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query, upgrade_level, upgrade_speed, upgrade_capacity)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        time.sleep(3)

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Pitch Talk - BOT{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    run = PitchTalk()
    run.main()
