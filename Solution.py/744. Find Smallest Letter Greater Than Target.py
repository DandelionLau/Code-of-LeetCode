class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i > target:
                return i
            elif i <= target and i == letters[-1]:
                return letters[0]
