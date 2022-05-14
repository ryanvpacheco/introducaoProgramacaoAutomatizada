from time import sleep
from traceback import print_tb
glossario = {"Python":"É uma linguagem de programação de alto nível, interpretada de script, imperativa, \n orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.",
            "Algoritimo ":"Em matemática e ciência da computação, um algoritmo é uma sequência finita de ações executáveis que visam \n obter uma solução para um determinado tipo de problema. Segundo Dasgupta, Papadimitriou e Vazirani; 'Algoritmos são procedimentos precisos, não ambíguos, padronizados, eficientes e corretos.'",
            "Variáveis":"As variáveis em Python tem um tipo, que é definido no momento em que a variável é criada por um comando de atribuição;\n Cada tipo define os valores que a variável pode armazenar; Cada tipo ocupa uma certa quantidade de nemória.",
            "IDE":"IDE, do inglês Integrated Development Environment ou Ambiente de Desenvolvimento Integrado,\n é um programa de computador que reúne características e ferramentas de apoio ao desenvolvimento de software com o objetivo de agilizar este processo.",
            "VSCODE":"O Visual Studio Code é um editor de código-fonte desenvolvido pela Microsoft para Windows, \n Linux e macOS. Ele inclui suporte para depuração, controle de versionamento Git incorporado, realce de sintaxe, complementação inteligente de código, snippets e refatoração de código.",
           }
for i in glossario :
    sleep(1)
    print("-"*100)
    print(f"{i} : \n {glossario[i]}")
print("-"*100)
print("CODIGO FINALIZADO")