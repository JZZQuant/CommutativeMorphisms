import helper
import LambdaCategory as lcb

expression = '(a & (!b | b)) | (!a & (!b | b))'.replace(' ','')
#expression = '(!b | b)'.replace(' ','')
#expression = '!(b & !b)'.replace(' ','')
lcb=lcb.LambdaCategoryBuilder(expression)

print lcb.evaluate(expression).element
