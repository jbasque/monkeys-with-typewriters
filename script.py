import random
import string
import math

# list of available characters
alphabet = string.ascii_letters[0:26] + ' '

# target string
target = 'monkeys with typewriters'

# mutation rate
mutation_rate = .01

# pop size
total_pop = 200

# keep track of current gen
generation = []


# fitness caculation for an entire generation
def calc_fitness(tg, gen):
    gen_fit = []
    for x in gen:
        fitness = 0
        for y, val in enumerate(x):
            if val == tg[y]:
                fitness = fitness+1
        gen_fit.append(fitness)
    return gen_fit


# fitness caculation for an individual 
def calc_fit_ind(tg, arr):
    curr_fit = 0
    for i, val in enumerate(arr):
        if val == tg[i]:
            curr_fit += 1
    
    return curr_fit


# makes next genenaration based on the fitness levels of the current gen
def next_gen(curr_gen, curr_gen_fitness):
    pool = []
    new_gen = []

    max_fitness = -1

    # finds the mosy fit in the generation
    for val in curr_gen_fitness:
        if val > max_fitness :
            max_fitness = val
            
    # normalizes fitness values to between 0 and 1, based on the most fit
    for x, val in enumerate(curr_gen_fitness):
        curr_gen_fitness[x] = val/max_fitness
        
    # adds a cetain amount of individuals to the curr generation based on their fitness
    for i in range(len(curr_gen)):
        n = int(math.floor(curr_gen_fitness[i]*100))
        for x  in range(n):
            pool.append(curr_gen[i])
            
    # crossover
    for x in range(total_pop):
        midpoint = random.randrange(1, len(target), 1)
        new_word = random.choice(pool)[0:midpoint] + random.choice(pool)[midpoint:len(target)]
        new_gen.append(new_word)

    return new_gen


# mutates current gen based on mutation rate
def mutate(arr):
    output = []

    for i, curr in enumerate(arr):
        output.append([])
        for j, val in enumerate(curr):
            if random.random() < mutation_rate:
                output[i].append(random.choice(alphabet))
            else:
                output[i].append(arr[i][j])

    return output

# initiates first gen with random choices
for i in range(total_pop):
    generation.append([])
    for j in range(len(target)):
        generation[i].append(random.choice(alphabet))

# current gen num
num_gens = 1


target_get = False
while not target_get:
    most_fit = 0
    for i, val in enumerate(generation):
        fitness = calc_fit_ind(target, val)
        if fitness > calc_fit_ind(target, generation[most_fit]):
            most_fit = i

    if calc_fit_ind(target, generation[most_fit]) == len(target):
        target_get = True
        print(''.join(generation[most_fit]))
        print('Goal achieved! It took the genetic algorithm {} generations to get to the target'.format(num_gens))

    else:
        generation = mutate(generation)
        print('current most fit is index {} {} with a fitness of {} in generation {}'.format(most_fit, ''.join(generation[most_fit]), calc_fit_ind(target, generation[most_fit]), num_gens))
        generation = next_gen(generation, calc_fitness(target, generation))
        num_gens += 1

