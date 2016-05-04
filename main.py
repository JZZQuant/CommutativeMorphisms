import helper
import LambdaCategory as lcb

if __name__ == '__main__':
    expression = '!(b & !b)'.replace(' ','')
    lcb=lcb.LambdaCategoryBuilder(expression)
    print lcb.evaluate()
