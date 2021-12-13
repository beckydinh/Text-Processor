import sys
from PartA import Tokenizer

# Runtime Complexity: O(n)
#  O(n) - tokenize text file1
#  O(n) - tokenize text file2
#  O(n) - compute token frequency for file1
#  O(n) - compute token frequency for file2
#  O(n) - finding common tokens
# O(5n) - equivalent to O(n)
if __name__ == "__main__":
    # 3 args expected
    # python file, text file1, text file2
    if len(sys.argv) != 3:
        print("Invalid input")
    else:
        t = Tokenizer()
        f1_tokens = t.tokenize(sys.argv[1]) # O(n)
        f2_tokens = t.tokenize(sys.argv[2]) # O(n)
        if f1_tokens is None or f2_tokens is None:
            pass
        else:
            f1_freq = t.computeWordFrequencies(f1_tokens)   # O(n)
            f2_freq = t.computeWordFrequencies(f2_tokens)   # O(n)
            common = []
            # O(n)
            # iterates through each token to find common tokens
            for k, v in f1_freq.items():
                if k in f1_freq and k in f2_freq:
                    common.append(k)
            print(len(common))
