###############################################################################
# DONE: 1. (3 pts)
#
#   For this _TODO_, write function called count() that takes one parameter:
#       number  <-- int
#
#   that simply counts from one until the number is reached (inclusive).
#
#   So, if the function is called like so:
#
#       count(5)
#
#   it would print:
#
#       1
#       2
#       3
#       4
#       5
#
#   Make sure to use a *while* loop in your solution. Also, notice how you will use the accumulator pattern for this problem.
#
#   Also, write a line of code that calls your function with whatever number you would like.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def count(number):
    x = 1
    while x <= number:
        print(x)
        x = x+1

count(9)


###############################################################################
# TODO: 2. (5 pts)
#
#   For this _TODO_, write a function called adder() that will continually ask the use to enter a number (using user input) like so:
#
#       "Please Enter a Number: "
#
#   and will keep a running total of all the numbers that the user enters.
#
#   If the user enters a zero (0) the function should end and print the sum to the user like so:
#
#       "The sum is <TOTAL HERE>."
#
#   Your solution may use either just ints or in can also accept floats (it's up to you).
#
#   Do NOT worry about what happens when a user enters a value that is not a number. It can simply error out in this case.
#
#   Make sure to use a *while* loop in your solution. Also, notice how you will use the accumulator pattern for this problem.
#
#   Also, make sure to call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def adder():
   num = input('Please enter a number: ')
   
       



    

###############################################################################
# TODO: 3. EXTRA CREDIT (3 pts)
#
#   DO NOT attempt this extra credit until you have completed m3!!!
#   
#   For this extra credit _TODO_, modify your code in _TODO_ #2 to handle the case when the user inputs a non-numeric input.
#
#   The function should maintain its total that it has calculated thus far and should prompt the user to enter a valid number like so:
#
#       "Invalid Input! Please enter a valid number: "
#
#   There are likely many ways you could accomplish this. Feel free to do some digging for potential solutions. Your solution should work no matter what the user types in.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################