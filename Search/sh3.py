def simple_sqrt(num):
    least = 0
    most = num
    ans = 1

    while least <= most:
        mid = (least + most)//2
        if mid*mid == num:
            ans = mid
            return ans
        elif mid*mid < num:
            ans = mid
            least = mid+1
        else:
            most = mid-1
            
    return ans

inp = int(input('simple sqrt: '))
print(simple_sqrt(inp))