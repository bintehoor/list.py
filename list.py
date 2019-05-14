# From random list to find minimum number with index , maximum number with index and mean value:
import  random
arr = []
for k in range (1,1001):
  arr.append(random.randint(1,1001))
  # for max and min values:
max=arr[0]
min=arr[1]
index = 0
index1 = 0
for num in range (len(arr)):
    if arr[num] > max:
        max = arr[num]
        index = num
        if arr[num] < min:
            min = arr[num]
            index1 = num
   # for mean:
sum = 0
for r in range(len(arr)):
    sum = sum+arr[r]
    mean=sum/len(arr)
# for print:
print(arr)
print("Maximum value is :",+max)
print("Maximum value index is",+index)
print("Minimum value is :",+min)
print("Minimum value index is",+(index1))
print("Mean :",+(mean))











