def max_number_in_kth_place(n, m, k,x):
    left = k-1
    right = n
    right = right - k
    idx = 1
    x= m-n
    if (x) > 0:
        add = 1 
        x =(m - n) - add
        y=1
        idx =idx+1
        while ((x) > 0) and (left>0 or right>0) and y==1:
            if left>0 and y==1:
                left =left - 1
                add =add+1
            if right>0 and y==1:
                right =right - 1
                add =add+1         
            idx =idx+1
            x = x - add
        increment = x / add
        increment = x/add
        idx =idx + increment

    return idx

line1=input()
line1_s=line1.split()
n = int(line1_s[0])
m = int(line1_s[1])
k = int(line1_s[2])
javab=max_number_in_kth_place(n, m, k, 1)
print(int(javab))            