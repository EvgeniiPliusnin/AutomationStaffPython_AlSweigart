def print_picnic(items_dict:list, left_width, right_width):
    print("TAKE A PICNIC WITH YOU")
    for k, v in items_dict.items():
        print((k.ljust(left_width, '.')))
    
