def fib(arg):
    if arg < 1 :
        print ('Wrong Argument')
    elif arg == 1 :
        return 0
    elif arg == 2 :
        return 1
    else :
        return fib(arg-1) + fib(arg-2)
