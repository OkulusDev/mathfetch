#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import platform
import subprocess
import socket
from random import choice, randint


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


class Quote:
	def __init__(self):
		self.quotes = [
			'Математика - единственный совершенный метод, позволяющий провести самого себя за нос. Альберт Эйнштейн',
			'Математика выявляет порядок, симметрию и определённость, а это – важнейшие виды прекрасного. Аристотель',
			'Математика - это искусство называть разные вещи одним и тем же именем. Анри Пуанкаре',
			'Математика — это доказательство самых очевидных вещей наименее очевидным способом. Джордж Пойа',
			'Законы математики, имеющие какое-либо отношение к реальному миру, ненадежны; а надежные математические законы не имеют отношения к реальному миру. Альберт Эйнштейн',
			'В математических вопросах нельзя пренебрегать даже с самыми мелыми ошибками. Исаак Ньютон',
			'Математика скучна только для тех, кто не может понять ее. Okulus Dev',
			'Математики – вроде французов: когда говоришь с ними, они переводят твои слова на свой язык и сразу получается что-то совсем другое Иоганн Гёте',
			'Математика - самая надежная форма пророчества. Вильгельм Швебель',
			'В математике нет символов для неясных мыслей. Анри Пуанкаре',
			'Великая книга природы написана математическими символами. Галилей',
			'Предмет математики настолько серьезен, что полезно не упустить случая сделать его немного занимательным. Блес Паскаль'
		]

		self.other_quotes = """Математика - это язык, на котором написана книга природы. (Г. Галилей)
Математика – царица наук, арифметика – царица математики. (К.Ф. Гаусс)
Кто с детских лет занимается математикой, тот развивает внимание, тренирует свой мозг, свою волю, воспитывает на­стойчивость и упорство в достижении цели. (А. Маркушевич)
«Числа управляют миром», – говорили пифагорейцы. Но числа дают возможность человеку управлять миром, и в этом нас убеждает весь ход развития науки и техники наших дней. (А. Дородницын)
Рано или поздно всякая правильная математическая идея находит применение в том или ином деле. (А.Н. Крылов)
Если вы хотите участвовать в большой жизни, то наполняйте свою голову математикой, пока есть к тому возможность. Она окажет вам потом огромную помощь во всей вашей работе. (М.И. Калинин)
Разве ты не заметил, что способный к математике изощрен во всех науках в природе? (Платон)
Было бы хорошо, если бы эти знания требовало само госу­дарство и если бы лиц, занимающих высшие государственные должности, приучали заниматься математикой и в нужных случаях к ней обращаться. (Платон)
Науки математические с самой глубокой древности обращали на себя особенное внимание, в настоящее время они полу­чили еще больше интереса по влиянию своему на искусство и промышленность. (П.Л. Чебышев)
Математика есть лучшее и даже единственное введение в изу­чение природы. (Д.И. Писарев)
Астрономия (как наука) стала существовать с тех пор, как она соединилась с математикой. (А.И. Герцен)
Полет – это математика. (В. Чкалов)
Вдохновение нужно в геометрии не меньше, чем в поэзии. (А.С. Пушкин)
Геометрия полна приключений, потому что за каждой задачей скрывается приключение мысли. Решить задачу – это значит пережить приключение. (В. Произволов)
В математике есть своя красота, как в живописи и поэзии. (Н.Е. Жуковский)
Химия – правая рука физики, математика – ее глаз. (М.В. Ломоносов)
Математику уже затем учить надо, что она ум в порядок приводит. (М.В. Ломоносов)
Я люблю математику не только потому, что она находит применение в технике, но и потому, что она красива. (Р. Петер) Все, что до этого было в науках: гидравлика, аэрометрия, оп­тика и других темно, сомнительно и недостоверно, математика сделала ясным, верным и очевидным. (М.В. Ломоносов)
Стремящийся к ближайшему изучению химии должен быть сведущ и в математике. (М.В. Ломоносов)
Слеп физик без математики. (М.В. Ломоносов)
Математик, который не является в известной мере поэтом, никогда не будет настоящим математиком. (К. Вейерштрасс)
Математика - это язык, на котором говорят все точные науки. (Н.И. Лобачевский)
Только с алгеброй начинается строгое математическое учение. (Н.И. Лобачевский)
Как бы машина хорошо ни работала, она может решать все требуемые от нее задачи, но она никогда не придумает ни од­ной. (А. Эйнштейн)
Именно математика дает надежнейшие правила: кто им следует – тому не опасен обман чувств. (Л. Эйлер)
Цифры (числа) не управляют миром, но они показывают, как управляется мир. (И. Гете)"""
		for quote in self.other_quotes.split('\n'):
			self.quotes.append(quote)

	def get_quote(self):
		return f'󰍡  󰝗 {choice(self.quotes)} 󰉾'


