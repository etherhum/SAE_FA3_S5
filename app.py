from flask import Flask, render_template, request
import subprocess
import ipaddress

app = Flask(__name__)


@app.route('/')  # Page d'accueil
def home():
    return render_template('index.html')  # Redirige vers la page index.html


@app.route('/ping', methods=['POST'])  # Page ping
def routePing():
    """ Fonction qui permet de récupérer l'IP ou le nom de domaine entré par l'utilisateur et de lancer la fonction ping

    :return: Affiche le résultat de la fonction ping dans la page ping.html
    """
    if request.method == 'POST':  # Si la méthode est POST, alors on lance la fonction ping avec l'host en paramètre
        host = request.form['host']
        result = ping(host)
        return render_template('ping.html', host=host, result=result)  # Redirige vers ping.html


def ping(host):
    """ Fonction qui permet de lancer la commande ping avec l'adresse IP ou le nom de domaine en paramètre

    :param host: Adresse IP ou nom de domaine
    :return: Résultat de la commande ping
    """
    try:  # On essaye de lancer la commande ping avec l'adresse IP ou le nom de domaine en paramètre
        result = subprocess.check_output(['ping', '-c', '4', host], universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"


@app.route('/ipv6', methods=['POST'])
def routeIpv6():
    """ Fonction qui permet de récupérer l'adresse IPv6 entrée par l'utilisateur

    :return: Affiche le résultat de la fonction ipv6 dans la page ipv6.html
    """
    if request.method == 'POST':
        ipv6_address = request.form['ipv6']
        simplified_ipv6, binary_octets = ipv6(ipv6_address)
        return render_template('ipv6.html', ipv6_address=ipv6_address, simplified_ipv6=simplified_ipv6,
                               binary_octets=binary_octets)


def ipv6(ipv6_address):
    """ Fonction qui permet de simplifier l'adresse IPv6 et de la convertir en binaire

    :param ipv6_address: Adresse IPv6
    :return: Adresse IPv6 simplifiée et en binaire
    """
    simplified_ipv6 = ipv6_address.upper().replace(":", "")
    binary_octets = ''.join(format(int(octet, 16), '08b') for octet in simplified_ipv6[:4])
    return simplified_ipv6, binary_octets


@app.route('/ipv4', methods=['POST'])
def routeIpv4():
    """ Fonction qui permet de récupérer l'adresse IP et le masque CIDR entrés par l'utilisateur
    :return: Affiche le résultat de la fonction ipv4 dans la page ipv4.html
    """
    if request.method == 'POST':
        ip_address = request.form['ip']
        cidr_mask = request.form['cidr']
        subnets = ipv4(ip_address, cidr_mask)
        return render_template('ipv4.html', ip_address=ip_address, cidr_mask=cidr_mask, subnets=subnets)


def ipv4(ip_address, cidr_mask):
    """ Fonction qui permet de calculer les sous-réseaux d'une adresse IP et d'un masque CIDR
    :param ip_address:
    :param cidr_mask:
    :return: Sous-réseaux
    """
    network = ipaddress.IPv4Network(f"{ip_address}/{cidr_mask}", strict=False)
    subnets = [str(subnet) for subnet in network.subnets()]
    return subnets


if __name__ == '__main__':
    app.run(debug=True)
