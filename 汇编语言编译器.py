# -*- coding: utf-8 -*-

#一个简单的hack汇编编译器（即文本处理器），根据编译过程，总共分三个模块，启动、解析和解码。



# 解码

def compcode(ccommond):
    
    diccomp={"0":"0101010","1":"0111111","-1":"0111010","D":"0001100","A":"0110000","!D":"0001101","!A":"0110001",
    "-D":"0001111","-A":"0110011","D+1":"0011111","A+1":"0110111","D-1":"0001110","A-1":"0110010","D+A":"0000010",
    "D-A":"0010011","A-D":"0000111","D&A":"0000000","D|A":"0010101","M":"1110000","!M":"1110001","-M":"1110011",
    "M+1":"1110111","M-1":"1110010","D+M":"1000010","D-M":"1010011","M-D":"1000111","D&M":"1000000","D|M":"1010101"}
    
    code=diccomp[ccommond]
    return code
    
def destcode(ccommond):    
    dicdest={"M":"001","D":"010","MD":"011","A":"100","AM":"101","AD":"110","AMD":"111"}
    code=dicdest[ccommond]
    return code
    
def jumpcode(ccommond):       
    dicjump={"JGT":"001","JEQ":"010","JGE":"011","JLT":"100","JNE":"101","JLE":"110","JMP":"111",}
    code=dicjump[ccommond]
    return code
 
         
def symbolcode(ccommond):
    ram=16
    if  ccommond in symbol:
        code=symbol[ccommond]
        return code
    else:             
        symbol[ccommond]=ram
        ram=ram+1
        code=symbol[ccommond]
        return code
    

       
#解析  
     
def firstread():
#处理命令中的伪代码（）
    rom=-1
    for line in f:
        if  not ("(" in line): 
            rom=rom+1
        else:
            line=line.replace("\n","")
            line=line.replace("(","")
            line=line.replace(")","")
            symbol[line]=rom+1
      
def secondread(): 
# 区分AC命令，并调用解码过程          
    for line in f:
        if   "@" in line:
            line=line.strip()
            str=line[1:]
            str=str.replace("\n","")
            if  not str.isdigit():
                str=symbolcode(str)                            
                num=bin(int(str)).replace("0b","")
                compile=num.zfill(16)
            else:  
                num=bin(int(str)).replace("0b","")
                compile=num.zfill(16)          
        else:
            if "=" in line:
                line=line.strip()
                dest=line[:(line.index("="))]
                comp=line[2:]                
                d=destcode(dest)
                comp=comp.replace("\n","")
                comp=comp.replace("=","")                
                c=compcode(comp)               
                compile="111"+c+d+"000"                           
            else:
                    if   ("(" in line): 
                        compile=1                   
                    else:
                        
                        line=line.strip()                      
                        comp=line[0]
                        jump=line[2:]
                        jump=jump.replace("\n","")
                        j=jumpcode(jump)                
                        c=compcode(comp)                
                        compile="111"+c+"000"+j                
        if compile==1:
            pass
        else:            
            cf.write(compile)
            cf.write("\n")    


# 启动

symbol={"R0":"0","R1":"1","R2":"2","R3":"3","R4":"4","R5":"5","R6":"6","R7":"7",
          "R8":"8","R9":"9","R10":"10","R11":"11","R12":"12","R13":"13","R14":"14","R15":"15", 
          "SP":"0","LCL":"1","ARG":"2","THIS":"3","THAT":"4","SCREEN":"16384","KBD":"24576"} 
f=open("C:/Users/xgr/Desktop/abc.txt","r")
firstread()
f.close()
f=open("C:/Users/xgr/Desktop/abc.txt","r")
cf=open("C:/Users/xgr/Desktop/abcd.txt","w")
secondread()
f.close()
cf.close()
   



    
            
            
        
    

