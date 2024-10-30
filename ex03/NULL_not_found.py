def NULL_not_found(object: any) -> int:
    x = 1;
    import math
    # print(object)
    if object is None:
        print("Nothing : None <class 'NoneType'>")
    elif isinstance(object, float) and math.isnan(object):
        print("Cheese: NaN <class 'float'>")
    elif isinstance(object, int) and object is 0:
        print("Zero: 0 <class 'int'>")
    elif object == '':
        print("Empty: <class 'str'>")
    elif object is False:
        print("Fake: <class 'bool'>")
    else:
        print("Type not found")
    return x
    