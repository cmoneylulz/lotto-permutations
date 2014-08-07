def find_permutations(number_list, permutation_index):
    if permutation_index == len(number_list) - 1:
        print number_list
    else:
        for i in range(permutation_index, len(number_list)):
            number_list[permutation_index], number_list[i] = number_list[i], number_list[permutation_index]
            find_permutations(number_list, permutation_index + 1)
            number_list[permutation_index], number_list[i] = number_list[i], number_list[permutation_index]


def find_cash_3(number_list):
	if len(number_list) != 3:
		print "not a cash 3 list"
	else:
		list_one = [number_list[0], number_list[1]]
		list_two = [number_list[1], number_list[2]]
		find_permutations(list_one, 0)
		find_permutations(list_two, 0)

def find_cash_4(number_list):
	if len(number_list) != 4:
		print "not a cash 4 list"
	else:
		list_one = [number_list[0], number_list[1], number_list[2]]
		list_two = [number_list[1], number_list[2], number_list[3]]
		find_permutations(list_one, 0)
		find_permutations(list_two, 0)

test_list = [1,2,3]
find_cash_3(test_list)

test_list2 = [1,2,3,4]
find_cash_4(test_list2)