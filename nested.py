''' The method or function in this module is for print nested list into the console
that's pretty easy, is not it?!'''

def lol(n):
    for i in n:
        if(isinstance(i, list)):
            lol(i)
        else:
            print(i)
       