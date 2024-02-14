
def mult_3and5():
    cur_sum = 0
    for num in range(1000):
        if (num % 3 == 0) or (num % 5 == 0):
            cur_sum += num
    
def fibonacci():
    sum = 0
    term1 = 1
    term2 = 2
    
    while term1 < 4_000_000:
        if (term1) % 2 == 0:
            sum += term1
            
        temp1 = term1
        term1 = term2
        term2 = temp1 + term2 
    return sum


def prime(num):
    #prime- anything divisible by itself and 1,
    tracking_primes = {}
    for num in range(13195, 2, -1):
        if not tracking_primes:
            tracking_primes.update(num)
            
def three_digit_palindrome():
    cur = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            i = str(i)
            j = str(j)
            if i[2] != 0 or j[2] != 0 or (i[2] != 5 and j[2] != 2) or (i[2] != 2 and j[2] != 5):
                if (str(int(i) * int(j)))[::-1] == str(int(i) * int(j)):
                    cur = max(cur, int(i) * int(j))
                    
    return cur

def smallest_multiple():
    start_num = 20
    while True:
        for i in range(1, 21):
            if start_num % i != 0:
                break
            if i == 20:
                return start_num
            
        start_num += 20

def sum_square():
    c = 0
    s = range(1, 101) #list
    su = sum(s)**2
    for n in s:
        c+=n**2
    return su - c

def pythagorean():
    pass

def power_sum():
    s = 0
    for i in str(2**1000):
        s += int(i)
    return s


if __name__=="__main__":
    
    #print(mult_3and5())
    # print(fibonacci())
    #print(three_digit_palindrome())
    #print(smallest_multiple())
   # print(sum_square())
    #print(power_sum())