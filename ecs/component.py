class Component(object):
    __component_name__ = None

    @classmethod
    def _component_name(cls):
        return cls.__component_name__ or cls.__name__.lower()