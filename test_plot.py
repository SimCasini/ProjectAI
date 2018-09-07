from dataset import Dataset
from copy import deepcopy
from decision_tree_alg import decision_tree_alg
import matplotlib.pyplot as mplot
import random
from csv import reader


def test_plot(file, attrnames, target, values, pre_prun):
    dataset = create_dataset(file, attrnames, target, values)
    p = [0, 0.1, 0.2, 0.5]
    accuracy_train = []
    accuracy_val = []

    for pp in p:
        accT_media = 0
        accV_media = 0
        for j in range(10):
            accT, accV = ten_fold_cross_validation(dataset, pre_prun, pp)
            accT_media += accT
            accV_media += accV
        accT_media = accT_media/10
        accV_media = accV_media/10
        accuracy_train.append(accT_media)
        accuracy_val.append(accV_media)

    mplot.plot(p, accuracy_train, '--', color='r', label="Train")
    mplot.plot(p, accuracy_val, '--', color='b', label="Val")
    mplot.legend(loc='best')
    mplot.ylabel("Accuracy")
    mplot.xlabel("p")
    mplot.grid(True)
    mplot.show()

def set_inputs(attributes, target):
    inputs = deepcopy(attributes)
    inputs.pop(inputs.index(target))
    return inputs

def create_dataset(file, attrnames, target, values):
    d = load_csv(file)
    examples = []
    for i in range(len(d)):
        example = {}
        for j in range(len(d[0])):
            example[j] = d[i][j]
        examples.append(example)
    attributes = [a for a in range(len(examples[0]))]
    inputs = set_inputs(attributes, target)
    d_set = Dataset(file, examples, attributes, attrnames, target, values, inputs)
    return d_set

def load_csv(filename):
    file = open(filename, "r")
    lines = reader(file)
    dataset = list(lines)
    return dataset

def ten_fold_cross_validation(dataset, pre_prun, prob):
    n = len(dataset.examples)
    fold_accT = 0
    fold_accV = 0
    random.shuffle(dataset.examples)
    for fold in range(10):
        dataset_1 = deepcopy(dataset)
        train_data, val_data = train_test_split(dataset_1, fold * (n / 10), (fold + 1) * (n / 10))
        dataset_1.examples = train_data
        dataset_1.removeRandomValues(prob)
        tree = decision_tree_alg(dataset_1, pre_prun)
        fold_accT += accuracy_ratio(tree, dataset.target, train_data)
        fold_accV += accuracy_ratio(tree, dataset.target, val_data) 
    accuracy_t = fold_accT/10
    accuracy_v = fold_accV/10
    return accuracy_t, accuracy_v

def train_test_split(dataset, start, end):
    start = int(start)
    end = int(end)
    examples = dataset.examples
    train = examples[:start] + examples[end:]
    val = examples[start:end]
    return train, val

def accuracy_ratio(tree, target, examples):
    count = 0
    for e in examples:
        if e[target] == tree(e):
            count += 1
    return (count/len(examples)) * 100 


