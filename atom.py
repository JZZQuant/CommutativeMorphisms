import helper

class atom(object):
    def __init__(self,left,condition,negate=0):
        self.element=left
        self.condition=condition
        if negate==1 :self.element=helper.Negation(left)
        #print "added to stack "+ str(self.element ) + "with condition "+ str(self.condition)
