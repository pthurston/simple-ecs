import unittest
from ecs.component import Component

class SimpleComponent(Component):
    pass

class TestComponentWithNameOverride(Component):
    __component_name__ = 'custom_name'

class TestComponent(unittest.TestCase):

    def test_component_name(self):
        self.assertEqual(Component._component_name(), 'component')

    def test_inherited_component_name(self):
        self.assertEqual(SimpleComponent._component_name(), 'simplecomponent')

    def test_overriden_component_name(self):
        self.assertEqual(TestComponentWithNameOverride._component_name(), 'custom_name')