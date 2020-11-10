# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:37:12 2020

@author: s.granel
"""
import md5

total = ""
i = 1
result_file = open('digest.txt', 'w')

while i <= 1000 :
    digest_file  = open('test'+str(i)+'.txt', 'r')
    print(digest_file)
    chaine_digest = digest_file.read()
   # chaine_digest= '    <b>message-digest: </b><span id="partial-proof">c3f54f53b8181ce8a2fa3a3c02d67184</span>'
    array = chaine_digest.split('"')
    sub_array = array[2][1:]
    temp = sub_array.split('<')
    total = temp[0]
    print(total)
    i = i + 1
    result_file.write(total)
    digest_file.close()
result_file.close()


md5_file = open('digest.txt', 'r')
to_md5 = md5_file.read()

m = md5.new()
m.update(to_md5)
print (m.hexdigest())