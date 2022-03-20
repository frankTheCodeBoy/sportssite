from collections import Counter
def Counter_example():
    ’’’ show some examples for Counter ’’’
    ’’’ it is a dictionary that maps the items to the number of
    occurrences ’’’
    seq1 = [1, 2, 3, 5, 1, 2, 5, 5, 2, 5, 1, 4]
    seq_counts = Counter(seq1)
    print(seq_counts)
    ’’’ we can increment manually or use the update() method ’’’
    seq2 = [1, 2, 3]
    seq_counts.update(seq2)