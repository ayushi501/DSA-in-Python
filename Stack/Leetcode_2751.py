# Robot Collisions

from collections import defaultdict


class Solution:
    def survivedRobotsHealths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        l = []
        m = defaultdict(int)
        n = len(positions)
        for i in range(n):
            l.append((positions[i], healths[i], directions[i]))
            m[positions[i]] = healths[i]
        l.sort()
        print(l)
        print(m)
        st = []
        for i in l:
            f = 1
            while st and i[2] == 'L' and st[-1][2] == 'R':
                t = st[-1]
                if i[1] == t[1]:
                    st.pop()
                    m[i[0]] = 0
                    m[t[0]] = 0
                    f = 0
                    break
                elif i[1] > t[1]:
                    k = (i[0], i[1]-1, i[2])
                    st.pop()
                    i = k
                    m[t[0]] = 0
                else:
                    k = (t[0], t[1]-1, t[2])
                    st.pop()
                    st.append(k)
                    m[i[0]] = 0
                    m[k[0]] = k[1]
                    f = 0
                    break
            if f == 1:
                m[i[0]] = i[1]
                st.append(i)

        print(st)
        if not st:
            return []
        ans = []
        for i in m:
            if m[i] == 0:
                continue
            ans.append(m[i])
        return ans
