#!/usr/bin/env python
# coding: utf-8

'''A Python SQLite Shell
'''

import sqlite3
import sys

__ver__ = '20140826'

__version__ = '0.0.1 build %s' % __ver__

PS1 = 'sql> '

if sys.version_info.major == 3:
    raw_input = input

def puts(s, end='\n'):
    if sys.version_info.major == 3:
        print (s, end)
    elif end == '\n':
        print s
    else:
        print s,

def slogan():
    puts('Welcome SQLite world!')
    puts('%s %s (%s), %s %s.' %
         ('PySqlite is version',
          sqlite3.version_info[0],
          sqlite3.version,
          'compiled and linked to use version SQLite',
          sqlite3.sqlite_version))
    puts('Type ? for help.  And be bold!\n')

def farewell():
    puts('Have a lot of fun!\n')

def help():
    puts('''\
Simple SQLite shell  Version %s

A very simple SQLite shell which creates a database in memory to show how to using the SQLite DB-API.

Command  Description
==========================================
help     Print help information
EXIT     Quit this application immediately

Example SQLite commands:

# Create table
CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)

# Insert a row of data
INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
INSERT INTO stocks VALUES ('2006-01-31', 'SELL', 'UNIX', 20000, 99.99)
INSERT INTO stocks VALUES ('2006-03-28', 'BUY', 'IBM', 1000, 45.00)
INSERT INTO stocks VALUES ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00)
INSERT INTO stocks VALUES ('2006-04-06', 'SELL', 'IBM', 500, 53.00)

SELECT * FROM stocks WHERE symbol='RHAT'

SELECT * FROM stocks ORDER BY price
''' % __version__)

def main():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    while True:
        cmd = raw_input(PS1).strip()
        if cmd.upper() in ['BY', 'BYE', 'QUIT', 'FAREWELL', 'EXIT']:
            break
        elif cmd.lower() in ['?', 'h', 'help']:
            help()
        else:
            try:
                c.execute(cmd)
                if cmd.startswith('SELECT '):
                    puts(c.fetchall())
            except sqlite3.Error as e:
                puts('An error occurred: %s' % e.args[0])
    # Done and close the connection.
    conn.close()

if __name__ == "__main__":
    slogan()
    main()
    farewell()

