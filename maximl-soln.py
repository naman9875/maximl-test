from collections import defaultdict, Counter
 
 
def SS(string):
    p = ''.join(set(string))
    # Dictionary which keeps a count of all the unique characters in input string.
    dict_unique = Counter(p)
 
    # Number of unique characters which need to be present in the desired window.
    required = len(dict_unique)
 
    l = 0
    r = 0
    
    #e.g. if input is "aabc" then the window must have two a's, one b and one c. Thus curr_window_uniq_chars_count would be = 3 when all these conditions are met.
    curr_window_uniq_chars_count = 0
 
    curr_window_uniq_dict = {}
 
    # ans tuple of the form (window length, left, right)
 
    min_window_len = float("inf")
    desired_window_l = None
    desired_window_r = None
 
    while r < len(string):
 
        # Add one character from the right to the window
        curr_window_uniq_dict[string[r]] = curr_window_uniq_dict.get(string[r], 0) + 1
 
        # If the frequency of the current character added equals to the desired count in string then increment the curr_window_uniq_chars_count count by 1.
        if string[r] in dict_unique and curr_window_uniq_dict[string[r]] == dict_unique[string[r]]:
            curr_window_uniq_chars_count += 1
 
        while l <= r and curr_window_uniq_chars_count == required:
 
            # Save the smallest window until now.
            if r - l + 1 < min_window_len:
                min_window_len = r - l + 1
                desired_window_l = l
                desired_window_r = r
 
            curr_window_uniq_dict[string[l]] -= 1
            if string[l] in dict_unique and curr_window_uniq_dict[string[l]] < dict_unique[string[l]]:
                curr_window_uniq_chars_count -= 1
 
            l += 1
 
        r += 1
    return "" if min_window_len == float("inf") else len(string[desired_window_l: desired_window_r + 1])
 
 
i = input()
 
ans = SS(i)
print (ans)