class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        
        content = []
        result = []
        resu = []

        for sentence in paths:
            sentence = sentence.split()
           
            for word in sentence[1:]:
                index = word.index('(')

                if word[index:] in content:
                    index1 = content.index(word[index:])

                    if not result[index1]:
                        result[index1].append(resu[index1])
                    result[index1].append(sentence[0]+'/'+word[:index])

                else:
                    content.append(word[index:])
                    result.append([])
                    resu.append(sentence[0]+'/'+word[:index])
           
        real_result = []
        for x in result:
            if x:
                real_result.append(x)
        return real_result

