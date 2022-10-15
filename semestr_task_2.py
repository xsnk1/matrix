from lib2to3.pgen2.grammar import opmap_raw
from math import ceil


def summa(mat1:list, mat2:list):
    s = 0
    if len(mat1) < len(mat2):
        mat1,mat2 = mat2,mat1
    while s!= len(mat1):
        try:
            for i in range(len(mat1)):
                for k in range(len(mat1[i])):
                    mat1[i][k] = mat1[i][k] + mat2[i][k]
                s += 1
            return mat1
        except IndexError:
            return 'error'
        except TypeError:
            return 'error'      
def det(mat1:list):
    s = 0
    while s!= 1:
        try:
            if len(mat1) == 2 and len(mat1[0]) == 2 and len(mat1[1]) == 2:
                opr = mat1[0][0] * mat1[1][1] - mat1[0][1] * mat1[1][0]
                return opr
            if len(mat1) == 3 and len(mat1[0]) == 3 and len(mat1[1]) == 3 and len(mat1[2]) == 3:
                opr = (mat1[0][0]*mat1[1][1]*mat1[2][2] + mat1[0][1]*mat1[1][2]*mat1[2][0] + mat1[1][0]*mat1[2][1]*mat1[0][2]) - (mat1[2][0]*mat1[1][1]*mat1[0][2] + mat1[1][0]*mat1[0][1]*mat1[2][2] + mat1[2][1]*mat1[1][2]*mat1[0][0])
                return opr
            elif len(mat1) == 4 and len(mat1[0]) == 4 and len(mat1[1]) == 4 and len(mat1[2]) == 4 and len(mat1[3]) == 4:
                opr  = mat1[0][0]*( ( mat1[1][1]*mat1[2][2]*mat1[3][3] + mat1[1][3]*mat1[2][1]*mat1[3][2] + mat1[1][2]*mat1[2][3]*mat1[3][1] ) - ( mat1[3][1]*mat1[2][2]*mat1[1][3] + mat1[1][1]*mat1[2][3]*mat1[3][2] + mat1[2][1]*mat1[1][2]*mat1[3][3] ) )- mat1[0][1]*( ( mat1[1][0]*mat1[2][2]*mat1[3][3] + mat1[1][3]*mat1[2][0]*mat1[3][2] + mat1[1][2]*mat1[2][3]*mat1[3][0] ) - ( mat1[1][3]*mat1[2][2]*mat1[3][0] + mat1[1][0]*mat1[2][3]*mat1[3][2] + mat1[1][2]*mat1[2][0]*mat1[3][3] ) ) + mat1[0][2]*( ( mat1[1][0]*mat1[2][1]*mat1[3][3] + mat1[1][3]*mat1[2][0]*mat1[3][1] + mat1[1][1]*mat1[2][3]*mat1[3][0] ) - ( mat1[1][3]*mat1[2][1]*mat1[3][0] + mat1[1][0]*mat1[2][3]*mat1[3][1] + mat1[1][1]*mat1[2][0]*mat1[3][3] ) ) - mat1[0][3]*( ( mat1[1][0]*mat1[2][1]*mat1[3][2] + mat1[1][2]*mat1[2][0]*mat1[3][1] +  mat1[1][1]*mat1[2][2]*mat1[3][0] ) - ( mat1[1][2]*mat1[2][1]*mat1[3][0] + mat1[1][0]*mat1[2][2]*mat1[3][1] + mat1[1][1]*mat1[2][0]*mat1[3][2] ) )
                s += 1
                return opr
            else:
                return 'error'
        except IndexError:
            return 'error'
        except TypeError:
            return 'error'
def transp(mat1:list):
    s = 0
    while s != 1:
        try:
            res=[]
            n=len(mat1)
            m=len(mat1[0])
            for j in range(m):
                tmp=[]
                for i in range(n):
                    tmp=tmp+[mat1[i][j]]
                res=res+[tmp]
            return res
        except ValueError:
            return 'error'
        except TypeError:
            return 'error'
def L1(mat1:list):
    s = 0
    while s!= 1:
        try:
            max = 0
            for i in range(len(mat1)):
                s = 0
                for j in range(len(mat1[i])):
                    if mat1[i][j] < 0:
                        mat1[i][j] = mat1[i][j] * (-1)
                    s += mat1[i][j]
                if s > max:
                    max = s
            return max
        except ValueError:
            return 'error'
        except TypeError:
            return 'error'
def L0(mat1:list):
    s = 0
    while s!= 1:
        try:
            s = 0
            m = 0
            for i in range(len(mat1)):
                for j in range(len(mat1[i])):
                    if mat1[i][j] != 0:
                        s += 1
                    m += mat1[i][j]
            return s
        except ValueError:
            return 'error'
        except TypeError:
            return 'error'
