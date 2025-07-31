"""
Based on the password user input, write a function to extract the unique substring of the password,
the length of the substring is k. Return the number of the distinct substring.
"""
def unique_substring_num(password:str, k:int)->int:
    if not password or len(password)==0:
        return 0
    sub_password_set=set()
    for i in range(len(password)-k+1):
        sub_password=password[i:i+k]
        sub_password_set.add(sub_password)
    return len(sub_password_set)

if __name__=='__main__':
    s="abcabc"
    num=unique_substring_num(s,3)
    print(f"the number of distinct substring: ", num)
