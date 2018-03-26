#Version:  1.0
#Author:  Kyle Siler
#Program Description:  This application is a fibonacci sequence algorithm
#that finds the next number in the sequence by adding the two numbers before it.
#The program output is based on the max number the user inputs into the program.
#So for example, if the user inputs the max number as 21, then the sequence output
#will not go above 21.

def main():
    #flag used to control when program runs
    runAgain = True

    #assign start of fibonacci sequence to 0
    #assign next number in fibonacci sequence to 1
    startNum, nextNum = 0, 1

    #run until the user has entered valid input or the fibonacci sequence is displayed
    while runAgain == True:
        #check to see if the user entered valid input
        try:
            #prompt the user for how many numbers there are to calculate in the fibonaci sequence
             sequence = int(input("What is the max term in the fibonacci sequence:  "))
    
        #if the user did not enter valid input, display and error message
        except:
            print("You have entered an invalid input please try again!")

        #calculate the fibonacci sequence  
        else:
            #display first number in fibonacci sequence
            print (startNum)
            #run until the max term in the sequence has been reached
            while nextNum <= sequence:
                #next number in sequence
                print (nextNum)
                #calculate following numbers in sequence
                #where startNum is the previous nextNum and Next num is the sum of previous startNum and nextNum
                startNum, nextNum = nextNum, startNum + nextNum
        #set flag to end program
        runAgain = False
            

main()
