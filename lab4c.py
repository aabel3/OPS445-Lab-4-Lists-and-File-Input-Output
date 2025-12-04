#!/usr/bin/env python3

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 
			'City': 'Toronto', 
			'Country': 'Canada', 'Postal Code': 'M3J3M6', 
			'Province': 'ON'}
			
dict_newnham = {'Address': '1750 Finch Ave E', 
				'City': 'Toronto', 
				'Country': 'Canada', 'Postal Code': 'M2J2X5', 
				'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
	new_dict = {}
	values_count = 0
	while values_count < len(keys):
		new_dict[keys[values_count]] = values[values_count]
		values_count = values_count + 1
	return new_dict
# ~ def shared_values(dict1, dict2):
	# ~ # Place code here- refer to function specifics in section below
	
if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
