class Bar():   

    class_var = 2 

    def __init__(self, i_var):       

        self.i_var = i_var        

        self.class_var = i_var

foo = Bar(1)

print(foo.i_var, foo.class_var, Bar.class_var)
