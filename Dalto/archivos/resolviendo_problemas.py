nombres = ["Mauricio", "Kaisy", "Luisa"]
apellidos = ["Valencia", "Villatoro","Yazbek"]

with open("nombres y apellidos.csv", "w") as arch:
    arch.writelines("Los datos son:\n") 
    # para el for en una sola linea tiene que ser dentro de un array, al inicio iria lo que se ejecutara y despues el for
    [arch.writelines(f"\nNombre: {n}\nApellido: {a}\n----------") for n,a in zip(nombres, apellidos)]
    
    '''
    este y el anterior es lo mismo solo que el anterior esta en una linea dentro de un array
    for n,a in zip(nombres, apellidos):
        arch.writelines(f"\nNombre: {n}\nApellido: {a}\n----------")
    '''