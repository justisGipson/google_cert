import timeit


def compare_equality(n_times):
    str1 = 'natural_language_processing' * 2000
    str2 = 'natural_language_processing' * 2000
    for i in range(n_times):
        if str1 == str2:
            pass


timeit.Timer(compare_equality(1000000))
