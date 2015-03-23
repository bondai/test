def checkio(data):
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.
    p2 = data
    if len(data) == 1:
        return data
    else:
        i=0
        for N in data:
            print(N)
            if data.count(N) == 1:
                #p2.pop(i)
                p2.remove(N)
            i+=1
        print (p2)
    #replace this for solution
        return p2

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


isinstance(checkio([1]), list)
checkio([10])
checkio([1, 2, 3, 1, 3])
checkio([1, 2, 3, 4, 5])
checkio([5, 5, 5, 5, 5])
checkio([10, 9, 10, 10, 9, 8])
