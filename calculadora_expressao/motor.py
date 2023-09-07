import re
def ordem_expressao(expression):
    operacoes = ["*","/"]
    index = 0
    for i in range(0,len(expression)):
        if expression[i] in operacoes:
            index = i
            break
    return index
    
def second_find(expression):
    operacoes = ["-","+"," ","*","/"]
    index = 0
    
    
    if expression[0] == "/":
        operacoes = ["+"," ","*","/"]
    
    elif expression[0] == "*":
        operacoes = ["+"," ","*","/"]
        
    for i in range(0,len(expression)):
        if expression[i] in operacoes:
            index = i
            break
            
    return index
    
def sinal_anterior(expression,index_multi):
    operacoes = ["-","+"," ","/"]
    index = 0
    if expression[index_multi] == "/":
        operacoes = ["-","+"," ","*"]
        
    for i in range(index_multi,0,-1):
        if expression[i] in operacoes:
            index = i
            break
    return index
    
def sinal_posterior(expression,index_multi):
    operacoes = ["-","+"," ","/"]
    index = 0
    
    if expression[index_multi] == "/":
        operacoes = ["+"," ","*"]
    
    if expression[index_multi] == "*":
         operacoes = ["+"," ","/"]
        
    for i in range(index_multi+1,len(expression)):
        if expression[i] in operacoes:
            index = i
            break
        if expression[i] == " ":
            index = len(expression)
            break
    return index

def resolve_multi(multi,resultado_multi,expression_1,index_anterior_multi,index_posterior_multi):
    
    operacoes = ["-","+"," ","*","/"]
    while "*" in expression_1:
        index_second = second_find(multi[1:len(multi)])+1
               
        if multi[0] == "-":
            resultado_multi*= float(multi[1:index_second]) * -1
            multi = multi[index_second:]
            continue
            
        elif multi[0] == "+":
            
            if resultado_multi != 1:
                resultado_multi += float(multi[1:index_second])
                multi = multi[index_second:]
                continue
            
            else:
                resultado_multi *= float(multi[1:index_second])
                multi = multi[index_second:]
                continue
        
        elif multi[0] == "*":
            
            
            if multi[1] == '-':
                index_second = second_find(multi[2:len(multi)])+2
                resultado_multi *= float(multi[2:index_second])* -1

            elif multi[1].isnumeric() == True:
                resultado_multi *= float(multi[1:index_second])
            else:
                resultado_multi += float(multi[1:index_second])
                
            if multi[index_second] == "*":
                multi = multi[index_second:]
                continue
                
            if expression_1[index_anterior_multi] in operacoes:
                expression_1 = expression_1[0:index_anterior_multi] + expression_1[index_anterior_multi] +str(resultado_multi)+ expression_1[index_posterior_multi:] + " "
               
                
                
            else:
                expression_1 = expression_1[0:index_anterior_multi]+str(resultado_multi)+ expression_1[index_posterior_multi:] + " "
                
                
                
            multi = multi[index_second:]
            resultado_multi = 1
            continue
        
        else:
            if multi == '' or multi == ' ':
                index_multi = expression_1.find("*")
                index_anterior_multi = sinal_anterior(expression_1,index_multi)
                index_posterior_multi = sinal_posterior(expression_1,index_multi)
                multi = expression_1[index_anterior_multi:index_posterior_multi] + " "
                continue
            
            multi = multi.split()
            multi.insert(0,"+")
            multi = "".join(multi)+ " "
            
            # resultado_multi*= float(multi[0:index_second])
            # multi = multi[index_second:]
            # continue
        
    return expression_1      
    
