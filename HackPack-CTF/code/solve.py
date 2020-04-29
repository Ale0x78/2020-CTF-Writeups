#!/usr/bin/env python3
import socket

target = ("cha.hackpack.club", 41709)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(target)

DEBUG   = b'\x00\x00\x00\x2a\x00\x00'
QUOTE   = b'\x00\x00\x00\x14\x00\x00\x00\x00'
ECHO    = b'\x00\x00\x00\x0a\x00\x00'


def display(s):
  print(b"[+] Got back: " + s)
def de(s):
  print(b"[-] Sending: " + s)
def get_echo_command(s):
  return ECHO + len(s).to_bytes(2, 'big') + s

def get_echo(soc, bytes):
  txt = get_echo_command(bytes)
  de(txt)
  soc.send(txt)
  return soc.recv(1024)

def get_quote(soc):
  de(QUOTE)
  soc.send(QUOTE)
  return soc.recv(1024)


def get_debug(soc, text=b'test'):
  txt = DEBUG + len(text).to_bytes(2, 'big') + text
  de(txt)
  soc.send(txt)
  return soc.recv(1024)

print(s.recv(1024).decode('utf-8'))

display(get_debug(s, b'old'))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))
display(get_quote(s))




