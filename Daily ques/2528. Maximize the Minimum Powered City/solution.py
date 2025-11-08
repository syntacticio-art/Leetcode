class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stations[i]

        curr = [0] * n
        for i in range(n):
            L = max(0, i - r)
            R = min(n - 1, i + r)
            curr[i] = pref[R + 1] - pref[L]

        def can(x):
            need = 0
            extra = [0] * (n + 1)
            window = 0  

            for i in range(n):
                window += extra[i]

                total_power = curr[i] + window
                if total_power < x:
                    add = x - total_power
                    need += add
                    if need > k:
                        return False

                    window += add
                    end = i + 2*r + 1
                    if end < n:
                        extra[end] -= add

            return True

        lo, hi = min(curr), max(curr) + k
        ans = lo
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
