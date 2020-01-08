import math

class Mist: # A Data Structure to store a mimimum Set of Disjoint Intervals
    def __init__(self):
        self.data = [[-math.inf,-math.inf],[math.inf, math.inf]]
    def __len__(self):                                          # Standard Length
        return len(self.data)
    def __str__(self):                                          # Standard Print Method
        return str(self.data)

    #-----------------------------------------------------------------------------------------------#
    def guards(self,x):                                             # Check input Data Types and Size

        if not isinstance(x, list):
            raise Exception('Not a List')
        if len(x) != 2:
            raise Exception('Interval is not the correct size')
        if not isinstance(x[0], int):
            raise Exception('d is not an Int')
        if not isinstance(x[1], int):
            raise Exception('f is not an Int')
        if x[0] > x[1]:
            raise Exception('D > F')

    #-----------------------------------------------------------------------------------------------#
    def unravel(self):                                          # Unravel so [1,2],[6,7] is 1, [1,2, ..., 7]
        out = []
        for i in range(1, len(self.data)-1):
            for j in range(self.data[i][0],self.data[i][1]+1):
                out.append(j)
        return out

    #-----------------------------------------------------------------------------------------------#
    def merge(self, mist_outside):                              # Merge two mist structures
        for x in mist_outside.data[1:len(mist_outside)-1]:
            self.insert(x)

    #-----------------------------------------------------------------------------------------------#
    def intersects(self, x):                                    # Return True if hits any interval Else False

        if isinstance(x, int):
            return self.intersects1(x)
        if isinstance(x, list):
            for n in x:
                if self.intersects1(n):
                    return True
        return False        

    #-----------------------------------------------------------------------------------------------#
    def intersects1(self, x, i=0, pos = None, m = None):          
        
        i += 1
        if pos is None:
            m = len(self)
            pos  = max( math.ceil( m / (2 **  i  ) )  - 1,1)
        step = max( math.ceil( m / (2 ** (i+1) )) - 1,1)
        if x < self.data[pos][0]:
            return self.intersects1(x,i,pos-step,m)
        elif x >= self.data[pos+1][0]:           
            return self.intersects1(x,i,pos+step,m) 
        elif x > self.data[pos][1]:
            return False
        else:
            return True            

    #-----------------------------------------------------------------------------------------------#
    def insert(self,x):                                             # Merges a new interval

        self.guards(x)                                              # Type Check inputs
        d, f = x
        pos = max( math.ceil(len(self.data)/ (1 * 2)) - 1,1)
        d_pos = self.fnd_kpos(d,1,pos)                             # Find Positions
        f_pos = self.fnd_kpos(f,1,pos,'f')                             # ... 
        d_min = min(d, self.data[math.ceil (d_pos)][0])             # merge overlapping intervals
        f_max = max(f, self.data[math.floor(f_pos)][1])             # ...
        del self.data[math.ceil(d_pos):math.ceil(f_pos+.5)]         # Delete covered intervals
        self.data.insert(math.ceil(d_pos),[d_min,f_max])            # Insert New interval
        return

    #-----------------------------------------------------------------------------------------------#
    def fnd_kpos(self, d, i, pos, type='d'):                         # Find position of integer in a valid MIST
        i += 1
        step = max( math.ceil(len(self.data)/ (2 ** i)) - 1,1)
        if self.data[pos][0] <= d: 
            if type == 'f':
                if d == self.data[pos+1][0] - 1:
                    return pos + 1
            if d <= self.data[pos][1] + 1:
                return pos
            if d <= self.data[pos+1][0] - 1: 
                    return pos + .5
            return self.fnd_kpos(d,i,pos+step, type)
        return self.fnd_kpos(d,i,pos-step, type)