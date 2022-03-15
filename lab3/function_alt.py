from math import atan
from statistics import mean


def find_coefficient(adjacent_side, opposite_side=154):
    """Returns the coefficient of static friction in radians when given the opposite and adjacent sides"""
    return opposite_side / adjacent_side


def loop_lengths(lengths):
    """Returns a list of angles when given a list of lengths"""
    x = []
    for i in range(len(lengths)):
        x.append(find_coefficient(lengths[i]))
    return x


#reads file and saves the contents to the variable "data"
file = open("lab3_data.csv", "r")
data = file.read()
file.close()

#removing unnecessary characters and splitting the data into separate rows
data = data.replace("\ufeff", "")
rows = data.split("\n")

#distance of first experiment, large area
large_distance = []
#diance of second experiment, small area
small_distance = []

for row in range(len(rows)):
    rows[row] = rows[row].split(",")
    large_distance.append(int(rows[row][0]))
    small_distance.append(int(rows[row][1]))

large_coefficients = loop_lengths(large_distance)
small_coefficients = loop_lengths(small_distance)

print(mean(large_coefficients), mean(small_coefficients))
