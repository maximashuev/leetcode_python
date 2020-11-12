def first_uniq_char(self,s:"leetcode"):
    hash_table={}
    for chas in s:
        if chas in hash_table:
            hash_table[chas]=hash_table[chas]+1
        else:
            hash_table[chas]=1
    for r,chas in enumerate(s):
        if hash_table[chas]==1:
            return r
    return -1
