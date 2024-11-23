import unittest
import logging
import traceback
import Runner_2 as Runner




class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner_1 = Runner.Runner('Вася', -10)

            for _ in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")
            logging.warning(traceback.format_exc())


    def test_run(self):
        try:
            runner_2 = Runner.Runner([2,3], 5)

            for _ in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
            logging.warning(traceback.format_exc())






if __name__ == '__main__':
    unittest.main()

logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="runner_tests.log",
    encoding='utf-8',
    format='%(asctime)s | %(levelname)s | %(message)s')
