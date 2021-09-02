file1 = open('1.txt', 'r')
file2 = open('2.txt', 'r')

file1_data = []
file2_data = []
for i in file1:
    i = i.strip()
    file1_data.append(i)
for i in file2:
    i = i.strip()
    file2_data.append(i)

for i in range(len(file1_data)):
    if file1_data[i] != file2_data[i]:
        print(f'i = {i} and {file1_data[i]}')
