def main():
    print(twoSumUsingForLoops([1,2,3],3))


    
#def twoSumUsingRecursion(list,target):




    
def twoSumUsingForLoops(list,target):
    #def twoSum(self, nums: List[int], target: int) -> List[int]
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if i +j == target:
                print("found it with", i, "and", j)
                return [i,j]    
          
    return []   



main()

     

