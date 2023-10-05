import h5py
import csv

filename = "C:/Users/lachl/Documents/thesis/rocky_data/test_4/test.rocky.files/simulation/rocky_simulation00176.rhs"

with h5py.File(filename, "r") as f:
    # Print all root level object names (aka keys) 
    # these can be group or dataset names 
    print("Keys: %s" % f.keys())
    
    particle_key = list(f.keys())[1]
    print(type(f[particle_key])) 

    particle_data = list(f[particle_key])
    print(particle_data)

    positions = list(f[particle_key]['particles_position'])
    orientation_vectors =  list(f[particle_key]['particles_orientation_vector'])
    orientation_angles =  list(f[particle_key]['particles_orientation_angle'])

    other =  list(f[particle_key]['ParticleScalars'])

print(other)

with open('C:/Users/lachl/Documents/thesis/process_rocky/part3_data.csv', 'w') as f:
    writer = csv.writer(f)
    for i in range(len(positions)):
        writer.writerow(list(positions[i])+list(orientation_angles[i])+list(orientation_vectors[i]))


