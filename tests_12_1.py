import Runner
import unittest
from russian_names import RussianNames
import random


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = Runner.Runner(random.choice(list_names))
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)
        print(runner_1)

    def test_run(self):
        runner_2 = Runner.Runner(random.choice(list_names))
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)
        print(runner_2)

    def test_challenge(self):
        runner_3 = Runner.Runner(random.choice(list_names))
        runner_4 = Runner.Runner(random.choice(list_names))
        for _ in range(10):
            runner_3.run()
            runner_4.walk()
        self.assertNotEqual(runner_3.distance, runner_4.distance)
        print(f'{runner_3}, {runner_4}')


if __name__ == '__main__':
    unittest.main()
list_names = []
rn = RussianNames(count=9, patronymic=False, surname=False)
for person in rn:
    list_names.append(person)
print(list_names)
