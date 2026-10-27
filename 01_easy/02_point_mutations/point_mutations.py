# class DNA:
#     def __init__(self, strand):
#         self.strand = strand

#     def hamming_distance(self, other_strand):
#         strandA, strandB = sorted((self.strand, other_strand), key=len)
#         distance = 0

#         for idx in range(len(strandA)):
#             if strandA[idx] != strandB[idx]:
#                 distance += 1

#         return distance

class DNA:
    def __init__(self, strand):
        self.strand = strand

    def hamming_distance(self, comparison):
        differences = 0

        for char1, char2 in zip(self.strand, comparison):
            if char1 != char2:
                differences += 1

        return differences
