import unittest
from active import eat, nap
class activityTests(unittest.TetCase):
	def test_eat_healthy(self):
		self.assertEqual(eat("food",is_healty=True),
			"very good to take good food,your good")

	def test_eat_unhealthy(self):
		self.assertEqual(eat("egg",is_healty=False),
			"very good to take good food,your good")
