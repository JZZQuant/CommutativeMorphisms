import helper
import atom as at
class LambdaCategoryBuilder(object):
    def __init__(self,expression):
        self.dualspace=helper.duality(expression)

    def stackCollapse(self,stack,symbol,fun,isLastinEngine):
        orstack=[]
        i=0
        while i+1<len(stack):
            if stack[i].condition!=symbol:orstack.append(stack[i])
            else:stack[i+1]=at.atom(fun(stack[i].element,stack[i+1].element),stack[i+1].condition)
            i=i+1
        if not isLastinEngine:
            orstack.append(stack[-1])
            return orstack
        else: return stack

    def reduceExp(self,fullstack):
        orstack=self.stackCollapse(fullstack,'&',helper.And,False)
        return self.stackCollapse(orstack,'|',helper.Or,True)[-1]

    def evaluate(self,expression):
        fullstack=[]
        if len(expression)<3:fullstack.append(at.atom(self.dualspace[expression[0]],-1,len(expression)-1))
        else:
            left=expression.find("(")
            if left not in [0,1]:
                negate=int(expression[0]=='!')
                fullstack.append(at.atom(self.dualspace[expression[0+negate]],expression[1+negate],negate))
                fullstack.append(self.evaluate(expression[2+negate:]))
            else:
                pos=helper.closure(expression,left)
                if len(expression)==pos:fullstack.append(at.atom(self.evaluate(expression[1+left:pos-1]).element,-1,left))
                else:
                    fullstack.append(at.atom(self.evaluate(expression[1+left:pos-1]).element,expression[pos],left))
                    fullstack.append(self.evaluate(expression[pos+1:]))

        return self.reduceExp(fullstack)
