# -*- coding: utf-8 -*-

import urllib.request
import os

# proxy = urllib.request.ProxyHandler({'http': '202.211.8.4:8080'})
# opener = urllib.request.build_opener(proxy)
# urllib.request.install_opener(opener)

dict1={1:"fm_",2:"la_",3:"di_1_",4:"di_2_",5:"ps_",6:"am_"}
dict2={1:"_p",2:"_q"}

targ_dir="./Todoroki/"

if not os.path.exists(targ_dir):
    os.mkdir(targ_dir)
for i in range(1,7):
    if not os.path.exists(targ_dir+(dict1[i])[:-1]):
        os.mkdir(targ_dir+(dict1[i])[:-1])
    for j in range(1,4):
        for k in range(1,10):
            for m in range(1,20):
                if j!=3:
                    url  = "http://www5a.biglobe.ne.jp/~todoroki/data/"+dict1[i]+"t_"+str(k)+"_"+str(m)+dict2[j]+".pdf"
                elif j==3:
                    url ="http://www5a.biglobe.ne.jp/~todoroki/data/"+dict1[i]+"p_"+str(k)+"_"+str(m)+".pdf"
                print(url)
                try:
                    urllib.request.urlretrieve(url, targ_dir+(dict1[i])[:-1]+url[41:])
                except urllib.error.URLError:
                    break