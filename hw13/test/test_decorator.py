def show(function):
    def _show(x, y):
        z = function(x, y)
        print('x: %d,\ny: %d,\nz: %d' % (x, y, z)) 
        return z
    return _show

@show
def add(x, y):
    return x + y;

@show
def sub(x, y):
    return x - y;

if __name__ == '__main__':
    x = 6;
    y = 3
    z = add(x, y)
    
