#!/usr/bin/python3

# def safe_print_list(my_list=[], x=0):
#     """Print the elements of a list in a safe manner"""
#     try:
#         for index in range(x):
#             print(my_list[index] , end="")
#         print("")
#     except Exception : 
#         pass
#     else : 
#         for index in range(x):
#             print(my_list[index] , end="")
#         return x
    
def safe_print_list(my_list=[], x=0):

        counter = 0
        try:
            for ele in my_list:
                if (counter >= x):
                    break
                print("{}".format(ele), end="")
                counter += 1
            print("".format())
            return counter
        except ValueError:
            print("ValueError error")
    
    
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))