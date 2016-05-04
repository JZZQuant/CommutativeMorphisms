import unittest
import helper
import LambdaCategory as lcb


class CMBTest(unittest.TestCase):
    def test_complex(self):
        expression = '(a & (!b | b)) | (!a & (!b | b))'.replace(' ','')
        Builder=lcb.LambdaCategoryBuilder(expression)
        given=Builder.evaluate()
        self.assertTrue(given)

    def test_startingBrackets(self):
        expression = '(!b | b)'.replace(' ','')
        Builder=lcb.LambdaCategoryBuilder(expression)
        given=Builder.evaluate()
        self.assertTrue(given)

    def test_startingnot(self):
        expression = '!(b & !b)'.replace(' ','')
        Builder=lcb.LambdaCategoryBuilder(expression)
        given=Builder.evaluate()
        self.assertTrue(given)

if __name__ == '__main__':
    unittest.main()
