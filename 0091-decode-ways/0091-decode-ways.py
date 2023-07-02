class Solution:
	def numDecodings(self, s: str) -> int:
	    
		if(s[0] == '0'):
			return 0

		if(len(s) == 1):
			return 1

		before, now = 1, 1

		for index in range(1, len(s)):

			before1 = int(s[index])
			before_beforer = int(s[index-1] + s[index]) 
			
			numbers = 0 
            
			if(before1 > 0):
				numbers += now
				
			if(10 <= before_beforer <= 26):
				numbers += before

			before = now
			now = numbers
	
		return now
		