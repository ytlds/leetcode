class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = eval(a) + eval(b)
        if sum == 0:
            return str(sum)
        c = '0' + str(sum)
        c_rev = c[::-1]
        ans = ''
        carry = 0
        for d in c_rev:
            tmp = eval(d) + carry
            if tmp > 1:
                tmp -= 2
                carry = 1
            else:
                carry = 0
            ans += str(tmp)
        ans = ans[::-1]
        if ans[0] == '0':
            ans = ans[1:]
        return ans


if __name__ == '__main__':
    s = Solution()
    a = '1010'
    b = '1011'
    print(s.addBinary(a, b))
