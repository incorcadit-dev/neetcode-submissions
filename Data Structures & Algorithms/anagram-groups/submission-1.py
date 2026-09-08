from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordsMap = {}

        for word in strs:
            sortedWord = "".join(sorted(word))

           
            if sortedWord not in wordsMap:
                wordsMap[sortedWord] = []

            wordsMap[sortedWord].append(word)

        return list(wordsMap.values())

        
                

            
            
            

        
        