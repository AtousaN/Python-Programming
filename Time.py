class Time :
    def __init__(arg,Hour=0,Minute=0,Second=0):
        arg.Hour = Hour
        arg.Minute = Minute
        arg.Second = Second
    def show(arg):
        return str(arg.Hour)+':'+str(arg.Minute)+':'+str(arg.Second)
    def __str__(arg):
        return str(arg.Hour)+':'+str(arg.Minute)+':'+str(arg.Second)
    def __repr__(arg):
        return str(arg.Hour)+':'+str(arg.Minute)+':'+str(arg.Second)
    def __add__(arg,other):
        if arg.Second+other.Second >= 60 :
            second = arg.Second+other.Second
            arg.Minute += (second)//60
            second = (second)%60
        if arg.Minute+other.Minute >= 60 :
            minute = arg.Minute+other.Minute
            arg.Hour += (minute)//60
            minute = (minute)%60
        return str(arg.Hour+other.Hour)+':'+str(minute)+':'+str(second)
    def __sub__(arg,other):
        self = arg.Second + arg.Minute*60 + arg.Hour*120
        another = other.Second + other.Minute*60 + other.Hour*120
        argsec = arg.Second%60
        othersec = other.Second%60
        argmin = (arg.Minute+(arg.Second//60))%60
        othermin = (other.Minute+(other.Second//60))%60
        arghour = (arg.Hour+(arg.Minute//60))
        otherhour = (other.Hour+(other.Minute//60))
        if self > another :
            print ('First time is after the second Time.')
            if argsec-othersec < 0 :
                second = argsec+60 - othersec
                argmin -= 1
            else :
                second = argsec - othersec
            if argmin-othermin < 0 :
                minute = argmin+60 - othermin
                arghour -= 1
            else :
                minute = argmin - othermin
            return 'The difference is: ',str(arghour-otherhour)+':'+str(minute)+':'+str(second)
        if self < another :
            print ('Second time is after the first Time.')
            if othersec-argsec < 0 :
                second = othersec+60 - argsec
                othermin -= 1
            else :
                second = othersec - argsec
            if othermin-argmin < 0 :
                minute = othermin+60 - argmin
                otherhour -= 1
            else :
                minute = othermin - argmin
            return 'The difference is: ',str(otherhour-arghour)+':'+str(minute)+':'+str(second)
        if self == another :
            return 'Both times are the same.'
        #return str(arg.Hour-other.Hour)+':'+str(arg.Minute-other.Minute)+':'+str(arg.Second-other.Second)
    def __lt__ (arg,other) :
        self = arg.Second + arg.Minute*60 + arg.Hour*120
        another = other.Second + other.Minute*60 + other.Hour*120
        if self > another :
            return False
            #return str(arg.Hour)+':'+str(arg.Minute)+':'+str(arg.Second)+\
                       #'is after'+str(other.Hour)+':'+str(other.Minute)+':'+str(other.Second)
        elif self < another :
            return True
            #return str(other.Hour)+':'+str(other.Minute)+':'+str(other.Second)\
                    #+'is after'+str(arg.Hour)+':'+str(arg.Minute)+':'+str(arg.Second)
        elif self == another :
            return False
            #return str(arg.Hour)+':'+str(arg.Minute)+':'+str(arg.Second)+'and'\
               #+str(other.Hour)+':'+str(other.Minute)+':'+str(other.Second)+'are the same'
    def __gt__ (arg,other) :
        self = arg.Second + arg.Minute*60 + arg.Hour*120
        another = other.Second + other.Minute*60 + other.Hour*120
        if self > another :
            return True
            #return str(arg.Hour)+':'+str(arg.Minute)+':'+str(arg.Second)+\
                       #' is after '+str(other.Hour)+':'+str(other.Minute)+':'+str(other.Second)
        elif self < another :
            return False
            #return str(other.Hour)+':'+str(other.Minute)+':'+str(other.Second)\
                    #+' is after '+str(arg.Hour)+':'+str(arg.Minute)+':'+str(arg.Second)
        elif self == another :
            return False
            #return str(arg.Hour)+':'+str(arg.Minute)+':'+str(arg.Second)+'and'\
               #+str(other.Hour)+':'+str(other.Minute)+':'+str(other.Second)+'are the same'
    def __eq__ (arg,other) :
        self = arg.Second + arg.Minute*60 + arg.Hour*120
        another = other.Second + other.Minute*60 + other.Hour*120
        if self > another :
            return False
            #return str(arg.Hour)+':'+str(arg.Minute)+':'+str(arg.Second)+\
                       #'is after'+str(other.Hour)+':'+str(other.Minute)+':'+str(other.Second)
        elif self < another :
            return False
            #return str(other.Hour)+':'+str(other.Minute)+':'+str(other.Second)\
                    #+'is after'+str(arg.Hour)+':'+str(arg.Minute)+':'+str(arg.Second)
        elif self == another :
            return True
            #return str(arg.Hour)+':'+str(arg.Minute)+':'+str(arg.Second)+'and'\
               #+str(other.Hour)+':'+str(other.Minute)+':'+str(other.Second)+'are the same'
