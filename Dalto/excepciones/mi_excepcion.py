class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error: {err}")
        
try:
    raise MiExcepcion("jajajaj te equivocaste")
except:
    print("como vas a cometer ese error")