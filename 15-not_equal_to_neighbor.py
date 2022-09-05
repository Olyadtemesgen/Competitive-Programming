class Solution:
    def rearrangeArray(self, nums):
        lis = list(sorted(nums))
        new_l = [0] * len(nums)
        counter = 1
        count = 1
        if len(nums) % 2 != 0:
            lista = lis[:len(nums) // 2 + 1]
            listb = lis[len(nums) // 2 + 1:]
            new_l[0] = lista[0]
            for x in range(1 , len(nums)):
                if x < len(lista):
                    new_l[x + counter] = lista[x]
                else:
                    new_l[x + count - len(lista)] = listb[x - len(lista)]
                    count += 1
                counter += 1
        else:
            lista = lis[:len(nums) // 2]
            listb = lis[len(nums) // 2:]
            new_l[0] = lista[0]
            for x in range(1 , len(nums)):
                if x < len(lista):
                    new_l[x + counter] = lista[x]
                else:
                    new_l[x + count - len(lista)] = listb[x - len(lista)]
                    count += 1
                counter += 1
        return new_l
