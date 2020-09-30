from random import randrange, random, choices
from statistics import mean
from matplotlib import pyplot as plt
from collections import deque

def shift_forward(configuration, confuser_list):
    new_configuration = apply_confusers(configuration, confuser_list)
    #temp = new_configuration[-1]
    #for i in range(len(configuration) - 1, 0, -1):
        #new_configuration[i] = new_configuration[i-1]
    #new_configuration[0] = temp
    new_configuration.rotate(1)
    return new_configuration

def apply_confusers(configuration, confuser_list):
    new_configuration = configuration
    for i in confuser_list:
        new_configuration[i] = (configuration[i] + 1) % 2
    return new_configuration

for j in range(5):
    prob_for_init_config = j/4
    print("Approximate percentage of 0s in initial configuration:", prob_for_init_config)

    length_of_configuration = 1000
    number_of_confusers = 20
    number_of_shifts = 500

    #current_configuration = [randrange(2) for i in range(length_of_configuration)]
    #new_configuration = [1] * length_of_configuration
    new_configuration = choices([0, 1], weights=[prob_for_init_config, 1-prob_for_init_config],
                                k=length_of_configuration)
    current_configuration = deque(new_configuration)
    current_confuser_list = [-1] * number_of_confusers

    print("Initial configuration:", current_configuration)


    for i in range(number_of_confusers):
        if i == 0:
            random_index = randrange(length_of_configuration)
        else:
            while(random_index in current_confuser_list):
                random_index = randrange(length_of_configuration)
        current_confuser_list[i] = random_index
    current_confuser_list.sort()

    print("Confuser list:", current_confuser_list)
    print()

    grey_values = [-1]*number_of_shifts

    for i in range(number_of_shifts):
        current_configuration = shift_forward(current_configuration, current_confuser_list)
        grey_values[i] = mean(current_configuration)

    plt.plot(grey_values)
    axis = plt.gca()
    axis.set_ylim([0, 1])
plt.show()