file_handler = open("test.txt")

#1st method 
print("count:" , len(list(file_handler)))

# file handler is a running like an iterator so you should re assign it to read lines again or put it into list
file_handler = open("test.txt")

# 2nd method
count = 0 
for i in file_handler:
    count+=1
print("count:" , count)

# related sources 
    # resetting-generator-object-in-python
    # https://rb.gy/0vzfo
    # file is not a generator but io textwrapper
    # https://rb.gy/gt0pw
    # file-modes
    # https://rb.gy/v1wi7
    # changing-pointer-position
    # http://rb.gy/vq9my