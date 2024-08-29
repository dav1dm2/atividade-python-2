#o programa calcula a media dos inputs e informa o ususario de sua situação academica

while True:
    print("bem vindo ao calculador de notas :)\n")

    nota_1 = input("digite sua primeira nota: ")
    nota_2 = input("digite sua segunda nota: ")
    nota_3 = input("digite sua terceira nota: ")

    try:
        media_das_notas = (float(nota_1) + float(nota_2) + float(nota_3))/3 

        if media_das_notas >= 10:
            print(f"Parabens! aprovado com distinção, sua media foi: {media_das_notas} :D ")
            break
        elif media_das_notas >= 7:
            print(f"aprovado, sua media foi: {media_das_notas} ")
            break
        else:
            print(f"reprovado :(, sua media foi: {media_das_notas}")    
            break
            
    except ValueError:
        print("Error: Valores não numericos >:( ")