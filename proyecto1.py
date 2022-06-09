#======================================================================
# Declaración de variables
#======================================================================
operador=""

dict_oper={}

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
  if (operacion=='+'):#nums[1]
    nums.append(str(int(nums[0])+int(nums[1])))
  else:
    nums.append(str(int(nums[0])-int(nums[1])))  
  return nums

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

  
#======================================================================
# Programa principal 
#======================================================================
oper=["34+15","12-200"]

#cadena de prueba 
t="150 - 10"
#t="10 + 150"
nums=Operacion(t)
 
print(nums)

if (len(nums[0])>len(nums[1])):
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

formato(nums)

"""
dict_oper[1]=nums
print(dict_oper)
print(dict_oper[1][1])


print(nums)
"""