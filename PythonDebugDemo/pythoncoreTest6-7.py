num_str = raw_input("input:")
num_num = int(num_str)
alist = range(1, num_num+1)
l = len(alist)
i = 0
while i < l:
    if num_num % alist[i] == 0:
        del alist[i]
        l -= 1
    else:
        i += 1
print alist
