my_dict = {
    "value": 1,
    "next": {
        "value": 2,
        "next": {
            "value": 3,
            "next": None
        }
    }
}

for key, value in my_dict.items():
    next = value.get("next")
    
    print(key, value)

# def rever(m_dict):
#     m_dict = {}
#
#     m_dict["value"], m_dict.get("next")["value"] = m_dict.get("next").get("value"), m_dict.get("value")
#     print(m_dict)
# rever(my_dict)