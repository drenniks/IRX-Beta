input_file = open('skirt_data_angles_comma.dat', 'r')
output_file = open('skirt_data_angles.dat', 'w')

for line in input_file:
    line = line.replace(',', "")
    output_file.write(line)
output_file.close()
input_file.close()
