import unittest
from ecs.entity import Entity

class TestEntity(unittest.TestCase):

    def test_id(self):
        e = Entity()
        self.assertIsInstance(e.id, str)
        self.assertGreater(len(e.id), 0)

    def test_id_override(self):
        e = Entity(id='special_id')
        self.assertEqual(e.id, 'special_id')

    def test_to_json(self):
        e = Entity()
        json = e.to_json()
        self.assertIsInstance(json, str)

    def test_from_json(self):
        json = '{"id": "e4cee65e81b111e8a9bf4ccc6a6cfbd8"}'
        e = Entity.from_json(json)
        self.assertEqual(e.id, 'e4cee65e81b111e8a9bf4ccc6a6cfbd8')