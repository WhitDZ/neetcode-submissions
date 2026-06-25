class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 0
        mults = []
        zero_count = 0
        for num in nums:
            if num != 0:
                if mult == 0:
                    mult = 1
                mult *= num
            else:
                zero_count += 1
        for num in nums:
            if num != 0:
                if zero_count > 0:
                    mults.append(0)
                else:
                    mults.append(int(mult/num))
            else:
                if zero_count > 1:
                    mults.append(0)
                else:
                    mults.append(mult)


        return mults

        