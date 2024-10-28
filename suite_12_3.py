import module_12_1, module_12_2

import unittest

testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)



