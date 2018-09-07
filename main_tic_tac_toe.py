from test_plot import test_plot

tic_names = {0: 'top-left-square', 1: 'top-middle-square', 2: 'top-right-square', 3: 'middle-left-square', 4: 'middle-middle-square', 5: 'middle-right-square', 
             6: 'bottom-left-square', 7: 'bottom-middle-square', 8: 'bottom-right-square', 9: 'class'}
tic_values = {0: ['x', 'o', 'b'],
              1: ['x', 'o', 'b'],
              2: ['x', 'o', 'b'],
              3: ['x', 'o', 'b'],
              4: ['x', 'o', 'b'],
              5: ['x', 'o', 'b'],
              6: ['x', 'o', 'b'],
              7: ['x', 'o', 'b'],
              8: ['x', 'o', 'b'],
              9: ['positive', 'negative']}

test_plot('tic_tac_toe.txt', tic_names, 9, tic_values)
