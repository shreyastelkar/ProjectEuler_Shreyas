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

def sum_primes(num):
    #sum of primes up to n
    res = 0
    for n in range(num):
        if is_prime(n):
            res += n
    return res

def str_to_matrix1(inp):
    
    count = 0
    matrix = []
    for row in range(20):
        new_l = []
        for col in range(0, 59, 3):
            if inp[count] == '0':
                st = inp[count + 1]
            else:
                st = inp[count] + inp[count + 1]
                
            new_l.append(int(st))
            
            if col != 57:
                count += 3
            else:
                count+=2
            
        matrix.append(new_l)
    return matrix

# Check right, down and diagonal right, if at right side end of matrix, only check down. Check at last 3 rows only do right 

def right(matrix, r, c):
     return matrix[r][c] * matrix[r][c + 1] * matrix[r][c + 2] * matrix[r][c + 3]
 
def down(matrix, r, c):
    return matrix[r][c] * matrix[r + 1][c] * matrix[r + 2][c] * matrix[r + 3][c]

def diag_right(matrix, r, c):
    return matrix[r][c] * matrix[r + 1][c + 1] * matrix[r + 2][c + 2] * matrix[r + 3][c + 3]

def diag_left(matrix, r, c):
    return matrix[r][c] * matrix[r + 1][c - 1] * matrix[r + 2][c - 2] * matrix[r + 3][c - 3]

def grid_product(inp):
    
    cur_prod = 0
    matrix = str_to_matrix1(inp)
    
    for row_i in range(len(matrix)):
        for col_i in range(len(matrix[row_i])):
            if col_i <= len(matrix[row_i]) - 4:
                cur_prod = max(cur_prod, right(matrix, row_i, col_i))
            if row_i <= len(matrix) - 4:
                cur_prod = max(cur_prod, down(matrix, row_i, col_i))
            if row_i <= len(matrix) - 4 and col_i <= len(matrix[row_i]) - 4:
                cur_prod = max(cur_prod, diag_right(matrix, row_i, col_i))
            if row_i <= len(matrix) - 4 and col_i >= 3:
                cur_prod = max(cur_prod, diag_left(matrix, row_i, col_i))
    return cur_prod

# loop through 1 mil, try collatz seq, keep count 
def longest_collatz(nums):
    chain = {}
    for num in range(1, nums):
        count = 0
        n = num
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = (3 * n) + 1
            count += 1
            
        chain[count] = num
    
    largest = 0
    for count in chain:
        largest = max(largest, count)
    
    return chain[largest] 

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sum_factorial(num):
    
    fac = factorial(num)
    return sum(int(digit) for digit in str(fac))

def fibonacci_rec(num):
    
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def fibonacci_iter():
    first, second = 1, 1
    count = 1
    while len(str(first)) < 1000:
        first, second = second, first + second
        count += 1
    return count

    
def fib_digits():
    num = 12
    while True:
        if len(str(fibonacci(num))) == 1000:
            return num  
        num += 1

def digit_fact():
    l = []
    num = 11
    while num < 50000:
        s = s = sum(factorial(int(digit)) for digit in str(num))
        if s == num:
            l.append(num)
        num += 1
    return sum(l)
    
if __name__=="__main__":
    
    #print(mult_3and5())
    # print(fibonacci())
    #print(prime_fac())
    #print(three_digit_palindrome())
    #print(smallest_multiple())
   # print(sum_square())
    #print(power_sum())
    #print(nthprime(10001))
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
    #print(sum_primes(2000000))
    
    inp1 = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08"\
            "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00"\
            "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65"\
            "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91"\
            "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80"\
            "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50"\
            "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70"\
            "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21"\
            "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72"\
            "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95"\
            "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92"\
            "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57"\
            "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58"\
            "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40"\
            "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66"\
            "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69"\
            "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36"\
            "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16"\
            "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54"\
            "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
            
    #print(grid_product(inp1))
    #print(longest_collatz(1000000))
    #print(sum_factorial(100))
    #print(fibonacci_iter())
    print(digit_fact())
    