import math
from tree import DecisionTree
from leaf import Leaf


def decision_tree_alg(dataset):
    target = dataset.target
    values = dataset.values

    def dt_learn(examples, attributes, parent_examples=()):
        if len(examples) == 0:
            return majority_value(parent_examples)
        elif same_class(examples):
            return Leaf(examples[0][target])
        elif len(attributes) == 0:
            return majority_value(examples)
        else:
            A = select_best_attribute(attributes, examples)
            tree = DecisionTree(A, dataset.attrnames[A])
            for (val_i, exs_i) in split(A, examples):
                subtree = dt_learn(exs_i, removeall(A, attributes), examples)
                tree.add(val_i, subtree)
            return tree

    def majority_value(examples):
        i = 0
        for v in values[target]:
            if(count(target, v, examples) > i):
                i = count(target, v, examples)
                major = v
        return Leaf(major)

    def same_class(examples):
        class_0 = examples[0][target]
        for e in examples:
            if e[target] != class_0:
                return False
        return True

    def count(attr, value, examples):
        counter = 0
        for e in examples:
            if e[attr] == value:
                counter += 1
        return counter

    def select_best_attribute(attributes, examples):
        max = 0
        for a in attributes:
            manage_missing_values(examples, a)
            info = information_gain(a, examples)
            if info >= max:
                max = info
                best = a
        return best

    def entropy_bits(examples):
        e = 0
        for v in values[target]:
            if len(examples) != 0:
                p = count(target, v, examples) / len(examples)
                if (p != 0):
                    e += ((-p) * math.log2(p))
        return e

    def information_gain(attribute, examples):
        N_examples = len(examples)
        remainder = 0
        for (v, examples_i) in split(attribute, examples):
            remainder += ((len(examples_i) / N_examples) * entropy_bits(examples_i))
        return entropy_bits(examples) - remainder

    def most_common_value(examples, attribute):
        i = 0
        for v in values[attribute]:
            if count(attribute, v, examples) > i:
                i = count(attribute, v, examples)
                major = v
        return major
      
    def manage_missing_values(examples, attribute): 
        value_default = most_common_value(examples, attribute)
        for e in examples:
            if e[attribute] is None:
                e[attribute] = value_default

    def split(attribute, examples):
        """Return a list of (value, example) pairs for each value of attribute"""
        return [(v, [e for e in examples if e[attribute] == v])
                for v in values[attribute]]

    def removeall(attr, seq):
        """Return a copy of seq (or string) with all occurences of attr removed."""
        if isinstance(seq, str):
            return seq.replace(attr, '')
        else:
            return [x for x in seq if x != attr]

    return dt_learn(dataset.examples, dataset.inputs)
