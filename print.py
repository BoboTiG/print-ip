#!/usr/bin/env python
# coding: utf-8
''' Impression et stockage des adresses IP.

    Script maintenu par Mickaël Schoentgen <mickael@jmsinfo.co>.
    Python 3.
'''

from configparser import Error, NoOptionError, SafeConfigParser

# Imports relatifs au projet Hermès
from thermalprinter import CodePage, ThermalPrinter

__all__ = ['']


__version__ = '0.0.1'
__author__ = 'Mickaël Schoentgen'
__copyright__ = '''
    Copyright (c) 2016, Mickaël 'Tiger-222' Schoentgen

    Permission to use, copy, modify, and distribute this software and its
    documentation for any purpose and without fee or royalty is hereby
    granted, provided that the above copyright notice appear in all copies
    and that both that copyright notice and this permission notice appear
    in supporting documentation or portions thereof, including
    modifications, that you make.
'''


def main(args):
    ''' . '''

    fo_ip = '/opt/hermes/stats/ip.ini'
    ini = SafeConfigParser()
    ini.read(fo_ip)

    with ThermalPrinter() as printer:
        printer.fo_stats = None
        if not printer.status()['paper']:
            return 1

        printer.justify('R')
        for arg in args:
            arg = arg.replace('|', ' ').strip()
            if arg:
                iface, ip = arg.split(' ')
                ini.set(iface.lower(), 'ip', ip)
                printer.write(arg.encode('latin-1'))
                printer.feed()
        printer.justify()
        printer.feed(3)

        ini.write(open(fo_ip, 'w'))

    return 1

if __name__ == '__main__':
    from sys import argv
    exit(main(argv[1:]))
