

def isNullOrEmpty(palabra):
    return palabra == None or palabra == ""



def getNombreContratante(contratante):

    if isNullOrEmpty(contratante.nombre1) and isNullOrEmpty(contratante.nombre2):
        return contratante.apellido_paterno
    
    if isNullOrEmpty(contratante.nombre2):
        return contratante.nombre1+" "+contratante.apellido_paterno+" "+contratante.apellido_materno

    return contratante.nombre1+" "+contratante.nombre2+" "+contratante.apellido_paterno+" "+contratante.apellido_materno
