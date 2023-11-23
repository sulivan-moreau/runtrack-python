
def calcule(num1, operator, num2):      

    num1=int(num1)                      
    operator=str(operator)              
    num2=int(num2)                    

    if operator == '+' :           
        resultat=num1+num2            
    elif operator == '-':
        resultat=num1-num2
    elif operator == '*':
        resultat=num1*num2
    elif operator == '%':
         resultat=num1%num2
    elif operator == '/':
          if num2 != 0:                 
            resultat=num1/num2
          else:                       
            resultat="Cela ne se fait pas de diviser par zéro"  
    else :
        resultat="Désolé, il est impossible de calculer ça"    

    return resultat                  