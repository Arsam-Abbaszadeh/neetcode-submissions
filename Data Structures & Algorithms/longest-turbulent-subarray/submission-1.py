class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # odd k = next is less
        # even k = next is greater
        # 2, 4, 3, 0
        # [2,4,3,2,2,5,1,4]
        # [1,1,2]
        # [9,4,2,10,7,8,8,1,9]

        subArrayLen = 1
        subArrayLenMax = 1
        subArray2Len = 1
        subArray2LenMax = 1
        for i in range(1, len(arr)):
            if i % 2 == 0:
                if arr[i - 1] > arr[i]:
                    subArrayLen += 1
                    subArrayLenMax = max(subArrayLenMax, subArrayLen)
                else:
                    subArrayLen = 1
            else:
                if arr[i - 1] < arr[i]:
                    subArrayLen += 1
                    subArrayLenMax = max(subArrayLenMax, subArrayLen)
                else:
                    subArrayLen = 1
            print(subArray2Len)
            print(subArrayLen)

            if i % 2 == 1:
                if arr[i - 1] > arr[i]:
                    subArray2Len += 1
                    subArray2LenMax = max(subArray2LenMax, subArray2Len)

                else:
                    subArray2Len = 1
            else:
                if arr[i - 1] < arr[i]:
                    subArray2Len += 1
                    subArray2LenMax = max(subArray2LenMax, subArray2Len)
                else:
                    subArray2Len = 1
            
        
        return max(subArrayLenMax, subArray2LenMax)
