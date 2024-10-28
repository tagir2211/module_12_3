from runner import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
  is_frizen = True
  @classmethod
  def setUpClass(cls):
    cls.all_results = {}

  def setUp(self):
    self.runner1 = Runner("Усейн", 10)
    self.runner2 = Runner("Андрей", 5)
    self.runner3 = Runner("Ник", 3)
  @unittest.skipIf(is_frizen, 'Тесты в этом кейсе заморожены')
  def test_start_1(self):
    self.tour = Tournament(90, self.runner1, self.runner3) 
    self.all_results[1] = self.tour.start()
    max_key = max(self.all_results[1].keys())
    self.assertTrue(self.runner3 == self.all_results[1][max_key])

  @unittest.skipIf(is_frizen, 'Тесты в этом кейсе заморожены')
  def test_start_2(self):
    self.tour = Tournament(90, self.runner2, self.runner3) 
    self.all_results[2] = self.tour.start()
    max_key = max(self.all_results[2].keys())
    self.assertTrue(self.runner3 == self.all_results[2][max_key])

  @unittest.skipIf(is_frizen, 'Тесты в этом кейсе заморожены')
  def test_start_3(self):
    self.tour = Tournament(90, self.runner1, self.runner2, self.runner3) 
    self.all_results[3] = self.tour.start()
    max_key = max(self.all_results[3].keys())
    self.assertTrue(self.runner3 == self.all_results[3][max_key])
  
  @classmethod
  def tearDownClass(cls):
    for result in cls.all_results.values():
      for key, runner in result.items():
        print(f'{key} место - {runner}; ', end='')
      print()

if __name__ == "__main__":
  unittest.main()
    