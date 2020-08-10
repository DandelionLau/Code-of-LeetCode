class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        template = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],\
                ['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        
        letters = [template[int(i)-2]  for i in list(digits)]
        length = len(letters) - 1
        i = 1
        result = []
        if length == 0:
            result = letters[0]
        else:
            i = 1
            while i <= length:
                if i == 1:
                    result = self.combinationTwo(letters[0], letters[i])
                else:
                    result = self.combinationTwo(result, letters[i])
                i = i + 1
        return result
    
    def combinationTwo(self, data1,data2):
        result = []
        for i in range(len(data1)):
            for j in range(len(data2)):
                result.append(data1[i]+data2[j])
        return result
                
        
        
        
