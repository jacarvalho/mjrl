import argparse
from copy import copy

parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str)
args = parser.parse_args()

N_SEEDS = 10
line_num_seed = -1
line_num_model = -1

with open(args.file) as myFile:
    for num, line in enumerate(myFile, 0):
        if '\'model_file\'' in line:
            line_num_model = num

        if '\'seed\'' in line:
            line_num_seed = num

if line_num_seed == -1 or line_num_model == -1:
    raise NotImplementedError

with open(args.file, 'r') as file:
    # read a list of lines into data
    data = file.readlines()

filename_prefix = args.file.split('.txt')[0]

model_prefix = data[line_num_model].split('.pickle')[0].split('_seed_')[0]

for seed in range(N_SEEDS):
    data[line_num_seed] = f'\'seed\'          :   {seed},\n'

    data[line_num_model] = f'{model_prefix}_seed_{seed}.pickle\',\n'

    with open(filename_prefix + str(seed) + '.txt', 'w') as file:
        data = [str(d) for d in data]
        file.writelines(data)
