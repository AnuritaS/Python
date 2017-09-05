'''Sherlock considers a string, , to be valid if either of the following conditions are satisfied:

All characters in  have the same exact frequency (i.e., occur the same number of times). For example,  is valid, but  is not valid.
Deleting exactly  character from  will result in all its characters having the same frequency. For example,  and  are valid because all their letters will have the same frequency if we remove occurrence of c, but  is not valid because we'd need to remove  characters.
Given , can you determine if it's valid or not? If it's valid, print YES on a new line; otherwise, print NO instead.'''

def isValid(s):
    # Complete this function\ // Complete this function
    ans = ""
    arr = {}
    ch1 = s[0]
    ch = ''
    count=0
    for i in s:
        ch = i
        if ch in arr:
            arr[i] += 1
        else:
            arr[i] = 1

    c = arr.get(ch)
    print(arr)

    for j in arr:
        if (c != arr.get(j)):
            if (arr.get(j) - 1 == c or arr.get(j) - 1 == 0):
                count += 1
            elif (c != arr.get(j)):
                ans = "NO"
        if (count == 1):
            ans = "YES"


    return ans


s = input().strip()
result = isValid(s)
print(result)

