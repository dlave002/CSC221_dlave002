from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()

pi_string = ' '

arr_result = []

for line in lines:
    pi_string += line
    

for i in lines:
    arr_result.append(i)

print(pi_string)

print('Below from a list')


for i in range(len(arr_result)):
    print(arr_result[i]+ '/n')
