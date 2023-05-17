# -*- coding: utf-8 -*-
"""
Created on Thu May 11 08:28:30 2023

@author: hadaw
"""
import numpy as np
from random import choice

class Mathamatics:
    def __init__(self, *args,**kwargs):
        super().__init__()
        self.i,self.j = None,None
        self.symbols = None
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def transform(self, XYZ, CONSTANT_TERMS):
        # Define an inner function to check if input arguments are arrays or not
        def _isARRAY(XYZ, CONSTANT_TERMS):
            # Create a list containing the input arguments
            grouping = [XYZ, CONSTANT_TERMS]
            # Create an empty list to store the arrays that are identified in the input
            result = []
            # Keep looping as long as XYZ is in the grouping list
            while XYZ in grouping:
                # Convert XYZ to an array (if it isn't already) and append it to the result list
                XYZ = np.asanyarray(XYZ)
                result.append(XYZ)
                try:
                    # Try to set XYZ to CONSTANT_TERMS
                    XYZ = grouping[1]
                except Exception:
                    # If there are no more arrays to identify, yield the result list
                    yield result
                    # Remove the first element of grouping (which is XYZ) and continue looping with the new value of XYZ
                grouping.pop(0)

        # Call the _isARRAY function with the input arguments
        for result in _isARRAY(XYZ, CONSTANT_TERMS):
            # Use column_stack to stack the arrays horizontally and return the result
            return np.column_stack(tuple(result))

    def gaussian_elimination(self, XYZ=False, CONSTANT_TERMS=False,NUM_SYMBOLS=None):
        """
        Parameters
        ----------
        XYZ : LIST_OF_ARRAYS, optional
            DESCRIPTION. The default is False.
            CONSTANT_TERMS : LIST, optional
            DESCRIPTION. The default is False.

        Returns
        -------
        MATRIX
            System of linear equations represented as a matrix
        """
        self.symbols = NUM_SYMBOLS
        matrix = self.transform(XYZ,CONSTANT_TERMS)
        
        if self.symbols == None:
            pass
        print(matrix)
        
        for self.i in range(matrix.shape[0]):
            for self.j in range(matrix.shape[1]):
                try:
                    if matrix[self.j][self.i] <= matrix[self.j+1][self.i]:
                        # Set I, II values of incrementation
                        I = 0
                        II = 1
                        # Perform Swap
                        matrix[[I, II]]=matrix[[II, I]]
                        # matrix[[II, I]] = matrix[[I, II]]
                        # Perform subtraction
                        matrix[II] = matrix[II]-matrix[I]
                        # Set Swap
                        swap = True
                        # Increment swap
                        if swap == True:
                            I+=1
                            II+=1
                            # Set swap to false
                            swap = False
                    else:
                        pass
                except Exception:
                    self.i,self.j = None,None

        print("\n\n\n") 
        print(matrix)
        return matrix


# Example input data
XYZ = [[np.random.randint(1,10), np.random.randint(1,10), np.random.randint(1,10)], [np.random.randint(1,10), np.random.randint(1,10), np.random.randint(1,10)], [np.random.randint(1,10), np.random.randint(1,10), np.random.randint(1,10)]]
CONSTANT_TERMS = [10, 11, 12]

Matrix = Mathamatics().gaussian_elimination(XYZ,CONSTANT_TERMS)
