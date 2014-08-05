def find_permutations(number_list, permutation_index):
    if permutation_index == len(number_list) - 1:
        print number_list
    else:
        for i in range(permutation_index, len(number_list)):
            number_list[permutation_index], number_list[i] = number_list[i], number_list[permutation_index]
            find_permutations(number_list, permutation_index + 1)
            number_list[permutation_index], number_list[i] = number_list[i], number_list[permutation_index]

test_list = [1,2,3]
find_permutations(test_list,0)
