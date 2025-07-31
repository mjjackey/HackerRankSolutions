"""
Based on the pwd user input, write a function to extract the unique substring of the pwd,
the length of the substring is k. Return the number of the distinct substring.
"""
def unique_substring_num(pwd:str, k:int)->int:
    if not pwd or len(pwd)==0:
        return 0
    sub_pwd_set=set()
    for i in range(len(pwd) - k + 1):
        sub_pwd= pwd[i:i + k]
        sub_pwd_set.add(sub_pwd)
    return len(sub_pwd_set)

if __name__=='__main__':
    s="abcabc"
    num=unique_substring_num(s,3)
    print(f"the number of distinct substring: ", num)
