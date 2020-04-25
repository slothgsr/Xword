def wordfinder(arg1, arg2): #arg1 = combo,  arg2 = Gridlist
    grid = arg2.copy()
    for letter in sorted(arg1):
        if len(grid) <=1:
            break
        remove = []
        for word in grid:
            if letter in word:
                remove.append(word)             
        for i in remove:
            grid.remove(i)
                
    return len(grid)
            
            
combos = [('o', 't', 'l', 'u', 'p', 'm', 'f', 'z')
        ('p', 'm', 'g', 'w', 'x', 'z', 'j', 'q')]

Grid1 = ['bridge', 'date', 'atom', 'pry', 'rib', 'substance', 
        'napkin', 'stack', 'mode', 'nut', 'mat', 'vesel',
        'brass', 'swim', 'unit', 'aunt', 'domestic', 'explain', 
        'day', 'reckless', 'taxi', 'nsal']
         
Grid1set = ["".join(set(x)) for x in Grid1]

for i in combos:
    count = wordfinder(i, Grid1set)

