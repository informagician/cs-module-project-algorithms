'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n,b=None):
    # Your code here

    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n == 4:
        return 7
    # n == 5 => 8
    if n > 4:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

# 0,1,2,3,4,5,6
# 1,1,2,3,5,8,13

# 1,1,1,1
# 1,1,2
# 1,2,1
# 2,1,1
# 1,3
# 3,1
# 2,2



# 1,1,1,1,1
# 1,1,1,2
# 1,1,2,1
# 1,2,1,1
# 2,1,1,1
# 1,1,3
# 1,3,1
# 3,1,1
# 3,2
# 2,3
# 1,2,2
# 2,1,2
# 2,2,1