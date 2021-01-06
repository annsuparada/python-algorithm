# Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine(if any). The fee structure is as follows:

# 1. If the book is returned on or before the expected return date, no fine will be charged(i.e.: .fine=0)
# 2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 * the number of dats late.
# 3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 * the number of months late.
# 4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
# Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be 10000.


def libraryFine(d1, m1, y1, d2, m2, y2):
    # check year
    if y2 < y1:
        yFine = y1 - y2
        return yFine * 10000
    elif y1 < y2:
        return 0
    #  check month
    elif m2 < m1:
        mFine = m1 - m2
        return mFine * 500
    elif y1 <= y2 and m1 < m2:
        return 0
    elif y1 <= y2 and m1 <= m2:
        # check date
        if d2 < d1:
            dFine = d1 - d2
            return dFine * 15
        elif d1 <= d2:
            return 0


print(libraryFine(28, 2, 2015, 15, 4, 2015))  # 0
print(libraryFine(2, 7, 1014, 1, 1, 1015))  # 0
print(libraryFine(9, 6, 2015, 6, 6, 2015))  # 45
