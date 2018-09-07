from test_plot import test_plot

bs_names = {0: 'balanced', 1: 'left-weight', 2: 'left-distance', 3: 'right_weight', 4: 'right-distance'}
bs_values = {0: ['L', 'B', 'R'],
             1: ['1', '2', '3', '4', '5'],
             2: ['1', '2', '3', '4', '5'],
             3: ['1', '2', '3', '4', '5'],
             4: ['1', '2', '3', '4', '5']}

test_plot('balance-scale.txt', bs_names, 0, bs_values)