#!/bin/bash
# Developer: Derxs

sleep 0.5
echo -e "\033[01;36m
------------------------------
╦  ┌─┐┌─┐╔═╗┬ ┬
║  │ ││  ╠═╝└┬┘
╩═╝└─┘└─┘╩   ┴  by Derxs v1.0
------------------------------
           INSTALL
\033[00;00m"
sleep 0.5

echo -e "\033[01;34m[+]\033[00;00m Instalação em andamento..."

sudo apt-get install python3 python3-pip -y > /dev/null
if [[ $? == 0 ]];then
	sudo pip3 install bs4 2> /dev/null
	if [[ $? == 0 ]];then
		echo -e "\033[01;32m[*]\033[00;00m Instalação concluída com sucesso!"
	else
		echo -e "\033[01;31m[!]\033[00;00m Módulo não instalado!"
	fi
else
	echo -e "\033[01;31m[!]\033[00;00m Houve um erro durante a instalação!"
fi
