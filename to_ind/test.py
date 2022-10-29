import to_ind.ind_func1
if __name__ == "__main__": 
    x = input("введите исходную строку: ")
    c = input("введите внещнюю функцию: ")
    h = input("введите внутреннюю функцию: ") 
    replace = to_ind.ind_func1.fun1(h,c) 
    print(replace(x))
