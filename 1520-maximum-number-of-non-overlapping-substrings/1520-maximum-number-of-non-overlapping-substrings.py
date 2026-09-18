class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {c: i for i, c in reversed(list(enumerate(s)))}
        last = {c: i for i, c in enumerate(s)}
        
        valid_intervals = []
        
        for c in set(s):
            start = first[c]
            end = last[c]
            is_valid = True
            
            i = start
            while i <= end:
                if first[s[i]] < start:
                    is_valid = False
                    break
                end = max(end, last[s[i]])
                i += 1
                
            if is_valid:
                valid_intervals.append((start, end))
                
        valid_intervals.sort(key=lambda x: x[1])
        
        result = []
        prev_end = -1
        
        for start, end in valid_intervals:
            if start > prev_end:
                result.append(s[start:end+1])
                prev_end = end
            elif start >= first[s[prev_end]] and end <= prev_end:
                result[-1] = s[start:end+1]
                prev_end = end
                
        return result