def resolve_div(resultado_div,div,expression_1,index_anterior_div,index_posterior_div):
    
    while "/" in expression_1:
        index_second = second_find(div[1:len(div)])+1
        print("in",index_second)
        print(div)
        print("res",resultado_div)
            
        if div[0] == "-":
            resultado_div += float(div[1:index_second]) * -1
            div = div[index_second:] + " "
            continue
        
        elif div[0] == "+":
            print(div)
            resultado_div += float(div[1:index_second])
            div = div[index_second:] + " "
            continue
        
        elif div[0].isnumeric == True:
            resultado_div /= float(div[1:index_second])
            div = div[index_second:]+ " "
            continue
            
        
        elif div[0] == "/":
            index_second = second_find(div[1:len(div)])+1
            
            if div[1] == '-':
                index_second = second_find(div[2:len(div)])+2
                resultado_div /= float(div[2:index_second])* -1

            else:
                resultado_div /= float(div[1:index_second])
                
                
            if div[index_second] == "/":
                div = div[index_second:]+ " "
                continue

            index_div = expression_1.find("/")
            index_anterior_div_2 = sinal_anterior(expression_1,index_div)
            index_posterior_div_2 = sinal_posterior(expression_1,index_div)
            
            if expression_1[index_anterior_div_2] == "+":
               
                expression_1 = expression_1[0:index_anterior_div_2] + expression_1[index_anterior_div_2] +str(resultado_div)+ expression_1[index_posterior_div_2:] + " "
                print("aqui0")

            else:
                
                expression_1 = expression_1[0:index_anterior_div_2]+str(resultado_div)+ expression_1[index_posterior_div_2:] + " "
                print("aqui1")
                print(expression_1)
                
            div = div[index_second:]
            resultado_div = 0
            continue
        else:
            if div == '' or div == " " or div == "  ":
                index_div = expression_1.find("/")
                index_anterior_div = sinal_anterior(expression_1,index_div)
                index_posterior_div = sinal_posterior(expression_1,index_div)
                div = expression_1[index_anterior_div:index_posterior_div] + " "
                print("aqui")
                continue
            
            div = div.split()
            div.insert(0,"+")
            div = "".join(div)+ " "
            
            # print("aqui",div)
            # resultado_div/= float(div[0:index_second])
            # print("aqui",resultado_div)
            # div = div[index_second:]
            # continue
    return expression_1

def resolve_sub_soma(expression_1):
    resultado = 0
    
    
    while "-" in expression_1 or "+" in expression_1:
        print("ex",expression_1)
        if expression_1[0] == "-":
            
            if expression_1[1] == "+":
                index_second = second_find(expression_1[2:len(expression_1)]) +1
                resultado+= float(expression_1[2:index_second]) * -1
                expression_1 = expression_1[index_second:] + " "
                continue
            
            else:    
                index_second = second_find(expression_1[1:len(expression_1)]) +1
                resultado+= float(expression_1[1:index_second]) * -1
                expression_1 = expression_1[index_second:] + " "
                continue
        
        
            
        else:
            if expression_1[0] == "+":
                index_second = second_find(expression_1[2:len(expression_1)]) +2
                print(index_second)
                resultado+= float(expression_1[1:index_second]) 
                expression_1 = expression_1[index_second:] + " "
                continue
            
            else:
                
                index_second = second_find(expression_1[1:len(expression_1)])+1
                resultado+= float(expression_1[0:index_second])
                print("Result",resultado)
                expression_1 = expression_1[index_second:] + " "
                print(expression_1)
                continue
        
        
        if "+" in expression_1:
            index_second = second_find(expression_1[1:len(expression_1)])+1
            
            if expression_1[index_second] == " ":
                resultado+= float(expression_1[1:index_second])
                expression_1 = expression_1[index_second:] 

                continue
            
            elif expression_1[0] == "+":
                resultado+= float(expression_1[1:index_second])
                expression_1 = expression_1[index_second:] + " "
                continue
            
            else:
                resultado+= float(expression_1[0:index_second])
                expression_1 = expression_1[index_second:] 
                continue
               
        if " " in expression_1:
            index_second = second_find(expression_1[1:len(expression_1)])+1
            if expression_1[index_second] == " ":
                resultado+= float(expression_1[1:index_second])
                expression_1 = expression_1[index_second:] 
            break
        
    return str(resultado)
                
def resolvedor(expression):
    expression_1 = "".join(expression.split()) + " " 
    expression_save = "".join(expression.split()) + " " 
    resultado = 0
    resultado_multi = 1
    resultado_div = 0
    
    while True:
        if  bool(re.search(r"\s", expression_1)) == True and expression_1[0] == " " : 
            break
        
        if expression_1[ordem_expressao(expression_1)] == '*':
            index_multi = expression_1.find("*")
            index_anterior_multi = sinal_anterior(expression_1,index_multi)
            index_posterior_multi = sinal_posterior(expression_1,index_multi)
            multi = expression_1[index_anterior_multi:index_posterior_multi] + " "
            expression_1 = resolve_multi(multi,resultado_multi,expression_1,index_anterior_multi,index_posterior_multi) + " "
            continue
            
              
        if expression_1[ordem_expressao(expression_1)] == '/':
            index_div = expression_1.find("/")
            index_anterior_div = sinal_anterior(expression_1,index_div)
            index_posterior_div = sinal_posterior(expression_1,index_div)
            div = expression_1[index_anterior_div:index_posterior_div] + " "
            expression_1 = resolve_div(resultado_div,div,expression_1,index_anterior_div,index_posterior_div)+ " "
            continue
            
                
        if "-" in expression_1 or "+" in expression_1:
            
            expression_1 = resolve_sub_soma(expression_1)
        break
        
                
    return expression_1
    
