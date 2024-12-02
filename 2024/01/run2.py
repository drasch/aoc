from collections import Counter

nums1 = []
nums2 = []

with open("input") as file:
    for line in file: 
        line = line.strip()
        n1, n2 = map(int,line.split())
        nums1.append(n1)
        nums2.append(n2)

nums_count2 = Counter(nums2)


print(sum([n1*nums_count2[n1] for n1 in nums1]))
#print(sum([n1*nums2.count(n1) for n1 in nums1]))