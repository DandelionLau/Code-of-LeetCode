class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        data = {'(':1, ')':-1}
        result = []
        result1, result2 = self.generateBracket(2*n)
        for i in range(len(result2)):
            if result2[i] == 0:
                result.append(result1[i])
        return result
    
    def generateBracket(self, n):
        result1 = []            # bracket
        result2 = []            # bracket sum
        if n == 1:
            return ['('], [1]
        else:
            pre, num = self.generateBracket(n-1)
            for i in range(len(pre)):
                temp1 = pre[i] + '('
                temp2 = pre[i] + ')'
                num_temp1 = num[i] + 1
                num_temp2 = num[i] - 1
                if num_temp1 >= 0:
                    result1.append(temp1)
                    result2.append(num_temp1)
                if num_temp2 >= 0:
                    result1.append(temp2)
                    result2.append(num_temp2)
        return result1, result2

        
                
            
