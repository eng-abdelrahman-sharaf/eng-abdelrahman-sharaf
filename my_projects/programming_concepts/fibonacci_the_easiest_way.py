# this algorithm has O(1)
# I suppose that fibonacci first element is 1
def fibo(num):
    if num == 1:
        return 1
    elif num<0:
        raise ValueError ("please print a positive number")
    else:
        num-=1
        return int((1/5**0.5)*(((1+5**0.5)/2)**num-((1-5**0.5)/2)**num))

for i in range(15):
    print(fibo(i))

# resources
    # https://discover.hubpages.com/education/Fibonacci-Sequence-and-Binets-Formula
    # https://github.com/giacomelli/GeneticSharp
    # https://math.stackexchange.com/questions/11502/find-formula-from-values
