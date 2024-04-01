import unittest
def recon_num(cadena):
    cadena = str(cadena)
    diccionarioestados = {
        '0':
        { '-':1, '+':1, '1':2, '2':2, '3':2, '4':2, '5':2, '6':2, '7':2, '8':2, '9':2, '0':2},
        '1':
        { '1':2, '2':2, '3':2, '4':2, '5':2, '6':2, '7':2, '8':2, '9':2, '0':2,},
        '2':
        { '1':2, '2':2, '3':2, '4':2, '5':2, '6':2, '7':2, '8':2, '9':2, '0':2, '$':8, '.':3,'E':5},
        '3':
        {'1':4, '2':4, '3':4, '4':4, '5':4, '6':4, '7':4, '8':4, '9':4, '0':4},
        '4':
        {'1':4, '2':4, '3':4, '4':4, '5':4, '6':4, '7':4, '8':4, '9':4, '0':4, 'E':5, '$':8},
        '5':
        {'+':6, '-':6, '1':6, '2':6, '3':6, '4':6, '5':6, '6':6, '7':6, '8':6, '9':6, '0':6},
        '6':
        {'1':7, '2':7, '3':7, '4':7, '5':7, '6':7, '7':7, '8':7, '9':7, '0':7},
        '7':
        {'1':7, '2':7, '3':7, '4':7, '5':7, '6':7, '7':7, '8':7, '9':7, '0':7, '$':8},
        '8':
        {'acepta'}
        }
    estado = '0' #El estado de error está representado como -1
    esvalida = False
    for simbol in cadena:
        if simbol in diccionarioestados[estado]:
            esvalida = True
            estado = str(diccionarioestados[estado][simbol])
        else:
            esvalida = False
            estado = -1
            return esvalida
    return esvalida
    #while (estado != 8) and estado != -1:
    #    pass
        #cadena[simboloactual]
class Testautomatadetectornumeros(unittest.TestCase):
    def testenterosolo(self):
        numinput = 15
        self.assertEqual(recon_num(numinput),True)
    def testenteroconsimbolo(self):
        numinput = -15
        self.assertEqual(recon_num(numinput),True)
    def testnumexponencial(self):
        numinput = '15E-03$'
        self.assertEqual(recon_num(numinput),True)
    def testnumincorrecto(self):
        numinput = 'hola15'
        self.assertEqual(recon_num(numinput),False)




unittest.main()