# my_dict = {
#     "value": 1,
#     "next": {
#         "value": 2,
#         "next": {
#             "value": 3,
#             "next": None
#         }
#     }
# }

# tmp = None
# while my_dict:
#         next = my_dict['next']
#         my_dict['next'] = tmp
#         tmp = my_dict
#         my_dict = next
#
# my_dict = tmp
# print(my_dict)