def get_logo(color: str, local_ip, hostname, os_version, screen_size, uptime, logotype) -> str:
	color = color.strip().lower()
	quote = Quote()

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
	elif color == 'default':
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
                                {quote.get_quote()}
'''

	logo2 = f'''{color}
___  ___      _   _           {ANSIColors.CITALIC}{hostname}{bcolors.ENDC}{color}
|  \\/  |     | | | |         {ANSIColors.CBOLD}{"" * hostname_len}{bcolors.ENDC}{color}
| .  . | __ _| |_| |__       {ANSIColors.CITALIC}{local_ip}{bcolors.ENDC}{color}
| |\\/| |/ _` | __| '_ \\      {ANSIColors.CITALIC}{os_version}{bcolors.ENDC}{color}
| |  | | (_| | |_| | | |     {ANSIColors.CITALIC}{screen_size}{bcolors.ENDC}{color}
\\_|  |_/\\__,_|\\__|_| |_|     {ANSIColors.CITALIC}{uptime}{bcolors.ENDC}{color}
                             {quote.get_quote()}
'''

	logo3 = f'''{color}
███╗   ███╗ █████╗ ████████╗██╗  ██╗     {ANSIColors.CITALIC}{hostname}{bcolors.ENDC}{color}
████╗ ████║██╔══██╗╚══██╔══╝██║  ██║     {ANSIColors.CBOLD}{"" * hostname_len}{bcolors.ENDC}{color}
██╔████╔██║███████║   ██║   ███████║     {ANSIColors.CITALIC}{local_ip}{bcolors.ENDC}{color}
██║╚██╔╝██║██╔══██║   ██║   ██╔══██║     {ANSIColors.CITALIC}{os_version}{bcolors.ENDC}{color}
██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║     {ANSIColors.CITALIC}{screen_size}{bcolors.ENDC}{color}
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝     {ANSIColors.CITALIC}{uptime}{bcolors.ENDC}{color}
                                         {quote.get_quote()}
'''

	logo4 = f'''{color}
    __  ___      __  __       {ANSIColors.CITALIC}{hostname}{bcolors.ENDC}{color}
   /  |/  /___ _/ /_/ /_      {ANSIColors.CBOLD}{"" * hostname_len}{bcolors.ENDC}{color}
  / /|_/ / __ `/ __/ __ \\     {ANSIColors.CITALIC}{local_ip}{bcolors.ENDC}{color}
 / /  / / /_/ / /_/ / / /     {ANSIColors.CITALIC}{os_version}{bcolors.ENDC}{color}
/_/  /_/\\__,_/\\__/_/ /_/      {ANSIColors.CITALIC}{screen_size}{bcolors.ENDC}{color}
                              {quote.get_quote()}
'''

	if logotype == 1:
		return logo
	elif logotype == 2:
		return logo2
	elif logotype == 3:
		return logo3
	elif logotype == 4:
		return logo4


def main():
	fetch = Fetch()

	local_ip, hostname, os_version = fetch.local_ip(), fetch.hostname(), fetch.os_version()
	uptime, screen_size = fetch.uptime(), fetch.screen_size()

	print(get_logo('default', local_ip, hostname, os_version, screen_size, uptime, randint(1, 4)))


if __name__ == '__main__':
	main()
