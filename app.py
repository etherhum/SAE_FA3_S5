from flask import Flask, render_template, request
import subprocess
import ipaddress

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ping', methods=['POST'])
def routePing():
    if request.method == 'POST':
        host = request.form['host']
        result = ping(host)
        return render_template('ping.html', host=host, result=result)


def ping(host):
    try:
        result = subprocess.check_output(['ping', '-c', '4', host], universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"


@app.route('/ipv6', methods=['POST'])
def routeIpv6():
    if request.method == 'POST':
        ipv6_address = request.form['ipv6']
        simplified_ipv6, binary_octets = ipv6(ipv6_address)
        return render_template('ipv6.html', ipv6_address=ipv6_address, simplified_ipv6=simplified_ipv6,
                               binary_octets=binary_octets)


def ipv6(ipv6_address):
    simplified_ipv6 = ipv6_address.upper().replace(":", "")
    binary_octets = ''.join(format(int(octet, 16), '08b') for octet in simplified_ipv6[:4])
    return simplified_ipv6, binary_octets


@app.route('/ipv4', methods=['POST'])
def routeIpv4():
    if request.method == 'POST':
        ip_address = request.form['ip']
        cidr_mask = request.form['cidr']
        subnets = ipv4(ip_address, cidr_mask)
        return render_template('ipv4.html', ip_address=ip_address, cidr_mask=cidr_mask, subnets=subnets)


def ipv4(ip_address, cidr_mask):
    network = ipaddress.IPv4Network(f"{ip_address}/{cidr_mask}", strict=False)
    subnets = [str(subnet) for subnet in network.subnets()]
    return subnets


if __name__ == '__main__':
    app.run(debug=True)
