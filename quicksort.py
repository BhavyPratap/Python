def partition(A,F,L):    #A=Array , F=index of first element and L= index of last element.  
    pivot = A[L]         #Taking last element as pivot
    i = F-1              #Start from -1 position
    for j in range(F,L): #Runs from 0 to n-1
        if arr[j] <= pivot:  
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i]
            #If the pivot is greater than jth element, swap the (i+1)th and jth term.
    
    arr[i+1],arr[L] = arr[L],arr[i+1] #At last swap the pivot element with (i+1)th term.
    return ( i+1 ) 
 
def quickSort(A,F,L): 
    if F < L: 
        p = partition(A,F,L) #After partitioning on the basis of pivot element, we will sort all the elements at left of the pivot and at the right of the pivot.
        quickSort(arr, F, p-1) #Where p is the partitoning index.
        quickSort(arr, p+1, L) #We will recurssively sort elememts left to p and right to p.
  
arr = [] 
n = int(input("Enter the number of elememts u want to insert:"))
print("\nEnter the elememts:")
for i in range(n):
    num=int(input())
    arr.append(num)

quickSort(arr,0,n-1) 

print ("\nSorted array is shown below:") 
for i in range(n): 
    print ("%d" %arr[i]) 
  