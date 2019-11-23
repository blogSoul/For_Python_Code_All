def myrange(start,end,step):
    list = []
    randomnumber_R = 1.0
    start = round(start,9)
    end = round(end,9)
    step = round(step,9)
    next_value = start
    len_list = int((end-start)/step)
    
    if(type(start) != type(randomnumber_R)):
        return print("please enter another number")
    if(type(end) != type(randomnumber_R)):
        return print("please enter another number")
    if(type(step) != type(randomnumber_R)):
        return print("please enter another number")
    
    interval = round(end - start,9)
    size_interval = abs(interval)
    size_step = abs(step)
    
    if(size_step>size_interval):
        return print("please enter another number")
    
    if(size_step == 0.000000000):
            return print("please enter another number")     
    else:
        if(start >= end):
            return print("please enter another number")
        elif(start < end and step < 0.000000000):
            return print("please enter another number")
        
        else:
            for i in range(0,len_list+1):
                list.append(next_value)
                next_value = next_value + step
                next_value = round(next_value,9)
                if(next_value >= end):
                    break
            return list
            
