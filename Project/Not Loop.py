def countDown(n):
    for i in range(n):
        print(n)
        n = n - 1
        
    print("Done")

countDown(100)

def countDownRecursive(n):
    if n <= 0:
        print("Done")
        return

    print(n)
    countDownRecursive(n = n - 1)

countDownRecursive(100)