import sys
sys.path.append('/home/hvids/pract/parser')
from ord_dict import ord_dict
def compareWords(lhs, rhs):
# 1 - первое слово больше, 2 - второе, 0 равыны
    if lhs[0] == '-':
        lhs = lhs[1:]
    if rhs[0] == '-':
        rhs = rhs[1:]
    lhs = lhs.replace('|','')
    lhs = lhs.lower()
    rhs = rhs.replace('|','')
    rhs = rhs.lower()
    ans = 0
    _min = min(len(lhs), len(rhs))
    for i in range(0,_min):
        if ord_dict(lhs[i]) > ord_dict(rhs[i]):
            ans = 1
            break
        elif ord_dict(lhs[i]) < ord_dict(rhs[i]):
            ans = 2
            break
    if ans == 0:
        if len(lhs) < len(rhs):
            ans = 2
        else:
            ans =  1
    return ans
def quickSort(nums):
    if len(nums) <= 1:
        return nums
    else:
        item = nums[0]
        s_nums = []
        m_nums = []
        e_nums = [item,]
        for n in nums[1:]:
            if compareWords(n,item) == 2:
                s_nums.append(n)
            elif compareWords(n,item) == 1:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quickSort(s_nums) + e_nums + quickSort(m_nums)
