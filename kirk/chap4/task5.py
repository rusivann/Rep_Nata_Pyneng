#!/usr/bin/env python3
import re

f = open('show_ipv6_intf.txt')
show = f.readlines()

for line in show:
# комент для регулярки - берём от начала строки любое количетсво пробелов, любое количество не пробелов,
# затем : и любое количество любых символов до /, после которого идёт любое количество цифр.
# Флаг dotall используем т.к. line - это raw string, т.е. строка, игнорирующая спецсимволы.
	match = re.search(r'^(\s+)(\S+):(.*)/(\d+)', line, flags = re.DOTALL)
	if match:
		print(match.group(0))

