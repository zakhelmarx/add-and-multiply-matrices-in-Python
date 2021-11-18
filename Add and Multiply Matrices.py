def transpose(function):
  def wrapper():
    #Funtion tranpose berisikan fungsi transpose suatu matrix.    
    FMatrix = function()
    FMatrix[1], FMatrix[2] = FMatrix[2], FMatrix[1]      
    return FMatrix
    #Function ini akan mengembalikan matrix tranpose dari matrix yang terdapat pada parameter di function ini.
     
  return wrapper

def matrixaddition(function1,function2):
  XaddY = []
#Function ini digunakan untuk menjumlahkan matrix X dan Y. Praktikan dilarang mendeklarasikan matrix X dan Y pada function ini.
#Nantinya matrix X dan matrix Y dipanggil sesuai pada parameter function di function ini yaitu secara berturut-turut function1 dan function2.
#Function ini akan mengembalikan list yang berupa matrix dari hasil penjumlahan matrix X dan Y.
#Nilai dari penjumlahan tersebut disimpan dalam variabel XaddY.
  for i in range(len(function1())) :
    XaddY.append(function1()[i]+function2()[i])  
  return XaddY

def matrixZmultiplyA(function):
  def wrapper():
    matrixZ = function()
    #Nantinya variabel ini digunakan untuk menyimpan matrix Z.    
    matrixA = [4,1,5,2]
    result = []
        
    result.append(matrixZ[0]*matrixA[0]+matrixZ[1]*matrixA[2])
    result.append(matrixZ[0]*matrixA[1]+matrixZ[1]*matrixA[3])
    result.append(matrixZ[2]*matrixA[0]+matrixZ[3]*matrixA[2])
    result.append(matrixZ[2]*matrixA[1]+matrixZ[3]*matrixA[3])
    
    return result
  return wrapper



#Isikan decoration untuk men-transpose-kan matrix X
@transpose
def matrixX():
  matrixX = [6,1,2,3]
  #Diasumsikan matrixX = |6  1|
                        #|2  3|
  return matrixX

#Isikan decoration untuk men-transpose-kan matrix Y
@transpose
def matrixY():
  matrixY = [3,2,4,5]
  #Diasumsikan matrixY = |3  2|
                        #|4  5|
  return matrixY

#Isikan decoration untuk mengalikan matrix Z dengan matrix A, lalu transpose hasil kali tersebut
@transpose
@matrixZmultiplyA
def resultmatrix():
  #Panggil function matrixaddition untuk menjumlahkan matrix X dan matrix Y, sesuaikan parameternya.
  matrixadd = matrixaddition(matrixX,matrixY)
  return matrixadd


print(resultmatrix())


#Note* Untuk lebih mengerti Kegiatan 2, silahkan dipahami Percobaan 4, 5, dan 6 pada modul ini!

#Test case 1:
#Input:
#matrixX = [6,1,2,3]
#matrixY = [3,2,4,5]
#matrixA = [4,1,5,2]
#Output:
#resultmatrix(transpose) = [66, 52, 21, 19]