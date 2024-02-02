class y_r_f:
    def __init__(self, k):
        self.k = k

    def __repr__(self):
        return 'k'
    
    def sum(self, k):
        return 1

b = 3

a = y_r_f(b)
print(a)
