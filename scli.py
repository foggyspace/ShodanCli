import argparse

from ShodanCli import parse_shodan_host_banner_info, lookup_a_host, searching_shodan

__version__ = '0.0.1'
__author__ = 'seaung'


# colors
W = '\033[0m'
G = '\033[1;32m'
R = '\033[1;31m'
O = '\033[1;33m'
B = '\033[1;34m'


def print_help():
    helps = '''
            >>> python scli.py -ip 192.168.2.101
            >>> python scli.py -host www.baidu.com
            >>> python scli.py -search nginx
    '''


def banner():
    print(G + '''
          version : {}
          author  : {}
     _               _                    _ _
 ___| |__   ___   __| | __ _ _ __     ___| (_)
/ __| '_ \ / _ \ / _` |/ _` | '_ \   / __| | |
\__ \ | | | (_) | (_| | (_| | | | | | (__| | |
|___/_| |_|\___/ \__,_|\__,_|_| |_|  \___|_|_|
          '''.format(__version__, __author__) + R)


def main():
    '''
    主调函数
    :return: None
    '''
    try:
        add_parser_argument = argparse.ArgumentParser()

        add_parser_argument.add_argument('-ip', dest='ip', type=str, action='store')
        add_parser_argument.add_argument('-host', dest='host', type=str, action='store')
        add_parser_argument.add_argument('-search', dest='search', type=str, action='store')

        parser_args = add_parser_argument.parse_args()

        if parser_args.ip is None and parser_args.host is None and parser_args.search is None:
            print_help()
        elif parser_args.ip:
            parse_shodan_host_banner_info(parser_args.ip)
        elif parser_args.host:
            lookup_a_host(parser_args.host)
        elif parser_args.search:
            searching_shodan(parser_args.search)
    except KeyboardInterrupt:
        exit()


if __name__ == '__main__':
    banner()
    main()
