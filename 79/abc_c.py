A = list(map(int, input()))

for bit in range(1 << 3):
    sum = A[0]
    # 式を保持
    ans = ""
    ans += str(A[0])
    for i in range(3):
        if (bit & (1 << i)):
            sum += A[i+1]
            ans += "+"
            ans += str(A[i+1])
        else:
            sum -= A[i+1]
            ans += "-"
            ans += str(A[i+1])
    if sum == 7:
        print(ans+"=7")
        exit()
