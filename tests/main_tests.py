import unittest
from tests.test_1 import MyTestCaseForAtoB
from tests.test_2 import MyTestCaseForOtoE
from tests.test_3 import MyTestCaseForGtoZ
from tests.test_4 import MyTestCaseForNtoD
from tests.test_5 import MyTestCaseForMtoF


def tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MyTestCaseForAtoB))
    suite.addTest(unittest.makeSuite(MyTestCaseForOtoE))
    suite.addTest(unittest.makeSuite(MyTestCaseForGtoZ))
    suite.addTest(unittest.makeSuite(MyTestCaseForNtoD))
    suite.addTest(unittest.makeSuite(MyTestCaseForMtoF))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)


if __name__ == '__main__':
    tests()
