def str_compare(A, B):
    ngrams = [A[i:i+3] for i in range(len(A))]
    count = 0
    for ngram in ngrams:
        count += B.count(ngram)

    return count

stroki = [("меч", "печь"), ("птица", "ученица"), ("университет", "специалитет"), ("exception", "interception")]

if __name__ == "__main__":
    for s, t in stroki:
        print(s, t, str_compare(s, t))

print()

str_const = "Я пришел домой поздно вечером"
spisok = [500, "Завтрак", "Машина", str_const, "School", "Каникулы"]
for elem in spisok:
    print(elem)
