#!/usr/bin/python
# -*- coding: utf-8 -*-

arquivo = open('teste','r')
urls = []

for u in arquivo:
    urls.append(u.strip())

print urls
