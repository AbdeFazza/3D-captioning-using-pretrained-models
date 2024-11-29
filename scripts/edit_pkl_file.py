import pickle

parent_dir = './assets'
path_multiple_examples = f'{parent_dir}/example_object_path_multiple_examples.pkl'
path_single_example = f'{parent_dir}/example_object_path_single_example.pkl'

#--------------- Read from .pkl file ---------------

# Load the .pkl file
with open(path_single_example, 'rb') as file:
    data = pickle.load(file)
    
print(data)

#--------------- Write to .pkl file ---------------

# data = [f'{parent_dir}/glbs/1964.88_armor_for_man_and_horse.glb',
#         f'{parent_dir}/glbs/bayonetta.glb',
#         f'{parent_dir}/glbs/cyberpunk_laptop_concept_design.glb',
#         f'{parent_dir}/glbs/dumptruck.glb',
#         f'{parent_dir}/glbs/frog.glb',
#         f'{parent_dir}/glbs/hospital_bed.glb',
#         f'{parent_dir}/glbs/p38.glb',
#         f'{parent_dir}/glbs/retro_computer.glb',
#         f'{parent_dir}/glbs/revolver.glb',
#         f'{parent_dir}/glbs/tiko.glb']
# print(data)

# Save the modified data back to the .pkl file
# with open(path_multiple_examples, 'wb') as file:
#     pickle.dump(data, file)