import argparse
import subprocess

from ShodanCli import parse_shodan_host_banner_info, lookup_a_host, searching_shodan

__version__ = '0.0.1'
__author__ = 'seaung'


def banner():
    print(f'''
          version : {__version__}
          author  : {__author__}
               _               _                    _ _
 ___| |__   ___   __| | __ _ _ __     ___| (_)
/ __| '_ \ / _ \ / _` |/ _` | '_ \   / __| | |
\__ \ | | | (_) | (_| | (_| | | | | | (__| | |
|___/_| |_|\___/ \__,_|\__,_|_| |_|  \___|_|_|
          ''')


def main():
    add_parser_argument = argparse.ArgumentParser()

    add_parser_argument.add_argument('-ip', dest='ip', type=str, action='store')
    add_parser_argument.add_argument('-host', dest='host', type=str, action='store')
    add_parser_argument.add_argument('-search', dest='search', type=str, action='store')

    parser_args = add_parser_argument.parse_args()

    if parser_args.ip:
        parse_shodan_host_banner_info(parser_args.ip)
    else:
        pass

    if parser_args.host:
        lookup_a_host(parser_args.host)
    else:
        pass

    if parser_args.search:
        searching_shodan(parser_args.search)
    else:
        pass

if __name__ == '__main__':
    banner()
    main()
