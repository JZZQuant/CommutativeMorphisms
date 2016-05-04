'''
Created on May 4, 2016

@author: euler
'''

class monoid(object):
    '''
    classdocs
    '''


    def __init__(self, left,condition,negate=0):
        '''
        Constructor
        '''    
        self.element=left
        self.condition=condition
        if negate==1 :self.element=helper.Negation(left)
        #print "added to stack "+ str(self.element ) + "with condition "+ str(self.condition)
