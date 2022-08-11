#https://leetcode.com/problems/text-justification/
#68. Text Justification

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        line = []
        chars_len = 0
        for word in words:
            # Add untill the words and spaces reach maxWidth
            if len(word) + chars_len + len(line) <= maxWidth:
                line.append(word)
                chars_len += len(word)
                continue
            #The line contains one big word. Left Justify
            if len(line) == 1:
                line[0] += ' ' * (maxWidth - chars_len)
                output.append(line[0])
            #The line contains multiple words. Fully justify
            else:
                spaces = maxWidth - chars_len
                mid_spaces, extra_spaces = divmod(spaces, len(line)-1)
                i = 0
                while i < len(line) and extra_spaces > 0:
                    line[i] += ' '
                    extra_spaces -= 1
                    i += 1
   
                sentence = (mid_spaces * ' ').join(line)
                output.append(sentence)
            
            line = [word]
            chars_len = len(word)
        
        #Left Justify the last line
        line = ' '.join(line)
        sentence = line + ((maxWidth - len(line)) * ' ')
        output.append(sentence)
        
        return output
            