T.C. = log(num) (base = 10) #no of digits in a number = log10(num)
S.C. = log(num) (base = 10) #due to recursive stack

class Solution:
    def numberToWords(self, num: int) -> str:
        lessThan10 = {1 : 'One', 2 : "Two", 3 : "Three", 4 : "Four", 5 : "Five", 6 : "Six", 7 : "Seven", 8 : "Eight", 9 : "Nine"}
        lessThan20 = {10 : "Ten", 11 : 'Eleven', 12 : "Twelve", 13 : "Thirteen", 14 : "Fourteen", 15 : "Fifteen", 16 : "Sixteen", 17 : "Seventeen", 18 : "Eighteen", 19 : "Nineteen"}
        lessThan100 = {2 : "Twenty", 3 : "Thirty", 4 : "Forty", 5 : "Fifty", 6 : "Sixty", 7 : "Seventy", 8 : "Eighty", 9 : "Ninety"}
        def solve(num):
            if num < 10:
                return lessThan10[num]
            if num < 20:
                return lessThan20[num]
            if num < 100:
                return lessThan100[num//10] + ((" " + solve(num%10)) if num % 10 != 0 else "")
            if num < 1000:
                return solve(num//100) + " Hundred" + ((" " + solve(num%100)) if num % 100 != 0 else "")
            if num < 1000000:
                return solve(num//1000) + " Thousand" + ((" " + solve(num%1000)) if num % 1000 != 0 else "")
            if num < 1000000000:
                return solve(num//1000000) + " Million" + ((" " + solve(num%1000000)) if num % 1000000 != 0 else "")
            return solve(num//1000000000) + " Billion" + ((" " + solve(num%1000000000)) if num % 1000000000 != 0 else "")
        return solve(num) if num != 0 else "Zero"
