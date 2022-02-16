def solution(A):
    A.sort()
    A = list(set(A))
    A = list(filter(lambda x: x > 0, A))

    if len(A) == 0:
        return 1

    x = min(A)
    if(max(A) <= 0 or x > 1):
        return 1

    # print(A)
    for i in range(len(A)):
        increment = 1 if i+1 < len(A) else 0
        payload = A[i+increment]
        #print(payload, x)
        if payload - x == 1:
            x = payload
        else:
            return x + 1
    print(solution(A))

