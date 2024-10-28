import unittest

import runner


class RunnerTest(unittest.TestCase):
    is_frizen = False
    @unittest.skipIf(is_frizen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        '''
        Test class Runner, functoin walc
        :return:
        '''
        t_walk = runner.Runner('Test')
        for _ in range(1, 11):
            t_walk.walk()
        self.assertEqual(t_walk.distance, 50)

    @unittest.skipIf(is_frizen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        '''
        Test class Runner, functoin run
        :return:
        '''
        t_run = runner.Runner('Test')
        for _ in range(1, 11):
            t_run.run()
        self.assertEqual(t_run.distance, 100)

