# -*- coding: utf-8 -*-
"""
Created on Mon May 11 21:41:03 2020

@author: jesus
"""
from tkinter import *
from tkinter import ttk,messagebox       #Librerías para la interfaz gráfica/Libraries for GUI
import re                                #Librería de expresiones regulares/Regular expression library
import datetime as dt                    #Librería para validar edad/Library to validate ages

#Lee para entender los nombres de las variables de tkinter/Read to understand the tkinter variable names
#Variables from tkinter:
#+ -> indica nombre, apellidos, correo, usuario, contraseña etc.../indicates name, last names, email, user, password etc...
#l+ -> Label              Etiqueta con texto/Label with text
#E+ -> Entry              Entrada de dato/Datum entry
#var+ -> StringVariable   Texto variable/Variable text
#lv+ -> Label             Etiqueta con texto variable/Variable text label
#cb+ -> Combobox          Menú desplegable/Dropdown menu
#el# -> Label             Etiquetas vacías de espacio/Emply labels for space

#Se crea la clase, el objeto será uen nuevo usuario/A class is created, the objet will be a new user
#Atrubutos: nombre, apellido paterno, apellido maetno, nickname o usuario, contraseña, correo, fecha de nacimiento, pregunta y respuesta de seguridad
#Attrubutes: name, both last names, nickname, password, email, birthdate, securuty question and answer
#Método: Registra->añade los atributos del objeto en un archivo csv.
#Method: Registra->ppends object attributes to a csv. file
class Nuevo_Usuario:
    def __init__(self,nickname,contraseña,correo,nombre,apellidop,apellidom,nacimiento,pregunta,respuesta):
        self.name=nombre
        self.apM=apellidom
        self.apP=apellidop
        self.NkNe=nickname
        self.__psswd=contraseña #Privada para que no se pueda obtener/Private so it can't be obtained
        self.email=correo
        self.birth=nacimiento
        self.quest=pregunta
        self.__answ=respuesta
    
    def Registra(self):
        with open('UsuariosBlackSite.csv','r') as UBS:
            lines=0
            for linea in UBS:
                lines+=1
        with open('UsuariosBlackSite.csv','a') as UBS: #Base de datos/Database
            w=str(lines)+','+self.NkNe+','+self.__psswd+','+self.email+','+self.name+','+self.apP+','+self.apM+','+str(self.birth)+','+self.quest+','+self.__answ+'\n' #Añade al archivo los datos del usuario/Appends to the file the user's data
            UBS.write(w)

