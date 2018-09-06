
import random


class Dataset(object):
    """ This class defines dataset for a decision tree learning problem.
    It has the following fields:

        d.name          Name of the dataset. It should identify its content.
        d.examples      A list of examples. Each element has a value
                        for all attributes in d.attributes
        d.attributes    A list of integers to index the attributes
        d.attrnames     A list of names such that {attribute : attrname}
                        for every attribute in d.attributes
        d.target        The attribute that the decision-tree-algorithm
                        will try to predict
        d.values        A list of lists: each sublist contains all possible
                        values for the corrisponding attribute in
                        d.attributes: {attribute : [v1, v2, v3], ...}
        d.inputs        The list of attributes without the target
    """
    def __init__(self, name='', examples=None, attributes=None,
                 attrnames=None, target=None, values=None, inputs=None):
        """Initialize dateset's fields"""
        self.name = name
        self.examples = examples
        self.target = target
        self.values = values
        self.inputs = inputs
        if attributes is None and self.examples is not None:
            attributes = list(range(len(self.examples[0])))
        self.attributes = attributes
        if isinstance(attrnames, str):
            self.attrnames = attrnames.split()
        else:
            self.attrnames = attrnames or attributes

    def addExample(self, example):
        """
        Checks the validity of the example, then adds the example to the list
        of examples.
        """
        self.checkExample(example)
        self.examples.append(example)

    def checkExample(self, example):
        """Checks if every value of the example is valid, 
        otherwise raise a ValueError exception"""
        if self.values:
            for a in self.attributes:
                if example[a] not in self.values[a]:
                    raise ValueError('Unvalid value {} for attribute {} in {}'
                                     .format(example[a], self.attrnames[a], example))

    def removeExample(self, example):
        self.examples.remove(example)

    def removeRandomValues(self, prob):
        """For each example remove inputs values with probability == prob""" 
        for example in self.examples:
            for index in self.inputs:
                if self.probability(prob) is True:
                    self.removeValue(example, index)

    def removeValue(self, example, index):
        example[index] = None

    def probability(self, p):
        return p > random.uniform(0.0, 1.0)

    def __repr__(self):
        return '<Dataset({}): {:d} examples, {:d} attributes>'.format(
                self.name, len(self.examples), len(self.attributes))



