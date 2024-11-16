import Runner
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner.Runner('Усейн', 10)
        self.runner_2 = Runner.Runner('Андрей', 9)
        self.runner_3 = Runner.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        return (cls.all_results)

    def test_tour_1(self):
        tour_1 = Runner.Tournament(90, self.runner_1, self.runner_3)
        t1_result = {k: str(v) for k, v in tour_1.start().items()}
        self.all_results.update(t1_result)
        self.assertTrue(t1_result[2], 'Ник')
        print(self.all_results)

    def test_tour_2(self):
        tour_2 = Runner.Tournament(90, self.runner_2, self.runner_3)
        t2_result = {k: str(v) for k, v in tour_2.start().items()}
        self.all_results.update(t2_result)
        self.assertTrue(t2_result[2], 'Ник')
        print(self.all_results)

    def test_tour_3(self):
        tour_3 = Runner.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        t3_result = {k: str(v) for k, v in tour_3.start().items()}
        self.all_results.update(t3_result)
        self.assertTrue(t3_result[2], 'Ник')
        print(self.all_results)


if __name__ == '__main__':
    unittest.main()
