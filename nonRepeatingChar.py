def first_non_repeating(s):

    for i in range(len(s)):

        count = 0

        for j in range(len(s)):
            if s[i] == s[j]:
                count+=1

        if count ==1:
                return s[i]
            
    return "none"

print(first_non_repeating("aabbcedd"))