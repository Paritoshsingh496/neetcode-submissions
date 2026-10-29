class Solution:
    def canJump(self, nums: List[int]) -> bool:

       max_reach = ''
       cur_reach = ''

       for i in range(len(nums)):
        cur_reach = i + nums[i]

        if i == 0:
            max_reach = cur_reach
        else:
            if i > max_reach:
                return False
            max_reach = max(max_reach,cur_reach)

        
       return True 

