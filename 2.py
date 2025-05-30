def tile(n,a):
    sum_= [0] * (n + 1)
    for i in range(n):
        sum_[i + 1] = sum_[i] + a[i]
    dp = [[9999999999999999999999999999999999999] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for len_ in range(2, n + 1):
        for i in range(n - len_ + 1):
            j = i + len_ 
            b=a
            f=sum(b)
            j=j-1
            for k in range(i, j):
                hazine = dp[i][k] + dp[k + 1][j] 
                hazine=hazine+ sum_[j + 1] - sum_[i]
                if dp[i][j]<hazine:
                    dp[i][j]=dp[i][j]
                else:
                    dp[i][j]=hazine
    print( dp[0][n - 1])
 
def main():
    input_1=input().split()
    n_ = int(input_1[0])
    input_2=input().split()
    arr = []
    for i in range(n_ ):
     arr.append(int(input_2[i]))
    tile(n_,arr)
 
if __name__ == "__main__":
    main()
 
 
 