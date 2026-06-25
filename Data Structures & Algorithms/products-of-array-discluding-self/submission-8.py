class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        mults = []
        zero_count = 0
        for num in nums:
            if num != 0:
                mult *= num
            else:
                zero_count += 1

        if zero_count > 1:
            mults = [0] * len(nums)
            return mults

        for num in nums:
            if num != 0:
                if zero_count > 0:
                    mults.append(0)
                else:
                    mults.append(int(mult/num))
            else:
                mults.append(mult)


        return mults

        