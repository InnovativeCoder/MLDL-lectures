def equilibrium(arr):
    leftSum = 0
    rightSum = 0
    n = len(arr)

    for i in range(n) :
      rightSum += arr[i]

    for i in range(n):
        rightSum -= arr[i]
        if(leftSum == rightSum):
          return i

        leftSum += arr[i]

    return -1

n = int(input())

arr = [int(x) for x in inpu
