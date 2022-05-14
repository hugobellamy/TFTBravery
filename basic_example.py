# -*- coding: utf-8 -*-
"""
Created on Sat May 14 22:26:33 2022

@author: Hugo
"""

import brave_autoload as br

br.update_lists()

def run():
    a,b,c = br.make_team()
    print('Origin : '+ a)
    print('Class  : '+ b)
    print('Carry  : '+ c)
    
run()
