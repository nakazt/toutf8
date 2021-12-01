#! /usr/bin/env python3

import os

def main():

  files = os.listdir('.\sjis')
  for file in files:
    print(file)
    with open('.\\sjis\\' + file, encoding='shift_jis') as fi, open('.\\utf8\\' + file, 'w',encoding='utf-8') as fo:
      fo.write(fi.read())

if __name__ == '__main__':
  main()
