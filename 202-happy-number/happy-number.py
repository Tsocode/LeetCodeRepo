class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()#visit variable is a set()

        while n not in visit:#loop; while n not visit:
            visit.add(n)#set().add to add visit to the set
            n = self.sumOfSquares(n)#get the sum of squares using a function

            if n == 1:
                return True

        return False

    def sumOfSquares(self, n: int) -> int:
            sumS = 0 #sum of squares and #get the numbers separately, 19 = 1 and 9 before we square them
            while n: #truly while loop
                d = n % 10 #[9]
                d = d ** 2 #[81]
                sumS += d #[81]
                n = n // 10 #[1]
            return sumS