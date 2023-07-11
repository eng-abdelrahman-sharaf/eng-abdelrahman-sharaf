# memoization and recursion project 
# regular time complexity is O(log n) but now it will be pretty faster after using memoization 
# and taking some data to store in memo
""" 
test cases
  5
  4
  7
  11
  45 (it will get it very quick than regular) 
  """


def regular_febo(n):

        if n == 1 or n == 2: 
            return 1

        else:
             return regular_febo(n-1) + regular_febo(n-2) 


memo = dict()

def febo(n):

    try:

        return memo[n]
        

    except KeyError: 

        if n == 1 or n == 2: 
            return 1
        
        else: 
            result = febo(n-1) + febo(n-2)
            memo [n] = result
            return result

# let's inject some data into memo
for i in ([5, 4, 7, 11]):
    febo(i)

# let's test
for i in ([45 , 70 , 457]):
    print(febo(i))


# # I advise you not to uncomment this
# for i in ([5, 4, 7, 11, 45]):
#     print(regular_febo(i))