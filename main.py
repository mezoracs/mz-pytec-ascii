from distutils.debug import DEBUG
import colorama, os;
from colorama import Back, Fore, Style;

# General
colorama.init(autoreset=True);
redCo = Fore.RED;
yellCo = Fore.YELLOW ;
whiCo = Fore.WHITE ;

class handleAscii:
    routeDefault = "ascii/a6.txt";

    def addPath(self):
        print(f"\n{redCo}[!]{whiCo} Para continuar inserta el nombre del archivo {yellCo}[txt]");
        print(f"{redCo}[!]{whiCo} Recuerda que debe estar dentro de la carpeta {yellCo}ascii/...");
        print(f"\n{redCo}>> ", end="");
        p = str(input(""));

        if os.path.exists(f"ascii/{p}"):
            print(f"\n[!]Enhora buena! Tu archivo, en la ubicación {yellCo}ascii/{p}{whiCo} se cargó correctamente!");
            print(f"[!]Ya estás listo para seguir experimentando con tu {yellCo}ASCII{whiCo}!\n"); 
            self.routeDefault = f"ascii/{p}"
        else:
            print(f"\n{redCo}[!]{whiCo} Error! El archivo en la ubicación {yellCo}ascii/{p}{whiCo} no existe.\n");

    def handleChar(self, m):
        dictChar = { 
            "_" : "-",
            "/" : "\ ",
            "-" : "_",
            "(" : ")",
            ")" : "(",
            "´" : "'",
            "'"  : "´",
            "?" : "¿",
            "¿" : "?",
            "!" : "¡",
            "¡" : "!"
            }
        for f in range(m):
            for c in range(m[f]):
                pass;
    
    def rotHor180(self, m):
        matRot = [];
        for f in range(len(m)):
            matRot.append([]);
            for c in range(len(m[f])):
                matRot[f].append(m[len(m)-1-f][len(m[f])-1-c]);
        return matRot;

    # def rotAntihor180(self, m): 
    #     N = len(m) 

    #     for i in range(N // 2):
    #         for j in range(N):
    #             temp = m[i][j]
    #             m[i][j] = m[N - i - 1][N - j - 1]
    #             m[N - i - 1][N - j - 1] = temp

    #     for j in range(N // 2):
    #         temp = m[N // 2][j]
    #         m[N // 2][j] = m[N // 2][N - j - 1]
    #         m[N // 2][N - j - 1] = temp

    #     return m;

    def rotAntihor180(self, mat):
        m2 = [];

        for f in range(len(mat)):
            m2.append([])
            for c in range(len(mat[f])):
                m2[f].append(mat[len(mat)-1-f][len(mat[f])-1-c]);
        return m2;

    def rotHor90(self, m):
        arrFi = [];
        
        co = 0;
        fi = 0;
        mLen = len(m)-1;

        for f in range(len(m[0])):
            fi = 0;
            arrFi.append([]);
            for c in range(len(m)):
                arrFi[f].append(m[mLen-fi][co]);
                fi += 1;
            co += 1;
        return arrFi;

    def rotAntihor90(self, m): 
        return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

    def printMatrix(self, m, route):
        print(f"\n{redCo}[!]{whiCo} Ruta de la matriz impresa: {yellCo}[{route}]", "\n");
        for f in m:
            for c in f:
                print(f"{c}", end="");
            print();
        print();

    def getMaxLenArr(self, arr):
        maxL = [0];
        if len(arr) > 0:
            for l in arr:
                if len(l) > len(maxL):
                    maxL = l;
            return len(maxL);
        else:
            return [];

    def getMatrixImg(self, path):
        ascFile = open(str(path), "r");
        ascStr = ascFile.read().split("\n");
        arrAsc = [];
        matAsc = [];

        idx = 0;
        for line in ascStr:
            arrAsc.append([]);
            for c in line:
                arrAsc[idx].append(c);
            idx += 1;

        ascMaxLen = self.getMaxLenArr(arrAsc);
        for f in range(len(arrAsc)):
            matAsc.append([]);
            for c in range(ascMaxLen):
                try:
                    matAsc[f].append(arrAsc[f][c]);
                except IndexError:
                    matAsc[f].append(" ");
        return matAsc;

    def freqChar(self, mat):
        freqCharDict = dict();



        for f in range(len(mat)):
            for c in range(len(mat[f])):
                if mat[f][c] not in freqCharDict:
                    freqCharDict[mat[f][c]] = 0;
                freqCharDict[mat[f][c]] += 1;
        
        print();
        for char, val in freqCharDict.items():
            print(f"Carácter: %-5s {yellCo}%-10s{whiCo} Frecuencia: %-10s" % (char, "<-->",val));
        print();

    def exitMenu(self):
        print(f"\n{Fore.RED}Nos vemos pronto!{Fore.WHITE} Gracias por utilizar el programa!")
        return exit();

    def handleOptMenu(self, opt):
        matAsc = self.getMatrixImg(self.routeDefault);
        if opt == 0:
            self.exitMenu();
        elif opt == 1:
            self.printMatrix(matAsc, self.routeDefault)
        elif opt == 2:
            self.printMatrix(self.rotHor90(matAsc), self.routeDefault);
        elif opt == 3:
            self.printMatrix(self.rotAntihor90(matAsc), self.routeDefault);
        elif opt == 4:
            self.printMatrix(self.rotHor180(matAsc), self.routeDefault)
        elif opt == 5:
            self.printMatrix(self.rotAntihor180(matAsc), self.routeDefault);
        elif opt == 6:
            self.freqChar(matAsc);
        elif opt == 7:
            self.addPath();
            pass;
        self.handleMenu();

    def asciiSeparator(self):
        return print((Fore.RED + "||") + (Fore.RED + "=")*70 + (Fore.RED + "||"));

    def clearConsole(self):
        os.system('cls' if os.name=='nt' else 'clear');

    def handleMenu(self):
        optArr = ["Salir del programa",
                "Imprimir Ascii Art", 
                "Rotar 90 grados en sentido Horario", 
                "Rotar 90 grados en sentido Antihorario", 
                "Rotar 180 grados en sentido Horario",
                "Rotar 180 grados en sentido Antihorario",
                "Mostrar frecuencia de carácteres",
                "Cargar ascii"];
        idx = 0;
        self.asciiSeparator();
        for opt in optArr:
            print(f"{Fore.RED}{Style.BRIGHT}[{idx}]{Fore.WHITE} {opt}.");
            idx += 1;
        self.asciiSeparator();
        
        print(f"\n{Fore.RED}>>{Fore.WHITE} ", end="");
        
        while True:
            opt = int(input());
            if opt in range(0, len(optArr)):
                break;
            else:
                print(f"\n{Fore.YELLOW}{Style.BRIGHT}[Atención]{Fore.WHITE} Ingresa un número válido para continuar...")
                print(f"{Fore.RED}>>{Fore.WHITE} ", end="");
                continue;
        
        self.handleOptMenu(opt);

    def handleWelcome(self):
        asciiLogo = r"""
         ___                                   ___           ___    
        /\  \                                 /\__\         /\__\    
       /::\  \       ___         ___         /:/ _/_       /:/  /    
      /:/\:\__\     /|  |       /\__\       /:/ /\__\     /:/  /     
     /:/ /:/  /    |:|  |      /:/  /      /:/ /:/ _/_   /:/  /  ___ 
    /:/_/:/  /     |:|  |     /:/__/      /:/_/:/ /\__\ /:/__/  /\__\
    \:\/:/  /    __|:|__|    /::\  \      \:\/:/ /:/  / \:\  \ /:/  /
     \::/__/    /::::\  \   /:/\:\  \      \::/_/:/  /   \:\  /:/  / 
      \:\  \    ~~~~\:\  \  \/__\:\  \      \:\/:/  /     \:\/:/  /  
       \:\__\        \:\__\      \:\__\      \::/  /       \::/  /   
        \/__/         \/__/       \/__/       \/__/         \/__/    
        """

        self.clearConsole();
        self.asciiSeparator();
        print(Fore.RED + asciiLogo);
        self.asciiSeparator();

        print("\n");
        print(f"-> {Fore.YELLOW}Hola!{Fore.WHITE} Bienvenido a la interfaz de {Fore.RED}{Style.BRIGHT}Pytec{Fore.WHITE} aquí verás un listado de opciones.")
        print(f"-> Para continuar, {Fore.YELLOW}selecciona una de ellas{Fore.WHITE}, eligiendo su {Fore.YELLOW}número{Fore.WHITE} correspondiente.");
        print("\n");

        self.handleMenu();

def main():
    handA = handleAscii();
    handA.handleWelcome();

if __name__ == "__main__":
    main();
