#!/usr/bin/python3
#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    counter2 = 0
    for ele in my_list:
        try:
            if (counter >= x):
                break
            print("{:d}".format(ele), end="")
            counter += 1
        except (ValueError, TypeError):
            counter2 += 1
    if (counter+counter2 < x):
        raise IndexError("list index out of range")
    print("".format())
    return counter
        
        
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))