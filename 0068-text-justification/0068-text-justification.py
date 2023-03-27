# condition
# ' ' necessasery
# spaces between words should be distributed as evenly as possible.
# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# left >= right
# maxWidth = 16
# constraints
# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth

# approach
# find max k satisfied, Sum(words[i:k] + k - i +1) <= maxwidth
# current_words_len = k - i + 1
# total_width = maxwidth - len(words[i:k]) 
# find one_width = current_words_len - 1 / maxwidth
#   if  one_width is not integer  
#   for example total_width = 9, current_words_len - 1 = 4
#   3,2,2,2 or 3,3,3,2
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                if len(cur) == 1:
                    res.append(cur[0] + ' '*(maxWidth - num_of_letters))
                else:
                    num_spaces = maxWidth - num_of_letters
                    space_between_words, num_extra_spaces  = divmod(
                        num_spaces, len(cur) - 1
                    )
                    for i in range(num_extra_spaces):
                        cur[i] += ' '
                    res.append((' '*space_between_words).join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        res.append(' '.join(cur) + ' '*(maxWidth - num_of_letters - len(cur) + 1))
        return res 

            

            
            




        