def rank(mat1:list):
    s = 0
    while s!= 1:
        try:
            r = 1
            while s!= 1:
                try:
                    l = 0
                    for i in range(len(mat1)):
                        for k in range(len(mat1[i])):
                            l += mat1[i][k]
                    if int(mat1[0][0]*mat1[1][1] - mat1[0][1]*mat1[1][0]) != 0:
                        r += 1
                        while s != 1:
                            try:
                                if int( (mat1[0][0]*mat1[1][1]*mat1[2][2] + mat1[0][1]*mat1[1][2]*mat1[2][0] + mat1[1][0]*mat1[2][1]*mat1[0][2]) - (mat1[2][0]*mat1[1][1]*mat1[0][2] + mat1[1][0]*mat1[0][1]*mat1[2][2] + mat1[2][1]*mat1[1][2]*mat1[0][0]) ) != 0:
                                    r += 1
                                    while s!= 1:
                                        try:
                                            if int(mat1[0][0]*( ( mat1[1][1]*mat1[2][2]*mat1[3][3] + mat1[1][3]*mat1[2][1]*mat1[3][2] + mat1[1][2]*mat1[2][3]*mat1[3][1] ) - ( mat1[3][1]*mat1[2][2]*mat1[1][3] + mat1[1][1]*mat1[2][3]*mat1[3][2] + mat1[2][1]*mat1[1][2]*mat1[3][3] ) )- mat1[0][1]*( ( mat1[1][0]*mat1[2][2]*mat1[3][3] + mat1[1][3]*mat1[2][0]*mat1[3][2] + mat1[1][2]*mat1[2][3]*mat1[3][0] ) - ( mat1[1][3]*mat1[2][2]*mat1[3][0] + mat1[1][0]*mat1[2][3]*mat1[3][2] + mat1[1][2]*mat1[2][0]*mat1[3][3] ) ) + mat1[0][2]*( ( mat1[1][0]*mat1[2][1]*mat1[3][3] + mat1[1][3]*mat1[2][0]*mat1[3][1] + mat1[1][1]*mat1[2][3]*mat1[3][0] ) - ( mat1[1][3]*mat1[2][1]*mat1[3][0] + mat1[1][0]*mat1[2][3]*mat1[3][1] + mat1[1][1]*mat1[2][0]*mat1[3][3] ) ) - mat1[0][3]*( ( mat1[1][0]*mat1[2][1]*mat1[3][2] + mat1[1][2]*mat1[2][0]*mat1[3][1] +  mat1[1][1]*mat1[2][2]*mat1[3][0] ) - ( mat1[1][2]*mat1[2][1]*mat1[3][0] + mat1[1][0]*mat1[2][2]*mat1[3][1] + mat1[1][1]*mat1[2][0]*mat1[3][2] ) )) != 0:
                                                r += 1
                                                return r
                                            else:
                                                return r
                                        except IndexError:
                                            return r
                                        except ValueError:
                                            return 'error'
                                        except TypeError:
                                            return 'error'
                                else:
                                    return r
                            except IndexError:
                                return r
                            except ValueError:
                                return 'error'
                            except TypeError:
                                return 'error'
                    else:
                        return r
                except IndexError:
                    return r
                except ValueError:
                    return 'error'
                except TypeError:
                    return 'error'
        except IndexError:
            return r
        except ValueError:
            return 'error'
        except TypeError:
            return 'error'
def mul(mat1:list,mat2:list):
    q = 0
    while q!= 1:
        try:
            s = 0
            t = []
            m3 = []
            if len(mat2) != len(mat1[0]):
                return 'error'
            else:
                r1 = len(mat1)
                c1 = len(mat1[0])
                c2 = len(mat2[0])
                for z in range(0, r1):
                    for j in range(0, c2):
                        for i in range(0, c1):
                            s = s + mat1[z][i] * mat2[i][j]
                        t.append(s)
                        s = 0
                    m3.append(t)
                    t = []
            return m3
        except ValueError:
            return 'error'
        except TypeError:
            return 'error'
def minor(mat2,i,j):
    return [row[:j] + row[j+1:] for row in (mat2[:i]+mat2[i+1:])]
def obratn(mat2):
    opr = det(mat2)
    if len(mat2) == 2:
        return [[mat2[1][1]/opr, -1*mat2[0][1]/opr],
                [-1*mat2[1][0]/opr, mat2[0][0]/opr]]
    obr = []
    for r in range(len(mat2)):
        obrROW = []
        for c in range(len(mat2)):
            mr = minor(mat2,r,c)
            obrROW.append(((-1)**(r+c)) * det(mr))
        obr.append(obrROW)
    obr = transp(obr)
    for r in range(len(obr)):
        for c in range(len(obr)):
            obr[r][c] = obr[r][c]/opr
    return obr
def diff(mat1:list,mat2:list):
    s = 0
    while s!= 1:
        try:
            mat2 = obratn(mat2)
            otv = mul(mat1,mat2)
            for i in range(len(otv)):
                for k in range(len(otv[i])):
                    otv[i][k] = round(otv[i][k],2)
            return otv
        except ValueError:
            return 'error'
        except TypeError:
            return 'error'








                    
                    
    
                
            
            

