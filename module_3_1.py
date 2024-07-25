calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    new_tuple = (len(string), string.upper(), string.lower())
    return new_tuple

def is_contains(string, list_to_search):
    count_calls()
    for item in list_to_search:
        new_list = []
        new_list.append(item.lower())
    if string.lower() in new_list:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)