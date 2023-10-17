def new_hash_table(size):
    return [None]*size

def hash_func(char):
    return ord(char) - ord(' ')

def isomorphic_string(str1, str2):
    hash_size = ord('~') - ord(' ') + 1
    hash1 = new_hash_table(hash_size)
    hash2 = new_hash_table(hash_size)
    
    for i in range(len(str1)):
        hv1 = hash_func(str1[i])
        hv2 = hash_func(str2[i])

        if hash1[hv1] is not None and hash1[hv1] != str2[i]:
            return False
        hash1[hv1] = str2[i]

        if hash2[hv2] is not None and hash2[hv2] != str1[i]:
            return False
        hash2[hv2] = str1[i]

    return True

inp1, inp2 = input('Enter str1,str2: ').split(',')
print(f'{inp1} and {inp2} are {("not ", "")[isomorphic_string(inp1, inp2)]}Isomorphic')