
def max_prize(teams, start, end,n):

    if start > end:
        return 0
    if start == end:
        return teams[start]

    mid=start
    mid=mid+end 
    mid=mid//2

    max_left = max(teams[start:mid + 1])
    max_right = max(teams[mid + 1:end + 1 ])         
    prize_when_left_eliminated = max_prize(teams, start, mid,1 )
    
    prize_when_right_eliminated = max_prize(teams, mid + 1, end,1 ) 
    
    if max_left + prize_when_right_eliminated>max_right + prize_when_left_eliminated:
        return max_left + prize_when_right_eliminated
    else:
        return max_right + prize_when_left_eliminated

def main():
    input_1=input()
    n_ = int(input_1) 
    input_2=input().split()
    teams = []
    for i in range(2**n_):
        o =0
        teams.append(int(input_2[i]))
        o=o+1
    result = max_prize(teams, 0, 2 ** n_ - 1,1)
    print(result)

main()
