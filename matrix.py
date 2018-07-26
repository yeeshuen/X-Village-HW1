#import random

#from copy import deepcopy


#class Matrix:

    #def __init__(self, nrows, ncols):
    #    """Construct a (nrows X ncols) matrix"""
    #    pass

    #def add(self, m):
    #    """return a new Matrix object after summation"""
    #    pass

    #def sub(self, m):
     #   """return a new Matrix object after substraction"""
     #   pass

    #def mul(self, m):
    #    """return a new Matrix object after multiplication"""
     #   pass

    #def transpose(self):
    #    """return a new Matrix object after transpose"""
     #   pass
    
   # def display(self):
   #     """Display the content in the matrix"""
  #      pass

#---------------------------------------------------------------------------------------
import random

class Matrix:

    def __init__(self, nrows_arg, ncols_arg):
        self.nrows = nrows_arg
        self.ncols = ncols_arg
        self.random_matrix = [[random.randint(0,9) for x in range(self.ncols)] for y in range(self.nrows)]

        pass 
    def add(self, matrix):
        print("==== A + B ====")
        
        if self.nrows == matrix.nrows and self.ncols == matrix.ncols :
            for x in range(self.nrows) :
                for y in range(self.ncols) :
                    print(self.random_matrix[x][y] + matrix.random_matrix[x][y] , end=" ")
                print()
        else :
            print("Matrixs' size should be in the same size")
        
        print()
        pass

    def sub(self, matrix):
        print("==== A - B ====")

        if self.nrows == matrix.nrows and self.ncols == matrix.ncols :
            for x in range(self.nrows) :
                for y in range(self.ncols) :
                    print(self.random_matrix[x][y] - matrix.random_matrix[x][y] , end=" ")
                print()
        else :
            print("Matrixs' size should be in the same size")

        print()
        pass

    def mul(self, matrix):
        print("==== A * B ====")
        if self.ncols != matrix.nrows :
            print("matrix B rows' size must same with matrix A column' size")
        else :
            for x in range(self.nrows):
                for y in range(matrix.ncols) :
                    ans = 0
                    for z in range(self.ncols) :
                        ans = ans + self.random_matrix[x][z] * matrix.random_matrix[z][y]
                    print(ans , end=" ")
                print()
        print()

    def transpose(self , matrix):
        print("==== the transpose of A * B ====")
        if self.ncols != matrix.nrows :
            print("matrix B rows' size must same with matrix A column' size")
        else :
            for x in range(matrix.ncols):
                for y in range(self.nrows) :
                    ans = 0
                    for z in range(self.ncols) :
                        ans = ans + self.random_matrix[y][z] * matrix.random_matrix[z][x]
                    print(ans , end=" ")
                print()
        print()
    
    def display(self):
        for x in range(self.nrows):
            for y in range(self.ncols):
                print(self.random_matrix[x][y] , end=" " )
            print()
        
        print()
        return self.random_matrix

A_Rows = int(input("Enter A matrix's rows:"))
A_Cols = int(input("Enter A matrix's cols:"))

MatrixA = Matrix(A_Rows , A_Cols)
MatrixA.display()


B_Rows = int(input("Enter B matrix's rows:"))
B_Cols = int(input("Enter B matrix's cols:"))

MatrixB = Matrix(B_Rows , B_Cols)
MatrixB.display()

MatrixA.add(MatrixB)
MatrixA.sub(MatrixB)
MatrixA.mul(MatrixB)
MatrixA.transpose(MatrixB)