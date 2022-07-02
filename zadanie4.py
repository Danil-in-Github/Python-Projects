class SravnenieStrok(object):
    def compare(self, A, B):
        ngrams = [A[i:i+3] for i in range(len(A))]
        count = 0
        for ngram in ngrams:
            count += B.count(ngram)
        return count/max(len(A), len(B))

if __name__ == "__main__":
    Comparator = SravnenieStrok()
    Comparator.compare("волк", "полковник")
