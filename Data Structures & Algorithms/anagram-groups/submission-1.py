class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: #function which will return list of list
        res = defaultdict(list)#creates a dictionary which will store the result 
        for s in strs: #goes through every word one by one 
            count = [0]*26  #creates a list of 26 zeroes for each letter
            for c in s:
                count[ord(c)-ord("a")] +=1   #ord(c)-converts a letter into ascii value 
                # ord(c)-ord("a") this will give us the position of a letter we wil add 1 to it and return its count 
            res[tuple(count)].append(s)    # reason to use tuple is because list can not be dictionary but tuples can.
        return list(res.values())   # time comple = (m*n)


        
        