#Problem Link - https://www.hackerrank.com/challenges/py-the-captains-room/problem

n=int(raw_input())
nums=map(int,raw_input().split(" "))
nums=sorted(nums)
for i in xrange(1,len(nums)):
    if i!=len(nums)-1:
        if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
            print nums[i]
            break
    else:
        print nums[i]
