"""
---*** THE PROBLEM ***---
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

---*** SOLUTION NOTES ***---
Iterating over every day of the century was the solution used in the problem. Creating a dict of the months and the
number of days in each will help with this problem.

"""


def first_days_months(day):
    # 'day' is the day of the week to find as the first of the month.
    # Returns the number of months that start with 'day' between 1901 and 2000.

    # the data for months and days, list used to aid in leap year issue.
    days_list = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
    months_dict = {1: [31], 2: [28, 29], 3: [31], 4: [30], 5: [31], 6: [30], 7: [31], 8: [31], 9: [30], 10: [31],
                 11: [30], 12: [31]}

    # Set up year conditions.
    start_year = 1900
    year = start_year

    # All days are iterated over to preserve the day position. (total_days % 7).
    total_days = 0

    # The number of 'day' at the start of the month.
    number = 0

    # Iterate over all the years required.
    while year < 2001:

        # Iterate over all the months in the specified years.
        for i in range(0, 12):

            # Generate a list from the keys of the dictionary.
            months_list = list(months_dict.keys())

            # If the month is February (testing for a leap year).
            if months_list[i] == 2:

                # If the year divides exactly by 4 (leap year) or 400, but does not divide by any other multiple of 100.
                if year%4 == 0 and (year%400 == 0 or year%100 != 0):

                    # Then we have a leap year.
                    list_key = 1

                else:

                    # Then we do not have a leap year.
                    list_key = 0

            else:
                # No other months have leap conditions.
                list_key = 0

            # Iterate over the days in the month specified.
            for j in range(1, months_dict.get(months_list[i])[list_key]+1):

                # Get the name of the next day to be iterated over.
                day_name = days_list[total_days % 7]

                # If the day is 'day' and it is the first of the month.
                if day_name == day and j == 1 and year > start_year:

                    # Add one to the number that will be the solution.
                    number += 1

                # Add to the toatl number of days iterated over.
                total_days += 1

        # Once the year has been checked, go onto the next one.
        year += 1

    return number


# Set program up for the initial conditions specified by the problem.
day = "Sun"

# Find the number of 'day' appearances at the start of the month.
solution = first_days_months(day)

# Print the solution.
print(solution)
