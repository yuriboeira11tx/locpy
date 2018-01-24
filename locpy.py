#coding: utf-8
# Developer: Derxs
# Version: 1.0
import requests, socket, time
from bs4 import BeautifulSoup

try:
	time.sleep(0.5)

	print('''\033[01;36m
╦  ┌─┐┌─┐╔═╗┬ ┬
║  │ ││  ╠═╝└┬┘
╩═╝└─┘└─┘╩   ┴  by Derxs v1.0
	\033[00;00m''')

	url = 'https://www.localizaip.com.br/localizar-ip.php?ip='
	
	time.sleep(0.5)

	website = input('\033[01;34m[+]\033[00;00m Website: ')

	ip_website = socket.gethostbyname(website)

	data = {'ip': '{}'.format(ip_website)}

	r = requests.get(url, params=data)

	soup = BeautifulSoup(r.text, 'lxml')

	print('\033[01;32m[*]\033[00;00m IP: {}'.format(ip_website))
	time.sleep(0.5)
	print('\033[01;32m[*]\033[00;00m Buscando localização...')

	soup = BeautifulSoup(r.text, 'lxml')

	lista = soup.find_all('span', class_='style4')

	dados_finais = []

	for dados in lista:
		lista_dados	= dados.find_all('b')
		for dado in lista_dados:
			dados_finais.append(dado.text)

	dados = {'ip': ip_website}

	response = requests.post('http://www.meuenderecoip.com/localizar-ip.php', data=dados)

	soup = BeautifulSoup(response.text, 'lxml')

	lista = soup.find_all('td')

	end = []

	for i in lista:
		resultado = str(i.string).split('\n')
		
		for a in range(len(resultado)):
			if resultado[a] == 'None' or resultado[a] == 'Localizar IP' or resultado[a] == 'Cidade' or resultado[a] == 'Região' or resultado[a] == 'País' or resultado[a] == 'Latitude' or resultado[a] == 'Longitude':
				pass
			else:
				end.append(resultado[a])
				if '\xa0' in end:
					end.remove('\xa0')
	
	time.sleep(0.5)
	
	print('\n\033[01;31mPaís: \033[01;32m{}\033[01;31m'.format(end[2]))
	print('Região: \033[01;32m{}\033[01;31m'.format(end[1]))
	print('Cidade: \033[01;32m{}\033[01;31m'.format(dados_finais[2]))
	print('Latitude: \033[01;32m{}\033[01;31m'.format(end[3]))
	print('Longitude: \033[01;32m{}\033[01;31m'.format(end[4]))
	print('Provedor: \033[01;32m{}\033[01;31m'.format(dados_finais[3]))
	print('IP-Reverso: \033[01;32m{}\033[00;00m\n'.format(dados_finais[4]))

except KeyboardInterrupt:
	print('\n\033[01;31m[!]\033[00;00m Você escolheu sair!')
