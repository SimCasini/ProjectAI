from test_plot import test_plot

car_names = {0: 'buying', 1: 'maint', 2: 'doors', 3: 'persons', 4: 'lug_boot', 5: 'safety', 6: 'evaluation'}
car_values = {0: ['vhigh', 'high', 'med', 'low'],
              1: ['vhigh', 'high', 'med', 'low'],
              2: ['2', '3', '4', '5more'],
              3: ['2', '4', 'more'],
              4: ['small', 'med', 'big'],
              5: ['low', 'med', 'high'],
              6: ['unacc', 'acc', 'good', 'vgood']}

test_plot('car.txt', car_names, 6, car_values)