#----------------------------------------------------------------------------------------            
def Ventana_Registra():     #Función 1. Crea una ventana para registrar usuarios/Function 1. Creates a new windor to register users
    
    def Valida():  #Función 1.1 Captura y valida los datos ingresados por el usuario. Muestra los errores que tuvo/Function 1.1 Captures and validates the entered data. Shows the errors the user had
        errores=[] #Lista para obtener el tipo de error los campos de entrada/list to obtain error type of the entries
        varn.set('')
        varap.set('')
        varam.set('')
        vare.set('')
        varu.set('')
        varc.set('')
        lvc2.config(fg='black')
        varc2.set('')
        varf.set('') #Se borra el texto variable para evitar errores/The variable text is deleted to avoid mistakes
        
        names = re.compile('([A-ZÑÁÉÍÓÚ]{1})([a-zñáéíóú]+)$') #Expresión regular->Empieza con una mayúscula seguida de minúsculas, permite ñ y acentos/Regular expression->Starts with an upper letter followed by lowers, allows ñ and accent marks
        nombre=En.get() #Se obtiene lo que el usuario escribió/What the user wrote is obtained
        if not names.match(nombre): #Si no sigue la expresión regular o patrón, añade a la lista de errores 'Nombre'/If the entry does not match th regular expression or pattern, 'Nombre' (name) is appended to the error list
            errores.append('Nombre')
            
        apellidop=Eap.get()
        if not names.match(apellidop): #Lo mismo que en nombre, ahora con el primer apellido/The same as the name, but now with the first last name
            errores.append('Apellido Paterno')
            
        apellidom=Eam.get()
        if not names.match(apellidom): #Lo mismo que en nombre, ahora con el segundo apellido/The same as the name, but now with the second last name
            errores.append('Apellido Materno')
        
        correoc = re.compile('^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,4})+$') #Correo electrónico->Empeza con series de mayúsculas, minúsculas, dígitos, punto, guión o guión bajo, seguido de un '@' y el dominio/Email->Starts with a serie of upper, lower letters, digits, dot, hyphen or underscore, followed by an '@' and the domine
        correo=Ee.get()
        if not correoc.match(correo):
            errores.append('Correo')
        
        nickname=Eu.get()
        with open('UsuariosBlackSite.csv','r') as UBS:
            lectura=[]
            rep=0
            for linea in UBS:
                lectura=linea.split(',')
                if str(lectura[1])==str(nickname):
                    errores.append('Usuario ya registrado')   #Antes de validar la sintaxis, revisa si ya hay un usuario registrado con ese apodo/Before validating the syntax, it checks if there is already the nickname registered
                    break
                elif rep==0:
                    nicknamec = re.compile('(?=.*[a-zA-Z0-9])([A-Za-z\d\-_]){2,}$') #Longitud de mínimo dos caracteres.Contiene, al menos, una mayúscula, minúscula o dígito/Length of minumum two characters. Contains, at least, an upper, a lower letter or a digit.
                    if not nicknamec.match(nickname):
                        rep+=1
                        errores.append('Caracteres')
        
        contraseña=Ec.get()
        contraseñac = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@+!%*?&])([A-Za-z\d+@$!%*?&]){8,15}$') #Longitud 8-15 caracteres. Contiene, al meons, una mayúscula, minúscula, dígito y caracter. Caracteres permitidos: $@+!%*?&/Length 8-15 characters. Contains, at least, an upper letter, a lower letter, a digit and a character. Allowed characters: $@+!%*?&
        if not contraseñac.match(contraseña): #Si no cumple las características, ni siquiera revisa la 'segunda' contraseña/If the password does not match, it does not even check the 'second'
            errores.append('Contraseña')
        else:
            contraseña2=Ec2.get() #Revisa la igualdad de las contraseñas/hecks the passwords equality
            if contraseña!=contraseña2:
                errores.append('Contraseña 2')
            
        dia=cbd.get()
        mes=cbm.get()
        año=cba.get()
        fecha_str=str(dia)+'-'+str(mes)+'-'+str(año)
        try:
            fecha = dt.datetime.strptime(fecha_str, "%d-%m-%Y").date() #Intenta crear la fecha (p.e.: 31-02-2020)/Tries creating the date (e.g.: 2020-02-31)
            hoy=dt.date.today()
            edad=hoy.year-fecha.year-((hoy.month,hoy.day)<(fecha.month,fecha.day)) #Calcula la edad del usuario/Calculates the user's age
            if edad<18: #El susario tiene que tener 18 o más/The user must be 18 or more
                errores.append('Edad') 
        except:
            errores.append('Fecha')
            
        pregunta=cbp.get() 
        respuesta=Ers.get() 
        
        if len(errores)==0: #Si no hay errores, registra al usuario/If there is no errors, creates the user.
            NewUser=Nuevo_Usuario(nickname,contraseña,correo,nombre,apellidop,apellidom,fecha,pregunta,respuesta)
            NewUser.Registra()
            messagebox.showinfo('BlackSite Message','Registro con éxito') #Avisa del registro/Advices of registration
            R.destroy() #Cuando se cierra el mensaje, se cierra la ventana/When closing the message, the window closes too
        else:
            for i in errores: #Modifica el texto según los errores obtenidos. Aparecerán en rojo/Modifies the text acorging to the obtained errors. They will appear in red.
                if i=='Nombre':
                    varn.set('Sigue el formato: Aaaa \nCaracteres permitidos: Ññ y vocales con acento')
                if i=='Apellido Paterno':
                    varap.set('Sigue el formato: Aaaa \nCaracteres permitidos: Ññ y vocales con acento')
                if i=='Apellido Materno':
                    varam.set('Sigue el formato: Aaaa \nCaracteres permitidos: Ññ y vocales con acento')
                if i=='Correo':
                    vare.set('ejemplo@dominio.aa\nejemplo@dominio.aa.aa\nejemplo@dominio.aa.aa.aa\nCaracteres permitidos: _ - .')
                if i=='Usuario ya registrado':
                    varu.set('Usuario ya registrado')
                if i=='Caracteres':
                    varu.set('No espacios\nCaracteres permitidos:_ -')
                if i=='Contraseña':
                    varc.set('8-15 caracteres\nAl menos una letra mayúscula, minúscula, dígito y caracter\nCaracteres permitidos:$@+!%*?&')
                if i=='Contraseña 2':
                    lvc2.config(fg='red3')
                    varc2.set('Las contraseñas no coincidieron')
                if i=='Edad':
                    varf.set('Debes ser mayor de 18 años para poder registrarte')
                if i=='Fecha':
                    varf.set('Fecha no válida')
    
    R=Tk() #Crea los widgets de la ventana/Create the window's widgets
    R.title('Registro a BlackSite')
    R.resizable(0,0)
    R.geometry("950x500")
    R.iconbitmap("BlackSite.ico")
    R.config(bg="white")
    bienv=Label(R, text="¡Regístrate en BlackSite®!",bg="white",fg="black",font=("Arial Black",15, "bold"))

    ln=Label(R,text='Nombre',bg="white",fg="black",font=("Arial",10))
    En=Entry(R)
    varn=StringVar(R)
    lvn=Label(R,textvariable=varn,bg="white",fg="firebrick3",font=("PMingLiU",7, "italic"))

    lap=Label(R,text='Apellido Paterno',bg="white",fg="black",font=("Arial",10))
    Eap=Entry(R)
    varap=StringVar(R)
    lvap=Label(R,textvariable=varap,bg="white",fg="firebrick3",font=("PMingLiU",7, "italic"))

    lam=Label(R,text='Apellido Materno',bg="white",fg="black",font=("Arial",10))
    Eam=Entry(R)
    varam=StringVar(R)
    lvam=Label(R,textvariable=varam,bg="white",fg="firebrick3",font=("PMingLiU",7, "italic"))

    le=Label(R,text='Correo Electrónico',bg="white",fg="black",font=("Arial",10))
    Ee=Entry(R)
    vare=StringVar(R)
    lve=Label(R,textvariable=vare,bg="white",fg="firebrick3",font=("PMingLiU",7, "italic"))

    lu=Label(R,text='Usuario',bg="white",fg="black",font=("Arial",10))
    Eu=Entry(R)
    varu=StringVar(R)
    lvu=Label(R,textvariable=varu,bg="white",fg="firebrick3",font=("PMingLiU",7, "italic"))

    lc=Label(R,text='Contraseña',bg="white",fg="black",font=("Arial",10))
    Ec=Entry(R,show='•')
    varc=StringVar(R)
    lvc=Label(R,textvariable=varc,bg="white",fg="firebrick3",font=("PMingLiU",7, "italic"))

    lc2=Label(R,text='Vuelve a escribir la contraseña',bg="white",fg="black",font=("Arial",10))
    Ec2=Entry(R,show='•')           #Como es contraseña, muestra viñetas/As it is a password, it shows bullets
    varc2=StringVar(R,value="*Las 2 contraseñas deben coincidir")
    lvc2=Label(R,textvariable=varc2,bg="white",fg="black",font=("PMingLiU",7, "italic"))

    ldn=Label(R,text='Día de nacimiento',bg="white",fg="black",font=("Arial",10))
    listad=[]
    for i in range(31): #Crea los valores de los días/Creates the days' list
        listad.append(str(i+1))
    cbd=ttk.Combobox(R,values=listad,width="3",state='readonly')

    lmn=Label(R,text='Mes de nacimiento',bg="white",fg="black",font=("Arial",10))
    listam=[]
    for i in range(12): #Crea los valores de meses/Creates the months' list
        listam.append(str(i+1))
    cbm=ttk.Combobox(R,values=listam,width="2",state='readonly')

    lan=Label(R,text='Año de nacimiento',bg="white",fg="black",font=("Arial",10))
    listaa=[]      #Crea los valores de el año actual menos 100 años/Creates the years' list from acutal minus 100 years
    añohoy=dt.date.today().year
    for i in reversed(range(añohoy-101,añohoy)):
        listaa.append(i+1)
    cba=ttk.Combobox(R,values=listaa,width="4",state='readonly')
    
    varf=StringVar(R)
    lvf=Label(R,textvariable=varf,bg="white",fg="firebrick3",font=("PMingLiU",7, "italic"),anchor='w')

    lps=Label(R,text='Pregunta de seguridad',bg="white",fg="black",font=("Arial",10))
    listapreg=['¿Cuál es el apellido materno de mi madre?','¿Cómo se llamó mi primera mascota?','¿En que calle se encontraba mi primer hogar?','¿Cómo se llama mi mejor amigo?','¿En qué secundaria estudié?']
    cbp=ttk.Combobox(R,values=listapreg,width=37,state='readonly')
    varps=StringVar(R,value="Esto es por si no recuerdas tu contraseña")
    lvps=Label(R,textvariable=varps,bg="white",fg="black",font=("PMingLiU",7, "italic"))

    lrs=Label(R,text='Respuesta de seguridad',bg="white",fg="black",font=("Arial",10))
    Ers=Entry(R,show='⋆') #en vez de viñetas muestra estrellas/Instead of bullets, it shows stars

    Validar=Button(R, text="Registrar",bg="white", fg="black",command=Valida) #Llama a la función 1.1/Calls to the finction 1.1

    el1=Label(R,bg='white')
    el2=Label(R,bg='white')
    el3=Label(R,bg='white')
    el4=Label(R,bg='white')

    bienv.grid(row=0,column=0,columnspan=4,pady=30)  #Carga los elementos como cuadrícula con filas y columnas/Packs the widgets as a grid with rows and columns
    ln.grid(row=1,column=0)
    En.grid(row=2,column=0,padx=30)
    lvn.grid(row=3,column=0)
    lap.grid(row=1,column=1)  
    Eap.grid(row=2,column=1,padx=30)  
    lvap.grid(row=3,column=1)  
    lam.grid(row=1,column=2)  
    Eam.grid(row=2,column=2,padx=30)  
    lvam.grid(row=3,column=2)  
    le.grid(row=1,column=3)
    Ee.grid(row=2,column=3,padx=30)  
    lve.grid(row=3,column=3) 

    el1.grid(row=4,column=0)
    lu.grid(row=5,column=0)
    Eu.grid(row=6,column=0)
    lvu.grid(row=7,column=0)
    lc.grid(row=5,column=1)
    Ec.grid(row=6,column=1)
    lvc.grid(row=7,column=1) 
    lc2.grid(row=5,column=2)
    Ec2.grid(row=6,column=2)
    lvc2.grid(row=7,column=2)

    el2.grid(row=8,column=0)
    ldn.grid(row=9,column=0)
    cbd.grid(row=10,column=0)
    lmn.grid(row=9,column=1)
    cbm.grid(row=10,column=1)
    lan.grid(row=9,column=2)
    cba.grid(row=10,column=2)
    lvf.grid(row=9,column=3,rowspan=2)

    el3.grid(row=11,column=0)
    lps.grid(row=12,column=0)
    cbp.grid(row=13,column=0,padx=30)
    lvps.grid(row=14,column=0)
    lrs.grid(row=12,column=1)
    Ers.grid(row=13,column=1)

    el4.grid(row=15,column=0)
    Validar.grid(row=16,column=3)

    R.mainloop()
