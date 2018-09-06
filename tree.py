
class DecisionTree:
    """It holds an attribute to test and a set of branches, one for each of the attribute's values"""    
    def __init__(self, attribute, attrname=None, branches=None):
        self.attribute = attribute
        self.attrname = attrname or attribute
        self.branches = branches or {}

    def __call__(self, example):
        """Given an example, classify it using the attribute and the branches."""
        attrvalue = example[self.attribute]
        if attrvalue in self.branches:
            return self.branches[attrvalue](example)

    def add(self, value, subtree):
        """Add a branch to the tree. If self.attribute = value go to the given subtree"""
        self.branches[value] = subtree

    def display(self, indent=0):
        name = self.attrname
        print('Test', name)
        for(value, subtree) in self.branches.items():
            print(' ' * 4 * indent, name, '=', value, '==>', end=' ')
            subtree.display(indent + 1)

    def __repr__(self):
        return('DecisionTree({0!r}, {1!r}, {2!r})'
               .format(self.attribute, self.attrname, self.branches))
