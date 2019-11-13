from IPython.display import display, Markdown, Latex,  Code

def display_code(code):
    display(Code(code,language='Python'))

def numpy_ex1():
    code = """
    import numpy as np
    print(np.__version__)
    """
    display_code(code)

def numpy_ex2():
    code = """
    np.isnan(a)
    """
    display_code(code)

def numpy_ex3():
    code = """
    array=np.arange(30,71); array
    """
    display_code(code)
    
def numpy_ex4():
    code = """
    v = np.linspace(5, 50, 10); v
    """
    display_code(code)

def numpy_ex5():
    code = """
    x = np.ones((10, 10))
    x[1:-1, 1:-1] = 0
    x
    """
    display_code(code)

def numpy_ex6():
    code = """
    np.save('temp_arra.npy', a)
    #x2 = np.load('temp_arra.npy')
    """
    display_code(code)

def numpy_ex7():
    code = """
    x = np.array(a)
    a2 = x.tolist()
    """
    display_code(code)

def numpy_ex8():
    code = """
    x = a.astype(float)
    x
    """
    display_code(code)

def numpy_ex9():
    code = """
    F = np.array(fvalues)
    C = 5*F/9 - 5*32/9
    C
    """
    display_code(code)

def numpy_ex10():
    code = """
    np.setxor1d(array1, array2)
    """
    display_code(code)

def numpy_ex11():
    code = """
    print("a > b")
    print(np.greater(a, b))
    print("a >= b")
    print(np.greater_equal(a, b))
    print("a < b")
    print(np.less(a, b))
    print("a <= b")
    print(np.less_equal(a, b))
    """
    display_code(code)

def numpy_ex12():
    code = """
    x.shape = (3, 3)
    x
    """
    display_code(code)

def numpy_ex13():
    code = """
    np.expand_dims(x, axis=1)
    """
    display_code(code)

def numpy_ex14():
    code = """
    np.linalg.det(a))
    """
    display_code(code)

def numpy_ex15():
    code = """
    w, v = np.linalg.eig(m); w, v
    """
    display_code(code)

def numpy_ex16():
    code = """
    x = np.random.normal(size=5); x
    """
    display_code(code)

def numpy_ex17():
    code = """
    np.random.seed(0)
    print(np.random.normal(size=5))
    np.random.seed(0)
    print(np.random.normal(size=5))
    """
    display_code(code)

def numpy_ex18():
    code = """
    np.random.randint(low=10, high=30, size=6)
    """
    display_code(code)

def numpy_ex19():
    code = """
    np.random.random((3,3,3))
    """
    display_code(code)


def matplotlib_ex1():
    code = """
    pokemon['Type 1'].value_counts().plot.bar()
    """
    display_code(code)

def matplotlib_ex2():
    code = """
    pokemon['HP'].value_counts().sort_index().plot.line()
    """
    display_code(code)

def matplotlib_ex3():
    code = """
    pokemon['Attack'].plot.hist()
    """
    display_code(code)
