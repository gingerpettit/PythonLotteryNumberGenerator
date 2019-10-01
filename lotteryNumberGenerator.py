#This program generates a random seven-digit lottery number between a range of 0 and 9.
#Import the random function
import random

#Define the main function
def main():
    generated_lottery_numbers = [0, 0, 0, 0, 0, 0, 0] #Define list
    for index in range(7):   #Set the range for the list
        generated_lottery_numbers[index] = random.randint(0, 9) #Call the random function to input random number
    for index in generated_lottery_numbers:
        print(index,end='')  #Print the randomly generated numbers

main()
