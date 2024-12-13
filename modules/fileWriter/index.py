def save(filename,data):
    with open(filename+".txt",'w+') as file:
        file.write(data)
    print(f'{filename}.txt saved!')
