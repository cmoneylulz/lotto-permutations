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

def cash_3(number_list):
	if len(number_list) != 3:
		print "not a valid cash 3 pick"
	else:
		list_one = [number_list[0], number_list[1]]
		list_two = [number_list[1], number_list[2]]

		number_list.sort()
		list_one.sort()
		list_two.sort()

		print number_list
		print list_one
		print list_two

def cash_4(number_list):
	if len(number_list) != 4:
		print "not a valid cash 4 pick"
	else:
		list_one = [number_list[0], number_list[1], number_list[2]]
		list_two = [number_list[1], number_list[2], number_list[3]]

		number_list.sort()
		list_one.sort()
		list_two.sort()

		print number_list
		print list_one
		print list_two

def fantasy_5(number_list):
	if len(number_list) != 5:
		print "not a valid fantasy 5 pick"
	else:
		number_list.sort()
		print number_list


test_list = [3,1,2]
cash_3(test_list)

test_list = [3,2,4,1]
cash_4(test_list)

test_list = [4,2,1,5,3]
fantasy_5(test_list)