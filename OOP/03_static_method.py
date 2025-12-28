class Math:
    @staticmethod
    def sum(*values):
        return sum(values)
    
print(Math.sum(2,4,6,10))