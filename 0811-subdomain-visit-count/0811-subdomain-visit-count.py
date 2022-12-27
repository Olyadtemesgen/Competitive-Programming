class Solution:
    def subdomainVisits(self, codomains: list[str]) -> list[str]:
        returned = {}
        for domain in codomains:
            split1 = domain.split('.')
            tempo = ''
            split1[:] = split1[::-1]
            split2 = split1[-1].split()
            split1[-1] = (split2[1])
            for x in split1[:len(split1)]:
                tempo = '.' + x + tempo
                returned[tempo] = returned.get(tempo, 0) + int(split2[0])
        returns = []
        for val, index in returned.items():
            returns.append(str(index)+' '+val[1:])
        return returns