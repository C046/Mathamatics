# Try to import cupy rather than numpy
try:
    import cupy as np
# Default to numpy if cupy cannot be used.
except ImportError:
    import numpy as np
LOL = [[[[1,2,3,4,5],[5,4,3,2,1],],[14,13]],[[[10,9,8,7,6],[6,7,8,9,10],],[13,14]]]
TUPLE = ([[1,2,3,4,5],[5,4,3,2,1],],[14,13])
class Gaussian:
    def __init__(self, Tuple):
        self.zero_count = None
        # Set tuple self variable
        self.tuple = Tuple
        # Set array variable
        self.array = np.asanyarray([])
        # Check if instance of tuple
        if isinstance(Tuple, tuple) == True:
            # Set matrix variable
            self.matrix = np.column_stack(Tuple)
        else:
            self.matrix = self._imatrix_()
    def is_nested(self, array):
        # check if list is nested
        if type(array) == type([]):
            return any(isinstance(elem, list) for elem in array)
        # check if array is nested
        if type(array) == type(np.asanyarray([])):
            return any(isinstance(elem, np.asanyarray([]).__class__) for elem in array)
    
    def swap_rows(self,row_one,row_two):
        def return_count(row):
            self.zero_count = list(row).count(0)
            return self.zero_count
        
        # Check if 0 is not in row_one
        if 0 not in row_one:
            pass # No zeros found, continue without any action
        else:
            # Iterate through elements in row_one
            for element in row_one:
                # Check if the element is 0
                if element == 0:    
                    return_count(row_one) # Count zeros in row_one
                else:
                    pass # Non-zero element, continue iteration
            x1_count = self.zero_count # Store the count of zeros in x1_count
        
        # Check if 0 is not in row_two
        if 0 not in row_two:
            pass # No zeros found, continue without any action
        else:
            # Iterate through elements in row_two
            for element in row_two:
                # Check if the element is 0
                if element == 0:
                    return_count(row_two) # Count zeros in row_two
                else:
                    pass # Non-zero element, continue iteration
            x2_count = self.zero_count # Store the count of zeros in x2_count
        
        # Compare the counts of zeros and perform row swaps
        if x1_count == None:
            # insert seperate logic for row operations
            pass
        if x2_count == None:
            # insert seperate logic for row operations
            pass
        else:
            try:
                # Compare x1_count and x2_count to determine row swaps
                if x1_count <= x2_count:
                    row_one, row_two = row_two, row_one
                else:
                    row_two, row_one = row_one, row_two
            except TypeError as e:
                print(e,f"\n Printing value_counts:\n {x1_count} |\n {x2_count}")

    def _imatrix_(self):
        self.matrix = np.asanyarray([])
        if self.is_nested(self.tuple):
            if isinstance(self.tuple[0], tuple) != True:
                size = len(self.tuple[0][0][0]) - 1
                for tuples in self.tuple:
                    tuples = tuple(tuples)
                    self.matrix = np.append(self.matrix, np.column_stack(tuples))
                self.matrix = np.asanyarray(np.hsplit(np.column_stack(self.matrix), size))
                x, _, y = self.matrix.shape
                return self.matrix.reshape((x, y))
            else:
                for tuples in self.tuple:
                    self.matrix = np.column_stack(tuples)
        else:
            self.matrix = np.column_stack(self.tuple)
        return self.matrix
matrix = Gaussian(LOL).matrix

# matrix = Gaussian(TUPLE).matrix
        
    
    
        
