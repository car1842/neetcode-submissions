class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        array = arr[:]
        for i in range(len(array)-1):

            array[i] = max(arr[i+1:])
        
        array[-1] = -1
        return array
        
        
        