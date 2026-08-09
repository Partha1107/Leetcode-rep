class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """

        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        # solve(i, M) = maximum stones current player can get
        # starting from index i with M
        memo = {}

        def solve(i, M):

            # No piles remaining
            if i >= n:
                return 0

            # If we can take all remaining piles
            if 2 * M >= n - i:
                return suffix[i]

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):

                # Stones opponent can get after our move
                opponent = solve(
                    i + X,
                    max(M, X)
                )

                # Current player's stones
                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, M)] = best

            return best

        return solve(0, 1)