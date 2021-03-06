287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/
  
#1. Hashtable/Counter

class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
      counter = Counter(nums)
      for e in counter.keys():
          if counter[e]>1:
              return e
            
#Time complexity: O(n)
#Space complexity:O(n)

#2 Binary Search
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r =1, len(nums)-1
        
        while l < r:
            counter = 0
            m = l+(r-l)//2
            for n in nums:
                if n <= m:
                    counter +=1
            if counter > m: 
                r = m
            else: 
                l = m + 1
        return r            
#Time complexity: O(n)
#Space complexity:O(1)



#3. Two pointers- fast and slow pointers
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0
        while True:
            slow = nums[slow]           # similar to linked node: slow=slow.next
            fast = nums[nums[fast]]     # similar to linked node: fast=fast.next.next
            if fast == slow:    
                break
        
        fast = 0                
        while slow != fast:     # meet again
            slow = nums[slow]
            fast = nums[fast]
        
        return fast
#Time complexity: O(n)
#Space complexity:O(1)
