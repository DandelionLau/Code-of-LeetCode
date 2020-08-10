# use dictionary

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        numbers = {}
        for i in range(len(strs)):
            s = list(strs[i])
            s.sort()
            s = str(s)
            if s not in numbers.keys():
                numbers[s] = [strs[i]]
            else:
                numbers[s].append(strs[i])

        return list(numbers.values())
