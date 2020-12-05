def take_input():
    maxi = 0
    lower = []
    highr = []
    iters = int(input())
    if iters < 1:
        print("Negative numbers not allowed!")
        exit(0)

    for i in range(iters):
        nums = input()
        numbers = nums.split()
        if (int(numbers[0]) > int(numbers[1])) or (int(numbers[0]) < 0):
            exit(0)

        lower.append(int(numbers[0]))
        highr.append(int(numbers[1]))
        if highr[i] > maxi:
            maxi = highr[len(highr)-1]
    return(lower,highr, maxi)


def find_max_p(maxi):
    import math
    primes = [2,3]
    epochs = math.ceil((maxi-1)/6)
    for i in range(1,epochs):
        num1 = 6*i - 1
        num1_is_prime = True
        num2 = 6*i + 1
        num2_is_prime = True
        for j in primes:
            if j > int(math.sqrt(num2)):
                break
            if(num1 % j == 0):
                num1_is_prime = False

            
            if(num2 % j == 0):
                num2_is_prime = False
            if(not(num1_is_prime) and not(num2_is_prime)):
                break
        if(num1_is_prime):
            primes.append(num1)

        if (num2_is_prime):
            primes.append(num2)
    return primes



def main():
    import time
    
    entire = []
    
    lower, highr, maxi = take_input()
    
    start_time = time.time()
    
    #Finding primes till maxi
    primes = find_max_p(maxi)

    for first,last in zip(lower,highr):
        numbers_this_time = []
        for num in primes:
            if(num >= first and num <=last):
                numbers_this_time.append(num)
            if(num >= last):
                break
        entire.append(numbers_this_time)
    #for p in entire:
        #for num in p:
            #print (num)
        #print ("\n")
    print("Time taken to compute:" + str(time.time() - start_time))
    #print (len(primes))
main()
