def fun1(to_replace, replacer):
    def fun2(string):
        nonlocal to_replace, replacer 
        result = string.replace(replacer, to_replace) 
        return result 
    return fun2 
