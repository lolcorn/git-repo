import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rn = runner.Runner(name="бегун")
        for _ in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    def test_run(self):
        rn = runner.Runner(name='бегун')
        for _ in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)


    def test_challenge(self):
        rn1 = runner.Runner(name='rn1')
        rn2 = runner.Runner(name='rn2')
        for _ in range(10):
            rn1.run()
            rn2.walk()
        self.assertNotEqual(rn1.distance, rn2.distance)

if __name__ == '__main__':
    unittest.main()
