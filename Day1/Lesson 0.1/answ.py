from IPython.display import display, Markdown, Latex,  Code

def display_code(code):
    display(Code(code,language='Python'))

def ex0():
    code = 'print("Hello World!")\n#print("Hello World!")'
    display_code(code)

def ex1():
    code = 'w1, w2 = "Hello", "World"\nprint(w1, w2)'
    display_code(code)

def ex2():
    code = '6 * (1 - 2)'
    display_code(code)

def ex3():
    code = 'bruce=2; bruce+4'
    display_code(code)

def ex4():
    code = """
    num_a = 0
    for c in 'The rain in Spain falls mainly in the plain.':
        if c == 'a':
            num_a += 1
    print('The letter "a" appears in your sentence ', num_a, ' times.')
    """
    display_code(code)

def ex4b():
    code = """
    num_a = len([c for c in 'The rain in Spain falls mainly in the plain.' if c == 'a'])
    print('The letter "a" appears in your sentence ', num_a, ' times.')
    """
    display_code(code)

def ex5():
    code = """
    for i in range(2,20):
        msg = 'neither'
        if i%2 == 0 and i%3 == 0:
            msg = 'both'
        elif i%2 == 0:
            msg = 'by 2'
        elif i%3 == 0:
            msg = 'by 3'

        print(i,"\t",msg)
    """
    display_code(code)

def ex5b():
    code = """
    for i in range(2,20):
        msg = 'neither'
        if i%2 == 0
            if i%3 == 0:
                msg = 'both'
            else:
                msg = 'by 2'
        elif i%3 == 0:
            msg = 'by 3'

        print(i,"\t",msg)
    """
    display_code(code)

def ex6():
    code = """
    def compare(a,b):
        if a > b: 
            return 1
        elif a == b: 
            return 0
        else: 
            return -1
    """
    display_code(code)
    
def ex7():
    code = """
    def hypotenuse(a,b):
        candidate = 0
        while candidate**2 < a**2 + b**2:
            print(candidate, "too short")
            candidate+=1
        print(candidate, "closest integer found")
        return candidate
    """
    display_code(code)
    
def ex8():
    code = """
    def slope(x1, y1, x2, y2):
        if x1 == x2: 
            print("Division per 0")
            return None
        return (y2-y1)/(x2-x1)
    """
    display_code(code)
    
def ex9():
    code = """
    def is_even(n): not bool(n%2)
    """
    display_code(code)
    