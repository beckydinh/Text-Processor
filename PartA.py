import sys
import re

class Tokenizer:
    # Runtime Complexity: O(n)
    #  O(n) - opening and reading a text file
    #  O(n) - regex split at non-alphanumeric characters
    #  O(n) - filter() method
    # O(3n) - equivalent to O(n)
    def tokenize(self, textFile):
        try:
            with open(textFile, "r", encoding="utf-8") as file:
                text = file.read().lower()              # O(n)
                # split at non-alphanumeric characters
                tokens = re.split(r"[^a-z0-9_]", text)  # O(n)
                # removes empty strings from list
                tokens = list(filter(None, tokens))     # O(n)
                return tokens
        except:
            print(textFile,"not found")

    # Runtime Complexity: O(n)
    # O(n) - iterates through each token in list to compute frequency
    def computeWordFrequencies(self, tokenList):
        freq = {}
        for i in tokenList:     # O(n)
            if i not in freq:
                freq.update({i: 1})
            else:
                freq[i] += 1
        return freq

    # Runtime Complexity: O(nlogn)
    # O(nlogn) - sorting tokens by frequency
    #     O(n) - iterates through each token in dictionary to print
    def print(self, tokenDict):
        # O(nlogn)
        tokens_sorted = sorted(tokenDict.items(), key=lambda kv: kv[1], reverse=True)
        for i in tokens_sorted:     # O(n)
            print(i[0], "->", i[1])


if __name__ == "__main__":
    # 2 args expected
    # python file, text file
    if len(sys.argv) != 2:
        print("Invalid input")
    else:
        t = Tokenizer()
        tokens = t.tokenize(sys.argv[1])
        if tokens is None:
            pass
        else:
            tokens_freq = t.computeWordFrequencies(tokens)
            t.print(tokens_freq)