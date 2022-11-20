def get_summ(one, two, delimiter = '&'):
    one = str(one)
    two = str(two)
    one_two = one + delimiter + two
    return one_two
one_two = get_summ('learn', 'python').upper()
print(one_two)


