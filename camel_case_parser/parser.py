import re

def camel_to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake_to_camel(name):
    components = name.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])



def dict_snake(my_dict: dict):
    new_dict = {}
    for (key, val) in my_dict.items():
        if isinstance(key, int):
            new_dict.update({key:val})
            continue
        # print(key, val)
        new_dict.update({camel_to_snake(key):val})
    return new_dict

def list_dict_snake(data: list[dict]):
    """
    Request data : type -> List of dictionary

    """
    result_list = []
    for dict_data in data:
        
        try:
            if not isinstance(dict_data, dict):
                raise TypeError(f"List have a unprocessed type of {type(dict_data)}, except type of 'dict'")
            parsed_data = dict_snake(dict_data)
        except TypeError as e:
            raise TypeError(f"{e}")
        except Exception:
            raise RuntimeError("Something must gone wrong")
        
        result_list.append(parsed_data)
    return result_list

