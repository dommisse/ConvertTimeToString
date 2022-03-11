# Print Time in words.
nums = ["zero", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen",
        "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen",
        "twenty", "twenty one", "twenty two",
        "twenty three", "twenty four",
        "twenty five", "twenty six", "twenty seven",
        "twenty eight", "twenty nine"];
specialCases = [0, 1, 59, 15, 30, 45]


def printWords(h, m):
    # if m == 0 or m == 1 or m == 59 or m == 15 or m == 30 or m == 45:
    #     handleSpecialCases(h, m);
    if specialCases.index(m) >= 0:
        handleSpecialCases(h, m);
    elif (m <= 30):
        print(nums[m], "minutes past", nums[h]);

    elif (m > 30):
        print(nums[60 - m], "minutes to",
              nums[(h % 12) + 1]);


def handleSpecialCases(h, m):
    if m == 0:
        print(nums[h], "o' clock");
    elif m == 1:
        print("one minute past", nums[h]);
    elif m == 59:
        print("one minute to", nums[(h % 12) + 1]);
    elif m == 15:
        print("quarter past", nums[h]);
    elif m == 30:
        print("half past", nums[h]);
    elif m == 45:
        print("quarter to", (nums[(h % 12) + 1]));


# Driver Code
h = 6;
m = 0;

printWords(h, m);
