from __future__ import print_function
from pprint import pprint
import os

import shodan
import requests
from requests.exceptions import ConnectionError, RequestException
from pyquery import PyQuery as pq


HEADERS = {"User-Agent": "__shodan__"}


SHODAN_API_KEY = os.getenv('SHODAN_API_KEY')

shodan_api = shodan.Shodan(SHODAN_API_KEY)


def get_shodan_host_banner_info(url):
    try:
        res = requests.get(url=url, headers=HEADERS, timeout=10)
        if res.status_code == 200:
            return res.text
    except (ConnectionError, RequestException) as e:
        print(f'[-] exception {e}')


def parse_shodan_host_banner_info(ip_address):

    try:
        url = f'https://www.shodan.io/host/{ip_address}'

        response = get_shodan_host_banner_info(url)

        doc = pq(response)

        information = {}

        desc = doc('table.table tr').items()

        services = doc('ul.services li').items()

        ports = doc('ul.ports li').items()

        ip = doc('div.row-fluid div.span6 div.page-header h2').text()

        information[ip] = ip

        for item in desc:
            city = item.find('th').text()
            country = item.find('th').text()
            organization = item.find('th').text()
            isp = item.find('th').text()
            last_update = item.find('th').text()
            asin = item.find('th').text()
            information['city'] = city
            information['country'] = country
            information['organization'] = organization
            information['isp'] = isp
            information['last_update'] = last_update
            information['asin'] = asin

        for port in ports:
            port_number = port.find('a').text()
            information['ports'] = port_number

        for service in services:
            port = service.find('div.port').text()
            protocol = service.find('div.protocol').text()
            state = service.find('div.state').text()
            service_link = service.find('a.link').attr('href')
            service_main = service.find('div.service-main h3').text()
            banner_info = service.find('div.service-main pre').text()

            information['port'] = port
            information['state'] = state
            information['protocol'] = protocol
            information['link'] = service_link
            information['service'] = service_main
            information['banner'] = banner_info

        pprint(f'''
               [*] found done !
                remote host information
                {information}
        ''')
    except Exception as e:
        print(f'[!] exception {e}')


def searching_shodan(keyword):
    try:
        items = shodan_api.search(keyword)
        pprint(f'''
            Found : {items['total']}
        ''')

        for item in items['matches']:
            pprint(f'''
                [*] found Ip address and banner
                IP : {item['ip_str']}
                Banner: {item['data']}
            ''')
    except (shodan.exception.APIError, shodan.exception.APITimeout) as e:
        print(f'[-] exception {e}')
        print(f'[-] not found.')


def lookup_a_host(hostname):
    try:
        host = shodan_api.host(hostname)
        pprint(f'''
            [*] found host ip address and banner
            IP : {host['ip_str']}
            Organization: {host.get('org', 'n/a')}
            Operating System: {host.get('os', 'n/a')}
        ''')

        for item in host['data']:
            pprint(f'''
                [*] found host !
                Port: {item['port']}
                Banner: {item['data']}
            ''')
    except shodan.APIError as e:
        print(f'[*] => APIError {e}')

