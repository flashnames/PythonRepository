class Solution:
    def game(self, guess,answer):
        Count=0
        for i in range(len(guess)):
            Guess=guess[i]
            if Guess==answer[i]:
                Count+=1
        return Count

if __name__=="__main__":
    print(Solution().game([2,2,3],[3,2,3]))