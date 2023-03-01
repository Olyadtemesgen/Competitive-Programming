class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        

        if rowIndex < 2:
            return [1] * (rowIndex + 1)
        else:
            rowIndex -= 1

            result = [1, 1]

            def getrows(result, rowIndex):

                if not rowIndex:
                    return result

                results = [1]

                for index in range( len(result) - 1):
                    results.append(result[index] + result[index + 1])


                results.append(1)
                rowIndex -= 1
                return [] + getrows(results, rowIndex)

            return getrows(result, rowIndex)
            