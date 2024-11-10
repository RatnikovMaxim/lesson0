import Runner
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = Runner.Runner('Усейн', 10)
        self.runner_2 = Runner.Runner('Андрей', 9)
        self.runner_3 = Runner.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    def tour_test_1(self):
        tour_1 = Runner.Tournament(90, self.runner_1, self.runner_3)
        t1_result = {k: str(v) for k, v in tour_1.start().items()}
        self.all_results.append(t1_result)
        self.assertTrue(t1_result[2], 'Ник')



if __name__ == '__main__':
    unittest.main()