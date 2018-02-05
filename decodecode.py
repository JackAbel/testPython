# /usr/bin/env python

CODEC = 'utf-8'
FILE = 'unicode.txt'

hello_out = u'Hello World\n'
byte_out = hello_out.encode(CODEC)
# f = open(FILE, "r")
# f.write(byte_out)
# f.close()

f = open(FILE, "r")
byte_in = f.read()
f.close()
hello_in = byte_in.decode(CODEC)
