def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    seen = {}
    for i, num in enumerate(numbers):
        try:
            return (seen[num], i)
        except KeyError:
            seen[target_sum - num] = i
    return None

    # numbers = list(sorted(numbers))  # added after the update
    #     # to make sure numbers are always sorted        
    # lo_index = 0
    # hi_index = len(numbers) - 1
    # while lo_index < hi_index:
    #     pair_sum = numbers[lo_index] + numbers[hi_index]
    #     if pair_sum < target_sum:
    #         lo_index += 1
    #     elif pair_sum > target_sum:
    #         hi_index -= 1
    #     else:
    #         return (lo_index, hi_index)
    # return None

print(find_two_sum([1, 3, 5, 7, 9], 12)) 

# for path in sys.path:
#     print(path)

# importlib.import_module('solution_two_sum')
# exec(open('solution_two_sum.py').read())

# runpy.run_module(mod_name='solution_two_sum')