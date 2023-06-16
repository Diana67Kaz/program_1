'''
def recurs(count):
    print(count)
    if count==5:
        return
    recurs(count + 1)
    print(count)

recurs(0)
'''
import os

current_path = os.path.abspath(__file__)
parend_path = os.path.join(current_path, '..') #от текущего пути к предыдущему

print(current_path)
print(parend_path)

def get_all_files(path):
    for i_name in os.listdir(path):
        new_path = os.path.join(path, i_name)
        if os.path.isdir(new_path):
            print('папка', i_name)
            get_all_files(new_path)
        else:
            print('-', i_name)
get_all_files(parend_path)



