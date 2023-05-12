
# partition function 
def partition(arr,tiny,huge):

   i = ( tiny-1 )
   pivot = arr[huge] # pivot element

   for j in range(tiny, huge):
      # If current element is smaller
      if arr[j] <= pivot:
         
         i = i+1

         arr[i],arr[j] = arr[j],arr[i]

   arr[i+1],arr[huge] = arr[huge],arr[i+1]

   return ( i+1 )

 
def quickSort(arrdata,tiny,huge):
 
   if tiny < huge:
  
      pi = partition(arrdata,tiny,huge)
      
      quickSort(arrdata, tiny, pi-1)
       
      quickSort(arrdata, pi+1, huge)
      

array_data = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]

print('the original array data: ', array_data )

array_len = len(array_data)

quickSort(array_data,0,array_len-1)

print('the sorted array is ...', array_data)
