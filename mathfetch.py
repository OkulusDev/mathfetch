#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import platform
import subprocess
import socket


class ANSIColors:
	CEND      = '\033[0m'
	CBOLD     = '\033[1m'
	CITALIC   = '\033[3m'
	CURL      = '\033[4m'
	CBLINK    = '\033[5m'
	CBLINK2   = '\033[6m'
	CSELECTED = '\033[7m'

	CBLACK  = '\033[30m'
	CRED    = '\033[31m'
	CGREEN  = '\033[32m'
	CYELLOW = '\033[33m'
	CBLUE   = '\033[34m'
	CVIOLET = '\033[35m'
	CBEIGE  = '\033[36m'
	CWHITE  = '\033[37m'

	CBLACKBG  = '\033[40m'
	CREDBG    = '\033[41m'
	CGREENBG  = '\033[42m'
	CYELLOWBG = '\033[43m'
	CBLUEBG   = '\033[44m'
	CVIOLETBG = '\033[45m'
	CBEIGEBG  = '\033[46m'
	CWHITEBG  = '\033[47m'

	CGREY    = '\033[90m'
	CRED2    = '\033[91m'
	CGREEN2  = '\033[92m'
	CYELLOW2 = '\033[93m'
	CBLUE2   = '\033[94m'
	CVIOLET2 = '\033[95m'
	CBEIGE2  = '\033[96m'
	CWHITE2  = '\033[97m'

	CGREYBG    = '\033[100m'
	CREDBG2    = '\033[101m'
	CGREENBG2  = '\033[102m'
	CYELLOWBG2 = '\033[103m'
	CBLUEBG2   = '\033[104m'
	CVIOLETBG2 = '\033[105m'
	CBEIGEBG2  = '\033[106m'
	CWHITEBG2  = '\033[107m'


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[96m'


class Fetch:
	def __init__(self, full: bool=True):
		self.full: bool = full

	def local_ip(self):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect(("8.8.8.8", 80))

			return f'󰩟  {s.getsockname()[0]}'
		except Exception as e:
			return f'{bcolors.FAIL}[!] {e}{bcolors.ENDC}'

	def hostname(self):
		try:
			return f'󰘧 {socket.gethostname()} 󰘧'
		except Exception as e:
			return f'{bcolors.FAIL}[!] {e}{bcolors.ENDC}'

	def os_version(self):
		try:
			return f'  {platform.platform()}'
		except Exception as e:
			return f'{bcolors.FAIL}[!] {e}{bcolors.ENDC}'

	def uptime(self):
		try:
			return f'  {subprocess.check_output(["uptime -p"], shell=True).decode("utf-8").strip().replace("up ", "")}'
		except Exception as e:
			return f'{bcolors.FAIL}[!] {e}{bcolors.ENDC}'

	def screen_size(self):
		try:
			resolution = subprocess.check_output(["xrandr | grep \"*\""], shell=True).decode('utf-8').strip().split(' ')[0]
			return f'  {resolution}'
		except Exception as e:
			return f'{bcolors.FAIL}[!] {e}{bcolors.ENDC}'


def get_logo(color: str, local_ip, hostname, os_version, screen_size, uptime) -> str:
	color = color.strip().lower()

	if color == 'blue':
		color = bcolors.OKBLUE
	elif color == 'cyan':
		color = bcolors.OKCYAN
	elif color == 'green':
		color = bcolors.OKGREEN
	elif color == 'yellow':
		color = bcolors.WARNING
	elif color == 'red':
		color = bcolors.FAIL
	elif color == 'boldgrey':
		color = ANSIColors.CBEIGE + bcolors.BOLD

	hostname = f"-> {hostname} <-"
	hostname_len = len(hostname) + 1

	logo = f'''{color}
                 _   _           {ANSIColors.CITALIC}{hostname}{bcolors.ENDC}{color}
                | | | |         {ANSIColors.CBOLD}{"" * hostname_len}{bcolors.ENDC}{color}
 _ __ ___   __ _| |_| |__       {ANSIColors.CITALIC}{local_ip}{bcolors.ENDC}{color}
| '_ ` _ \\ / _` | __| '_ \\      {ANSIColors.CITALIC}{os_version}{bcolors.ENDC}{color}
| | | | | | (_| | |_| | | |     {ANSIColors.CITALIC}{screen_size}{bcolors.ENDC}{color}
|_| |_| |_|\\__,_|\\__|_| |_|     {ANSIColors.CITALIC}{uptime}{bcolors.ENDC}{color}
		'''

	return logo


def main():
	fetch = Fetch()

	local_ip, hostname, os_version = fetch.local_ip(), fetch.hostname(), fetch.os_version()
	uptime, screen_size = fetch.uptime(), fetch.screen_size()

	print(get_logo('boldgrey', local_ip, hostname, os_version, screen_size, uptime))


if __name__ == '__main__':
	main()
