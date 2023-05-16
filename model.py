# -*- coding: utf-8 -*-
"""
Project_One Sistema con arquitectura MVC para Surveys de servicio en centros de salud.

Luis Miguel Gaviria C. - 1035916086

Operadores de Pertenencia: in - not in

Operadores de Identidad: is y is not (is devuelve True si los operandos refieren el mismo obj.)
                                      is not - devuelve True si ''' No se refieren al ''' 
"""
from datetime import date as date
import operator as op  #libreria para sorted() diccionarios por clave op.itemgetter(0) o valor op.itemgetter(1)

class User():
    
    def __init__(self):
        
        self.__name = ''
        self.__identity = 0
        self.__age = 0
        self.__eps = ''
        self.__city = ''
        self.__estrato = 0
        self.__phone = 0
        self.__date = date()
        
        
    def setName(self, name):         
        self.__name = name
        
    def getName(self):        
        return self.__name
        
    def setId(self, num):        
        self.__id = num
        
    def getId(self):        
        return self.__id
    
    def setAge(self, age):
        self.__age = age
        
    def getAge(self):
        return self.__age
    
    def setEps(self, eps):
        self.__age = eps
        
    def getEps(self):
        return self.__eps
    
    def setCity(self, city):
        self.__city = city
        
    def getCity(self):
        return self.__city
    
    def setEstrato(self, estrato):
        self.__estrato = estrato
        
    def getEstrato(self):
        return self.__estrato
    
    def setPhone(self, phone):
        self.__phone = phone
        
    def getPhone(self):
        return self.__phone        
    
    def setDate(self, date):
        self.__date = date
        
    def getDate(self):
        return self.__date
    
#·-------------------------------

class Centre():
    
    def __init__(self):
        self.__name = ''
        self.__city = ''
        self.__adress = ''
        self.__level = ''
        self.__service = []        
        self.__benefited = 0
        
    def setName(self, name):
        self.__name = name
        
    def getName(self):
        return self.__name
        
    def setCity(self, city):
        self.__city = city
        
    def getCity(self):
        return self.__city
    
    def setAdress(self, adress):
        self.__adress = adress
        
    def getAdress(self):
        return self.__adress
    
    def setLevel(self, level):
        self.__level = level
        
    def getLevel(self):
        return self.__level
    
    def setService(self, service):
        self.__service.append(service)
        
    def getService(self):
        return self.__service
    
    def setBenefited(self, benefited):
        self.__benefited = benefited
        
    def getBenefited(self):
        return self.__benefited
    
#--------------------------------------

class Survey():
    
    def __init__(self):  #Constructor
        self.__qualification = 0
        self.__userData = {}
        self.__centerData = ''  # tipo atributo redefinido por metodo getCenterData..
        self.__consecutive = 0
        
    def setQualification(self, qualification):
        self.__qualification = qualification
        
    def getQualification(self):
        return self.__qualification
    
    def setUserData(self, user):  #key as document user, value as object user.
        self.__userData[user.getId()] = user
        
    def getUserData(self):
        return self.__userData
    
    def setCenterData(self, centre):
        self.__centerData = centre  #centre de tipo objeto.
        
    def getCenterData(self):
        return self.__centerData
    
    def setConsecutive(self):  #método para asignar consecutivo alfanumerico automático
        self.__consecutive = format(id(self), 'x')  #identificador hexadecimal del objeto mismo
        
    def getConsecutive(self):
        return self.__consecutive
    
#------------------------------------------

class System():  #operador relacional != , == , >= 
    
    def __init__(self):  #Constructor of class, atributo survey de tipo dict.
        self.__survey = {}
        
        
    def addSurvey(self, survey):
        self.__survey[survey.getConsecutive()] = survey  #key as consecutive atribute
        
    #---------------------------------------------------------------------
    def analyse(self):  #metodo para clasificar mejores hospitales según encuestas.        
        
        vector_hospitals = []
        var = {}  #dict clave nombre hospital - valor: sumatoria calificaciones
        sumatoria = 0   
        #vector_survey = list(self.__survey.values())  #lista de tipo objetos(Survey)
        
        for x in list(self.__survey.values()):  #convertir valores del dict a lista para iterar           
            
            if x.getCenterData().getName() not in vector_hospitals:  # x objeto encuesta, invoca método que retorna objeto centro y metodo de nombre de centro
                vector_hospitals.append(x.getCenterData().getName())
            else:
                continue
        
        for k in vector_hospitals:
            
            for x in list(self.__survey.values()):
                
                if k == x.getCenterData().getName():  # x objeto encuesta, invoca método que retorna objeto centro y metodo de nombre de centro
                    sumatoria += x.getQualification()
                else:
                    continue
                
            var[k] = sumatoria  #clave nombre centro. valor sumatoria de Qualificaciones
            sumatoria = 0  #inicializar valor de acumulador de Qualif.   
            
        # Método sorted devuelve lista de tuplas cuando se aplica a diccionarios    
        var_sort = sorted(var.items(), key=op.itemgetter(1), reverse=True)
        return var_sort               
             
   
# for name in enumerate(clients_sort):
#     print(name[1][0], 'has spend', clients[name[1][0]])        


#---------------------------
fallback_phone = '+e00000000'

def get_phone():
    
    phone = input("Please provide your phone : ")
    if not phone:
        return fallback_phone.round()
    
    return int(phone)

def run():
    my_phone = get_phone()
    print(f'Your Phone is: {my_phone}')

def main():
    
    run()
    
if __name__ == "__main__":
    
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
    
    

    
    
    