#Leia o nome, sexo e idade de 5 pessoas e mostre qual o(a) mais velho(a) do grupo,
# quantos homens tem no total
# e quantas mulheres menores de idade tem no total.

#----------------------------------------------------------------------------------------------------------------------

nomevelho = ' '
idademaior = 0
velho = ' '
tothomem = 1
totmulher18 = 0
idadef = 0
pluralm = ' '
for p in range(1, 4):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo [M/F]: ')).strip()
    idade = int(input('Idade: '))

    if p == 1 and idade >= 1:
        idademaior = idade
        nomevelho = nome
        if sexo in 'Mm':
            velho = 'o'
        else:
            velho = 'a'
    if sexo in 'Mn' or 'Ff' and idade > idademaior:
        idademaior = idade
        nomevelho = nome
        if sexo in 'Mm':
            velho = 'o'
        else:
            velho = 'a'
    if sexo in 'Mm' and tothomem == 1:
        sexo = 1
        tothomem += sexo
    if idade < 18 and sexo in 'Ff':
        sexo = 1
        idade = 1
        idadef = idade
        totmulher18 += idadef
        if totmulher18 >= 2:
            pluralm = 'es'
        else:
            pluralm = ' '
print('{} é {} mais velh{} do grupo.'.format(nomevelho, velho, velho))
print('Temos {} pessoas do sexo masculino no grupo.'.format(tothomem))
print('Temos {} mulher{} menor{} de idade.'.format(totmulher18, pluralm, pluralm))
