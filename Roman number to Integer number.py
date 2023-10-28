class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """


        roman_numerals = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }


        integer_number = 0
        previous_number = 0
        for R_number in s[::-1]:
            RM_value = roman_numerals[R_number]

            if RM_value<previous_number:
                integer_number-=RM_value

            else:
                integer_number+=RM_value

            previous_number = RM_value
        return integer_number
