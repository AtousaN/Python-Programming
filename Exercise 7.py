def fib_list(arg):
        if arg < 1 :
            print ('Wrong Argument')
        elif arg == 1 :
            return [0]
        elif arg == 2 :
            return [0,1]
        else :
            fib_list = [0,1]
            for i in range(arg-2):
                fib_list += [0]
                fib_list[i+2] = fib_list[i+1]+fib_list[i]
            return fib_list
