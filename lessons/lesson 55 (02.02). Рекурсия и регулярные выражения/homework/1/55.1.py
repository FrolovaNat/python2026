def is_balanced(s):
    if not s:
        return True
    if len(s) == 1 or not s in "([{":
        return False
    
    for р in range(len(s)):
        if s[p] in ['(', '[', '{'] and s[p+1] in [')', ']', '}']:
            return is_balanced(s)
        else:
            return False




    
