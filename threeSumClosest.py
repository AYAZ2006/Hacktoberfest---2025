class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res=[]
        nums.sort()
        close=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            j,k=i+1,len(nums)-1
            while j<k:
                sumo=nums[i]+nums[j]+nums[k]
                if sumo==target:
                    return target
                if abs(sumo-target)<abs(close-target):
                    close=sumo
                elif sumo<target:
                    j+=1
                else:
                    k-=1
        return close
        
        
