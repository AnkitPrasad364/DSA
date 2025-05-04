# count numbers
                                
# Function to count the number
# of digits in an integer 'n'.
def countDigits(n):
    # Initialize a counter variable
    # 'cnt' to store the count of digits.
    cnt = 0
    # While loop iterates until 'n'
    # becomes 0 (no more digits left).
    
    # in case the provided number is only 0 then it should give count as 1
    if n==0:
        return 1
    while n > 0:
        # Increment the counter
        # for each digit encountered.
        cnt = cnt + 1
        # Divide 'n' by 10 to
        # remove the last digit.
        n = n // 10
    # Return the
    # count of digits.
    return cnt


if __name__ == "__main__":
    N = int(input("Enter any number to count the number of digits present in it :  "))
    print("N:", N)
    digits = countDigits(N)
    print("Number of Digits in N:", digits)
                                
                            