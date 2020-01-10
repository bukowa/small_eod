import factory
import factory.fuzzy

from .models import Feature, Dictionary


class DictionaryFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "dictionary-%04d" % n)
    active = True
    minItems = factory.fuzzy.FuzzyInteger(0, 3)
    maxItems = factory.fuzzy.FuzzyInteger(4, 5)

    class Meta:
        model = Dictionary

class FeatureFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "feature-%04d" % n)

    class Meta:
        model = Feature

