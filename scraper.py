# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:23:28 2017

@author: jaydeep thik
"""

import os
import requests
from bs4 import BeautifulSoup

def search(item):
    path = os.getcwd()
    dirs = os.listdir()
    if item not in dirs:
        os.mkdir(item)
    image_dir = path+'/'+item
    
    os.chdir(image_dir)
    
    
    if ' ' in item:
        pholder = item.replace(' ','+')
    r = requests.get('https://www.google.co.in/search?q='+pholder+'&hl=en&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjfpOeo9_nXAhWHtY8KHWm5CEAQ_AUICigB&biw=1366&bih=598#imgrc=x_7gN_kuIgT94M:')
    data = r.text
    
    soup = BeautifulSoup(data,'lxml')
    iid=0
    for link in soup.findAll('img'):
        image = link.get('src')
        
        r2 = requests.get(image)
        
        with open(item+'_'+str(iid)+'.png','wb') as f:
            f.write(r2.content)
        iid+=1
        
    os.chdir(path)
        
        
        