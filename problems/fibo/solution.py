n = int(input())
m = int(input())

# O(1) memory, O(n) time
fibo = [0,1,0] #f(0) = 0, f(1) =1
for i in range(2, n+1):
    fibo[i%3] = ((fibo[(i-1)%3] + fibo[(i-2)%3])%m)

print(fibo[n%3])
