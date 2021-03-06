#======================================================================
# Declaración de variables
#======================================================================
operador=""

dict_oper={}

#======================================================================
# Declaración de funciones
#======================================================================
def formato(cadena):
  for i in range(len(cadena)):
    
    print(cadena[i])

def Operacion(cadena):
  global operador
  num=""
  nums=[]
  
  i=0
  for ch in cadena:
    
    if ch=="+" or ch=="-":
      operador=ch
      #dict_oper[1]=num
      nums.append(num)
      operacion=ch
      #nums.append(ch)      
      num=''
      ch=''    
      continue
    elif ch == " ":
      continue
    else:
      num+=ch

  nums.append(num)

  try:
    assert(len(nums[0]) <=4  and len(nums[1]) <=4)

    try:
      if (operacion=='+'):#nums[1]
        nums.append(str(int(nums[0])+int(nums[1])))
      else:
        nums.append(str(int(nums[0])-int(nums[1])))  
      return nums
    except:
      raise 
  except:
    raise

def dosEspacios(A):
  A[0]="  "+A[0]

def numEspacios(A):
  return abs(len(A[0])-len(A[1]))



def agregarEsp(A,numE):
  esp=""
  for i in range(numE):
    esp+=" "
  A[1]=esp+A[1]

def agregarEsp2(A,numE):
  esp=""
  for i in range(numE):
    esp+=" "
  A[0]=esp+A[0]

def simbolo(A):
  global operador
  A[1]=operador+" "+A[1]
  #A[1]="+ "+A[1]

def raya(A):
  ray=""
  for i in range(len(A[0])):
    ray+="_"
  ray+="__"
  #print(ray)
  A.insert(2,ray)

def raya2(A):
  ray=""
  for i in range(len(A[1])):
    ray+="_"
  ray+="__"
  #print(ray)
  A.insert(2,ray)

def resultado(A):
  num_space=len(A[2])-len(A[3])
  space=""
  for i in range(num_space):
    space+=" "

  A[3]=space+A[3]


def printFormat(status):
  if (status == False):
    rango=3
  else:
    rango=4

  for k in range(rango):
    for i in range(5):
      print(dict_oper[i+1][k],end="")
      print("    ", end="")
    
    print()

def arithmetic_arranger(oper, status=False):

  try:
    for i in oper:
      if (('/' in i) or ('*' in i) ):
        raise

    try:
      if(len(oper)>5):
        raise

      try:

        #assert len(oper)<6
        indice=1
        for t in oper:
          nums=Operacion(t)
          
          #print(nums)
          
          if ((len(nums[0])>len(nums[1])) or (len(nums[0])==len(nums[1]))):
            raya(nums)                                                                                                          
            #print(numEspacios(nums))
            agregarEsp(nums,numEspacios(nums))
            dosEspacios(nums)    
            simbolo(nums)
            resultado(nums)

          elif (len(nums[0])<len(nums[1])):
            raya2(nums)
            agregarEsp2(nums,numEspacios(nums))
            dosEspacios(nums) 
            simbolo(nums)
            resultado(nums)
          #formato(nums)
          dict_oper[indice]=nums
          indice+=1

        printFormat(status)

      except AssertionError:
        print("Error: Numbers cannot be more than four digits.")

      except ValueError:
        print("Error: Numbers must only contain digits.")

    except:
      print("Error: Too many problems.")
  except:
    print("Error: Operator must be '+' or '-'.")
  
  
#======================================================================
# Programa principal 
#======================================================================
oper=["34+698","3801+ 2"," 45+43 ","123 + 49","34-15"]
print(oper)

arithmetic_arranger(oper,True)