import unittest
import Runner
from russian_names import RussianNames
import random


class RunnerTest(unittest.TestCase):
    is_frozen = False
    def test_walk(self):
        runner_1 = Runner.Runner(random.choice(list_names))
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)


    def test_run(self):
        runner_2 = Runner.Runner(random.choice(list_names))
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)


    def test_challenge(self):
        runner_3 = Runner.Runner(random.choice(list_names))
        runner_4 = Runner.Runner(random.choice(list_names))
        for _ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)



class TournamentTest(unittest.TestCase):
    is_frozen = True
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

    @unittest.skip(f'Тесты в этом кейсе заморожены')
    def test_tour_1(self):
        tour_1 = Runner.Tournament(90, self.runner_1, self.runner_3)
        t1_result = {k: str(v) for k, v in tour_1.start().items()}
        self.all_results.update(t1_result)
        self.assertTrue(t1_result[2], 'Ник')

    @unittest.skip(f'Тесты в этом кейсе заморожены')
    def test_tour_2(self):
        tour_2 = Runner.Tournament(90, self.runner_2, self.runner_3)
        t2_result = {k: str(v) for k, v in tour_2.start().items()}
        self.all_results.update(t2_result)
        self.assertTrue(t2_result[2], 'Ник')

    @unittest.skip(f'Тесты в этом кейсе заморожены')
    def test_tour_3(self):
        tour_3 = Runner.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        t3_result = {k: str(v) for k, v in tour_3.start().items()}
        self.all_results.update(t3_result)
        self.assertTrue(t3_result[2], 'Ник')


if __name__ == '__main__':
    unittest.main()
list_names = []
rn = RussianNames(count=10, patronymic=False, surname=False, gender=1)
for person in rn:
    list_names.append(person)