#----------------------------------------------------------------------------------------
def Ventana_Recupera_Contraseña(): #Función 2. Crea ventana para recuperar contraseña/Function 2. Creates a window to recover password
    def Valida(): #Función 2.1 Pasa el filtro del usuario y correo/Function 2.1 Passes both the user and the mail filter
        def Valida2(): #Función 2.1.1 Pasa el filtro de la pregunta de seguridad y muestra contraseña/Function 2.1.1 Passes the security question filter and shows the password
            ltc=Label(RC, text="Tu contraseña es: ",bg="white",fg="black",font=("Arial",10))
            vartc=StringVar(RC)
            lvtc=Label(RC, textvariable=vartc ,bg="white",fg="black",font=("Arial",10))
            
            respuesta=Ers.get()
            usuario=Eu.get()
            with open('UsuariosBlackSite.csv','r') as UBS:
                lectura=[]
                for linea in UBS:
                    lectura=linea.split(',')
                    if lectura[1]==usuario:
                        if lectura[9].replace('\n','')==respuesta: #Compara la base de datos con la entrada/Compares the database and the entry
                            bi2.config(state='disable')
                            RC.geometry("730x330") #Amplía la wntana/Widens the window
                            varrs.set('')
                            vartc.set(lectura[2])
                            el3.grid(row=9,column=0) #Coloca las etiquetas de la contraseña/Packs the pasword's labels
                            ltc.grid(row=10,column=0)
                            lvtc.grid(row=10,column=1)
                        else:
                            varrs.set('Respuesta incorrecta') #Si no concuerda, avisa/Advidces if the password does not match
                        
        bi2=Button(RC, text="Ingresar",bg="white", fg="black",command=Valida2)
        varu.set('')
        varc.set('')
        
        usuario=Eu.get()
        correo=Ec.get()
        
        with open('UsuariosBlackSite.csv','r') as UBS:
            lectura=[]
            hay=0
            for linea in UBS:
                lectura=linea.split(',')
                if lectura[1]==usuario: #Valida el usuario/Validates the username
                    hay=1
                    if lectura[3]==correo: #Valida el correo/Validates the email
                        bi.config(state='disable') #Una vez pasado el filtro, bloque el botón/Once the filters are passed, the button locks
                        varps.set(lectura[8]) #Imprime la pregunta de seguridad/Prints the secuity question
                        RC.geometry("730x270")
                        el2.grid(row=5,column=0) #Carga la pregunta de seguridad y un entry/Packs the security questiond and an entry
                        lps.grid(row=6,column=0)
                        lvps.grid(row=7,column=0)
                        lrs.grid(row=6,column=1)
                        Ers.grid(row=7,column=1)
                        lvrs.grid(row=8,column=1)
                        bi2.grid(row=7,column=2)
                        
                    else:
                        varu.set('')
                        varc.set('El correo no coincide') #Muestra si el correo no coincide/Shows if the email does not match
            if hay==0:
                varc.set('')
                varu.set('No existe el usuario') #Muestra si el usuario no existe/Shows if the user does not exist
    
    RC=Tk()
    RC.title('Recupera tu contraseña de BlackSite')
    RC.resizable(0,0)
    RC.geometry("620x150")
    RC.iconbitmap("BlackSite.ico")
    RC.config(bg="white")
    rec=Label(RC, text="¡Recupera tu contraseña BlackSite!",bg="white",fg="black",font=("Arial Black",15, "bold"))
    
    lu=Label(RC, text="Usuario",bg="white",fg="black",font=("Arial",10))
    Eu=Entry(RC)
    varu=StringVar(RC)
    lvu=Label(RC,textvariable=varu,bg="white",fg="black",font=("PMingLiU",8, "italic"))
    
    lc=Label(RC, text="Correo",bg="white",fg="black",font=("Arial",10))
    Ec=Entry(RC,show='•')
    varc=StringVar(RC)
    lvc=Label(RC,textvariable=varc,bg="white",fg="black",font=("PMingLiU",8, "italic"))
    
    bi=Button(RC, text="Ingresar",bg="white", fg="black",command=Valida) #Cuando es presionado, va a la función 2.1/When pressed, goes to function 2.1
    
    lps=Label(RC, text="Pregunta de Seguridad",bg="white",fg="black",font=("Arial",10))
    varps=StringVar(RC)
    lvps=Label(RC,textvariable=varps,bg="white",fg="black",font=("PMingLiU",10, "italic"))
    
    lrs=Label(RC, text="Respuesta de seguridad",bg="white",fg="black",font=("Arial",10))
    Ers=Entry(RC,show='•')
    varrs=StringVar(RC)
    lvrs=Label(RC,textvariable=varrs,bg="white",fg="black",font=("PMingLiU",8, "italic"))
    
    el1=Label(RC,bg='white')
    el2=Label(RC,bg='white')
    el3=Label(RC,bg='white')
    
    rec.grid(row=0,column=1,rowspan=3,pady=30)
    el1.grid(row=1,column=0)
    
    lu.grid(row=2,column=0)
    Eu.grid(row=3,column=0,padx=10)
    lvu.grid(row=4,column=0)
    lc.grid(row=2,column=1)
    Ec.grid(row=3,column=1,padx=10)
    lvc.grid(row=4,column=1)
    bi.grid(row=3,column=2,padx=10)
