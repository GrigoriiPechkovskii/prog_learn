#!/usr/bin/env python3
#https://rtfm.co.ua/python-modul-argparse-opcii-komandnoj-stroki-v-primerax/
import sys
print('start')

sys.argv = ['./arg_l.py', '-1', 'two', 'three', '3'] 



import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-1', '--one', help='This will be option One')
parser.add_argument('two', help='This will be option two')
parser.add_argument('three', help='This will be option three')

print ('parser---',parser.parse_args())

print('sys---',sys.argv)

print('end')

