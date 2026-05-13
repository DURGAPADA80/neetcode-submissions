class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else: 
                count[n] =1
        #frequency base bucket creat
        freq=[[] for i in range(len(nums) + 1)]

        for num in count:
            frequency = count[num]
            freq[frequency].append(num)
        #result for k frequent element
        result = []
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result