#----------------------------------------------------------------------------------------
def Inicio_Sesión(): #Función 3 Valida que existan los datos y muestra mensaje de inicio de sesión/Function 3. Validates that the data exists and shows a login-message
    usuario=Eu.get()
    contraseña=Ec.get()
    
    with open('UsuariosBlackSite.csv','r') as UBS:
        lectura=[]
        hay=0    #Variable para conocer si hay usuario registrado o no/Variable to know if there is, or not, a registered user
        for linea in UBS:
            lectura=linea.split(',')
            if lectura[1]==usuario:
                hay=1
                if lectura[2]==contraseña:
                    messagebox.showinfo('BlackSite Message','Sesión iniciada con éxito')
                    MW.destroy()  #Cuando se cierra el mensaje, se cierra la ventana/When closing the message, the window closes too
        if hay==1:
            varu.set('')
            varc.set('Contraseña Incorrecta') #Si la contraseña no coincide y existe el usuario, avisa. /If the password does not match and the user exists, warns
            RecuperarContraseña.pack() #Se agrega la opción de recuperar contraseña solamente si existe el usuario y la contraseña no coincide/The option of recover password (func. 2) only if the user exists and the password does not match
        else:
            varc.set('')
            varu.set('Usuario no registrado') #Si el usuario no existe, avisa/Warns if the user does not exist
            
                    
