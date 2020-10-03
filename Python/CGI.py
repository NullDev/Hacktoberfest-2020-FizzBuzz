#!/usr/bin/python3.5
# -*- coding: UTF-8 -*-
import cgi
print("Content-Type: text/html")
number = 0
while 1 == 1:
  number += 1
  if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print("<b><i>fizzbuzz</i></b>")
        continue
  elif fizzbuzz % 3 == 0:
        print("<b>fizz</b>")
        continue
  elif fizzbuzz % 5 == 0:
        print("<i>buzz</i>")
        continue
        
