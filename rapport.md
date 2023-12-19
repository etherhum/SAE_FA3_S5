# SAE - BUT3 - F3
## Rapport de projet
### Paul Montagnac, FA-3

---
## Enoncé
Le projet consiste à mettre en place une interface web, permettant d'exécuter 3 modules. L'interface doit être déployable sur en production sur un système linux.

Les 3 modules à développer sont les suivants:
- Ping: L'utilisateur peut saisir une adresse dans un champ et effectuer un ping
- IPv6: Simplifier l'écriture d'une adresse IPv6 ou l'écrire en entier en fonction de l'adresse entrée. Le binaire des deux octets les plus significatifs de l'adresse seront également affichés.
- IPv4: L'utilisateur obtiens une division en sous-réseaux logique d'une adresse IP donnée ainsi qu'un masque écrit en notation CIDR
---
## Installation
### Prérequis
- Python 3.6 ou supérieur (`sudo apt-get install python3`)
- pip (`sudo apt-get install python3-pip`)
- Cloner le dépôt git (`git clone https://github.com/etherhum/SAE_FA3_S5.git`)
### Installation

#### Automatique
- Lancer le script **install.sh** (`./install.sh`)
  - Si nécessaire utiliser `sudo chmod +x install.sh` pour rendre le script exécutable

#### Manuel
- Installer les dépendances python (`pip3 install -r requirements.txt`)
- Démarrer le script python (`python3 main.py`)

---
## Utilisation
- Le lancement se fait avec `python app.py`
- Le serveur est ensuite accessible depuis l'adresse suivante: http://127.0.0.1:5000
---

## Fonctionnement
L'accès au serveur web se fait à l'aide du module Flask, basé sur le moteur de template Jinja2. Le module Flask permet de définir des routes entre les différentes pages du site web, et de définir des fonctions à exécuter lors de l'accès à ces routes. Les pages HTML sont stockées dans un dossier template.

Le style est défini simplement avec le framework csspico, qui s'importe simplement dans les balises `<head>` des fichiers html.

Ces différentes technologies étaient utilisées en cours l'année au S4, ce qui m'as permis de les réutiliser simplement dans le cadre de ce projet.

Les différents modules sont implémentés en Python (qui permet d'effectuer les différentes commandes shell nécessaires) et sont appelés depuis le script python principal (app.py).
### Ping
Le module ping est implémenté à l'aide du module `subprocess` de python, qui permet d'exécuter des commandes shell depuis un script python. La commande ping est exécutée avec l'option `-c 4` pour limiter le nombre de paquets envoyés à 4. Le résultat est affiché dans la page `ping.html`.
### IPv6
Le module IPv6 est implémenté à l'aide du module `ipaddress` de python, qui permet de manipuler des adresses IPv6. Le module permet de simplifier une adresse IPv6, ou de l'écrire en entier en fonction de l'adresse entrée. Le binaire des deux octets les plus significatifs de l'adresse seront également affichés dans la page `ipv6.html`.
### IPv4
Le module IPv4 est également implémenté à l'aide du module `ipaddress` de python. Le module permet d'obtenir une division en sous-réseaux logique d'une adresse IP donnée ainsi qu'un masque écrit en notation CIDR. Le résultat est affiché dans la page `ipv4.html`.

Le code est python est commenté pour le rendre plus compréhensible.

---
## Questions
En cas de questions ou problèmes, vous pouvez me contacter à l'adresse suivante: `montagnac.paul@hotmail.fr`.
