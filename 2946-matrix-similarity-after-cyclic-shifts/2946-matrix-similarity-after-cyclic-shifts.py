class Solution(object):
    def areSimilar(self, mat, k):
        n = len(mat[0])   # number of columns
        shift = k % n     # effective shift
        
        for i in range(len(mat)):
            row = mat[i]
            
            if i % 2 == 0:
                # even index → left shift
                shifted = row[shift:] + row[:shift]
            else:
                # odd index → right shift
                shifted = row[-shift:] + row[:-shift]
            
            if shifted != row:
                return False
        
        return True