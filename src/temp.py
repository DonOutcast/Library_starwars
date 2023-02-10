my_dict = {
    "value": 1,
    "next": {
        "value": 2,
        "next": {
            "value": 3,
            "next": {
                "value": 4,
                "next": None
            }
        }
    }
}

tmp = None
while my_dict:
        m_next = my_dict['next']
        my_dict['next'] = tmp
        tmp = my_dict
        my_dict = m_next

my_dict = tmp
print(my_dict)
