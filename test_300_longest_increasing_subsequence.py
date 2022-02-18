from code_300_longest_increasing_subsequence import Solution

def test_example_1():
    s = Solution()
    assert s.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4

def test_example_2():
    s = Solution()
    assert s.lengthOfLIS([0,1,0,3,2,3]) == 4

def test_example_3():
    s = Solution()
    assert s.lengthOfLIS([7,7,7,7,7,7,7]) == 1

def test_failed_31():
    s = Solution()
    assert s.lengthOfLIS([1,3,6,7,9,4,10,5,6]) == 6