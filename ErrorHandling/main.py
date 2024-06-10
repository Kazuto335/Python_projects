# # # # # # # # # # # # # # # #
# ----- E R R O R S --------- #
# ------- H A N D L I N G --- #
# # # # # # # # # # # # # # # #


# FileNotFound
# file = open('random_file.txt')

# # KeyError
# a_dictionary = {'key': 'value'}
# value = a_dictionary['non_existent_key']

# # IndexError
# fruit_list = ['apple', 'orange', 'grapes']
# fruit = fruit_list[3]

# # TypeError
# text = 'abcd'
# print(text + 5)


try:
    file = open('random_file.txt')
    a_dictionary = {'key': 'value'}
    print(a_dictionary['key'])
except FileNotFoundError as error_message:
    print(f'{error_message} was not found so we create the new file.')
    file = open('random_file.txt', 'w')
    file.write('Created file Successful')
except KeyError as error_message:
    print(f'The key {error_message} does not exist.')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('File Closed')
