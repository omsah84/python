import  array
arr = array.array('i',[1,2]);
print("The new create array is:",end=' ');
for i in range(0,1,2):
    print(arr[i],end=" ");


# print(arr.pop())
print("\n",arr.index(2));

arr.insert(2,3)
print(arr);
arr.reverse();
print(arr);