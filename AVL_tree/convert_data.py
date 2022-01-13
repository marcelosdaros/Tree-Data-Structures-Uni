def convertData(data):
    x = data.split("/")

    dia = int(x[0])
    mes = int(x[1])*30
    ano = int(x[2])*365
    return dia+mes+ano