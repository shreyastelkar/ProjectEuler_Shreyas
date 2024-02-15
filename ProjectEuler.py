from math import sqrt

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


def prime_fac():
    # Example 20, 20 /2 = 10, 10 / 2 = 5, 
    # 5 / 3, 
    # 5 / 5 = 1, 
    
    num = 600851475143
    startOdd = 3
    
    while (num % 2 == 0):
        num /= 2
    
    while num != 1:
        while (num % startOdd == 0):
            last_num = num
            num /= startOdd
        startOdd += 2

        
    return int(last_num)
    
            
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

def power_sum():
    s = 0
    for i in str(2**1000):
        s += int(i)
    return s

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nthprime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num
        

# 3^2 + 4^2 = 5^2, 9 + 16 = 25, 3 + 4 + 5 = 12
# Find pythagorean triple where a + b + c = z

def pythagorean():
    
    for a in range(1, 1000):
        for b in range(a, 1000):
            c_squared = a**2 + b**2
            c = sqrt(c_squared)
            if a + b + c == 1000:
                return int(a * b * c)


def str_to_matrix(inp):
    matrix = []
    start = 0
    for row_i in range(20):
        new_l = []
        for col_i in range(start, start + 50):
            new_l.append(int(inp[col_i]))
        matrix.append(new_l)
        start += 50
    return matrix


# need to check for last row where it should not go to the next line. 

def adj_prod(inp, n):
    matrix = str_to_matrix(inp)
    cur_prod = 0
    new_prod = 1
    row_i = 0
    i_step = 0
    
    while row_i < (len(matrix) - 1):
        for col_i in range(0, len(matrix[row_i])): #0-49
            
            #with overlap
            i_step = col_i
            num = i_step + n
            
            while i_step < num:
                
                if (i_step//(len(matrix[row_i]))) > 0:
                    r_i = row_i + 1
                else:
                    r_i = row_i
                
                print(i_step % (len(matrix[row_i])),r_i)
                
                new_prod *= matrix[r_i][i_step % (len(matrix[row_i]))]
                i_step += 1

            cur_prod = max(cur_prod, new_prod)
            new_prod = 1
            
        row_i += 1
        
    return cur_prod

def sum_primes():
    


if __name__=="__main__":
    
    #print(mult_3and5())
    # print(fibonacci())
    #print(prime_fac())
    #print(three_digit_palindrome())
    #print(smallest_multiple())
   # print(sum_square())
    #print(power_sum())
    print(nthprime(10001))
    #print(pythagorean())
    
    inp = "73167176531330624919225119674426574742355349194934"\
    "96983520312774506326239578318016984801869478851843"\
    "85861560789112949495459501737958331952853208805511"\
    "12540698747158523863050715693290963295227443043557"\
    "66896648950445244523161731856403098711121722383113"\
    "62229893423380308135336276614282806444486645238749"\
    "30358907296290491560440772390713810515859307960866"\
    "70172427121883998797908792274921901699720888093776"\
    "65727333001053367881220235421809751254540594752243"\
    "52584907711670556013604839586446706324415722155397"\
    "53697817977846174064955149290862569321978468622482"\
    "83972241375657056057490261407972968652414535100474"\
    "82166370484403199890008895243450658541227588666881"\
    "16427171479924442928230863465674813919123162824586"\
    "17866458359124566529476545682848912883142607690042"\
    "24219022671055626321111109370544217506941658960408"\
    "07198403850962455444362981230987879927244284909188"\
    "84580156166097919133875499200524063689912560717606"\
    "05886116467109405077541002256983155200055935729725"\
    "71636269561882670428252483600823257530420752963450"
    
    #print(adj_prod(inp, 13))