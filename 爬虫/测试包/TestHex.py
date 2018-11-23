#!/usr/bin/env python
# -*- coding:utf-8 -*-

def bin_to_str(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])


def str_to_bin(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])


def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(' ')]])


def str_to_hex(s):
    return ' '.join([hex(ord(c)).replace('0x', '') for c in s])


str = str_to_hex('wan131')
print(str)
str = "77 61 6e "
str = hex_to_str(str)
print(str)
str = str_to_bin('wan')
print(str)
str = bin_to_str(str)
print(str)
