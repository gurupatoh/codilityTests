def solutiion(A):
    sum_left=A[0]
    sum_right=sum(A)-A[0]
    difference=abs(sum_left-sum_right)
    for i in range(1,len(A)-1):
        sum_left+=A[i]
        sum_right-=A[i]
        current_difference=abs(sum_left-sum_right)
        if(difference>current_difference):
            difference=current_difference
    return difference
print(solutiion([3,1,2,4,3]))