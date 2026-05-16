with open('cewl.txt', 'r') as f:
    with open ('password.txt', 'a') as new:
        for line in f:
            password=line.strip().capitalize()+'1995!\n'
            new.write(password)
