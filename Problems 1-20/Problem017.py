"""
---*** THE PROBLEM ***---
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

---*** SOLUTION NOTES ***---
Creating a dictionary of all the numbers needed and the length of the word for those numbers will help in the solution.
The number 112 is read as OneHunderedAndTwelve, it has 4 parts in the solution. (Not as OneHundredAndTenTwo)
These means that numbers between 10 and 19 will need their own special cases.
"""

# Hand created list of numbers needed, the words associated and the length of those words.
number_dict = {1: ["One", 3],
               2: ["Two", 3],
               3: ["Three", 5],
               4: ["Four", 4],
               5: ["Five", 4],
               6: ["Six", 3],
               7: ["Seven", 5],
               8: ["Eight", 5],
               9: ["Nine", 4],
               10: ["Ten", 3],
               11: ["Eleven", 6],
               12: ["Twelve", 6],
               13: ["Thirteen", 8],
               14: ["Fourteen", 8],
               15: ["Fifteen", 7],
               16: ["Sixteen", 7],
               17: ["Seventeen", 9],
               18: ["Eighteen", 8],
               19: ["Nineteen", 8],
               20: ["Twenty", 6],
               30: ["Thirty", 6],
               40: ["Forty", 5],
               50: ["Fifty", 5],
               60: ["Sixty", 5],
               70: ["Seventy", 7],
               80: ["Eighty", 6],
               90: ["Ninety", 6],
               100: ["Hundred", 7],
               1000: ["Thousand", 8]}


def create_list_num(number):
    # 'number' the number to be converted to a list.
    # Returns a list of digits in the number.
    # i.e 102 -> ["1", "0", "2"], 112 -> ["4", "0", "12"], 124 -> ["1", "2", "4"].

    # Cast the number as a string to then cast it as a list.
    str_num = str(number)
    list_num = list(str_num)

    # If the number is in the hundreds category.
    if len(list_num) >= 2:

        # And if the second character is a 1 (i.e the number is is between x10 and x19).
        if int(list_num[-2]) == 1:
            # Set the last element of the list to the combination of the middle and last character.
            list_num[-1] = list_num[-2] + list_num[-1]

            # The middle character becomes 0.
            list_num[-2] = "0"

    # Reverse the list, the reason for this will become clear later
    list_num.reverse()

    return list_num


def find_string_sum(num_list, number_dict):
    # 'num_list' is the unique list associated with a number as previously created by the "create_num_list" function.
    # Returns a list of the string associated with a number and the length of that string. (i.e ['Twelve', 6]).

    string_sum = ["", 0]

    # Iterate over all terms of the 'num_list'.
    for i in range(0, len(num_list)):

        # Zero is not a word that appears in the word version of numbers, so skip elements that are 0.
        if int(num_list[i]) != 0:

            # For the first part of the number, this is why the list was reversed (numbers 1 to 19).
            if i == 0:
                # Get the values list from the dictionary based on the key.
                values = number_dict.get(int(num_list[i]))

            # For the second part of the number in multiples of 10 (numbers 20 to 90).
            if i == 1:
                # The numerical value is needed for the tens column.
                numerical_value = 10 * int(num_list[i])

                # Get the values list from the dictionary based on the key.
                values = number_dict.get(numerical_value)

            # For the third part of the number in multiples of 100(numbers 100 to 900).
            if i == 2:

                # Get the values list from the dictionary based on the key. The part before the hundred word.
                # For example: for 200, unit = ["Two", 3], for 234, unit = ["Two", 3].
                unit = number_dict.get(int(num_list[i]))

                # Get the values list from the dictionary based on the key. This is the hundred word.
                # For example: for 200, hundred = ["Hundred", 7], for 234, hundred = ["Hundred", 7].
                hundred = number_dict.get(100)

                # Combine these two parts to produce the final values list.
                # For example: for 200, values = ["TwoHundred", 10].
                values = [unit[0] + hundred[0], unit[1] + hundred[1]]

                # However for values that aren't whole multiples of 100 an extra "And" is needed to match British
                # convention, so check to see if the number is a whole multiple of 100.
                if int(num_list[i - 1]) == 0 and int(num_list[i - 2]) == 0:

                    # If it is, then the "And" is not needed.
                    pass

                else:

                    # Otherwise add the "And", then add 3 to the total length.
                    values = [values[0] + "And", values[1] + 3]

            # For the fourth part of the number in multiples of 1000 (In the case of this problem only 1000 is needed).
            if i == 3:
                # Get the values list from the dictionary based on the key. The part before the Thousand word.
                # For example: for 2000, unit = ["Two", 3], for 2340, unit = ["Two", 3].
                unit = number_dict.get(int(num_list[i]))

                # Get the values list from the dictionary based on the key. This is the Thousand word.
                # For example: for 2000, thousand = ["Thousand", 8], for 2340, thousand = ["Thousand", 8].
                thousand = number_dict.get(1000)

                # Combine these two parts to produce the final values list.
                # For example: for 2000, values = ["TwoThousand", 11].
                values = [unit[0] + thousand[0], unit[1] + thousand[1]]

            # Append the values found on this iteration to the ones found previously.
            string_sum[0] = values[0] + string_sum[0]
            string_sum[1] = values[1] + string_sum[1]

    return string_sum


def sum_of_all_range(upper, number_dict):
    # 'upper' is the upper bound of the range to find the number of characters over.
    # Returns the number of characters in the range of numbers between 1 and maximum.

    addition = 0

    # Iterate over the whole range specified.
    for i in range(1, (upper + 1)):
        # Get the list of associated digits.
        list_num = create_list_num(i)

        # Get the string associated with the number and the number of characters in this string.
        string_sum = find_string_sum(list_num, number_dict)

        # Add the number of characters in this string to the previously found ones.
        addition += string_sum[1]

    return addition


# Set program up for the initial conditions specified by the problem.
upper = 1000

# Find the numer of characters associated with this range.
solution = sum_of_all_range(1000, number_dict)

# Print the solution found.
print(solution)
