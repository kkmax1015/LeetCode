from typing import List
class Solution＿BruteForce:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        
class Solution_HashTable:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # hashテーブル(dict)への要素の登録
        dict_nums ={}
        for i in range(0, len(nums)):
            # キーに要素,ValueにIndexを登録する
            dict_nums[nums[i]] = i
        
        # target - nums[i]を探す
        for i in range(0, len(nums)):
            search_num = target - nums[i]
            if search_num in dict_nums:
                if dict_nums[search_num] != i:
                    return [i, dict_nums[search_num]]

class Solution_HashTable_Oneloop:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # hashテーブル(dict)への要素の登録
        dict_nums ={}
        for i in range(0, len(nums)):
            # target - nums[i]を探す
            search_num = target - nums[i]
            if search_num in dict_nums:
                if dict_nums[search_num] != i:
                    return [i, dict_nums[search_num]]
                
            # キーに要素,ValueにIndexを登録する
            dict_nums[nums[i]] = i
        