#----------------------------------------------------------------------------------------
try:
    print('entra al try')
    with open('UsuariosBlackSite.csv','x') as UBS: #Crea el archivo si no existe/Creates te file if it does not exist
        print('Archivo creado')
    with open('UsuariosBlackSite.csv','a') as UBS: #Escribe los títulos de las columnas si no existe el archivo/Writes the column's names if the file does not exist
        e='#,Usuario,Contraseña,Correo Electrónico,Nombre,Apellido Paterno,Apellido Materno,Fecha de nacimiento,Pregunta de seguridad,Respuesta de seguridad\n'
        UBS.write(e)
        print('Títulos en el archivo')
except:
    print('error')


MW=Tk() #Ventana principal/Main window
MW.title('BlackSite')
MW.resizable(0,0)
MW.geometry("400x390")
MW.iconbitmap("BlackSite.ico") #Icono con el logo de la empresa/Icon with the company logo
MW.config(bg="black")
foto=PhotoImage(file="BlackSite.png")
Logo =Label(MW, image=foto,bg="black")
bienv=Label(MW, text="¡Bienvenido a BlackSite®!",bg="black",fg="white",font=("Arial Black",15, "bold"))
labeluser=Label(MW,text='Usuario',bg="black",fg="white",font=("Arial",10))
varu=StringVar()
varc=StringVar()
Eu=Entry(MW)
lu=Label(MW,textvariable=varu,bg="black",fg="white",font=("PMingLiU",8, "italic"))
labelcontra=Label(MW,text='Contraseña',bg="black",fg="white",font=("Arial",10))
Ec=Entry(MW,show='•')
lc=Label(MW,textvariable=varc,bg="black",fg="white",font=("PMingLiU",8, "italic"))
labelvacio=Label(MW,text="",bg="black",fg="white",font=("PMingLiU",2, "italic"))
Ingresar=Button(MW, text="Iniciar Sesión",bg="black", fg="white",command=Inicio_Sesión) #Si se presiona, llama a la func. 3/If pressed, calls the func. 3
Registrar=Button(MW, text="Registrarse",bg="black", fg="white",command=Ventana_Registra) #Si se presiona, llama a la func. 1/If pressed, calls the func. 1
RecuperarContraseña=Button(MW, text="Recuperar Contraseña",bg="black", fg="white",command=Ventana_Recupera_Contraseña) #Si se presiona, llama a la func. 2. No aparece hasta que se negó el acceso al usuario porque la contraseña no coincidió/If pressed, calls the func. 1. It does not appear until the access is denied because of the unmatched password

Logo.pack()
bienv.pack()
labeluser.pack()
Eu.pack()
lu.pack()
labelcontra.pack()
Ec.pack()
lc.pack()
Ingresar.pack()
labelvacio.pack()
Registrar.pack()

MW.mainloop()

