# coding: utf-8

__author__ = 'Yemilice_lau'

from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:7900', allow_none=True)

s.PrintWork("Good job")
