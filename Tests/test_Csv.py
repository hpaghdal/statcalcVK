import unittest
from CsvReader import CsvReader
from Fileutilities.absolutepath import absolutepath
import math


class CsvReader_testcase(unittest.TestCase):

    path = "Tests/Data/StatCalcData.csv"
    fileName = "StatCalcData"
    myFile = path + fileName

    try:
        with open("Tests/Data/StatCalcData.csv") as f:
            sequences = pick_lines(f)
        except FileNotFoundError:
            print("File not found. Check the path variable and filename")


    if __name__ == '__main__':
        unittest.main()