from functools import reduce

def second_max(lst):
    def step(init, x):
        max1, max2 = init

        if max1 is None or x > max1:
            return (x, max1)
        elif max2 is None or x > max2:
            return (max1, x)
        else:
            return (max1, max2)

    max1, max2 = reduce(step, lst, (None, None))
    return max2
	
print(second_max([5, 4, 3, 2, 5]))