class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        # create a 26-length character array for character-mappings
        mappings = [None for i in range(26)]
        mappings_length = [0 for i in range(26)]

        # how to generate mappings?
        # we can generate all possible valid mappings by using the length of each mapping
        for c in s:
            idx = ord(c) - 97
            # assign a value
            if mappings_length[idx] == 0:
                mappings_length = 1
        # validate mapping..?
            

    def validate_mapping(self, pattern, s, mappings):

    
