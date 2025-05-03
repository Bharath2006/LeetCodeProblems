class Solution:
    def uniqueMorseRepresentations(self, x: List[str]) -> int:
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len(set(["".join([a[ord(i)-97] for i in j]) for j in x]))