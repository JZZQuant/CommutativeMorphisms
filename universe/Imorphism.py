'''
Created on May 4, 2016

@author: euler
'''
from abc import ABCMeta 

class IMorphism(object):
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta


    def inner(self, left,right):
        '''
        Constructor
        '''
        pass
    
    def outer(self, left,right):
        '''
        Constructor
        '''
        pass
    
    def inverse(self, left,right):
        '''
        Constructor
        '''
        pass