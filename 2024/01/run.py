nums1 = []
nums2 = []

with open("input") as file:
    for line in file: 
        line = line.strip()
        n1, n2 = map(int,line.split())
        nums1.append(n1)
        nums2.append(n2)

nums1 = sorted(nums1)
nums2 = sorted(nums2)

print(sum([abs(n1-n2) for n1, n2 in zip(nums1,nums2)]))
