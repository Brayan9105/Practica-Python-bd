import mysql.connector
import tkinter as tk
from tkcalendar import *
from tkinter import ttk
from tkinter import messagebox
import datetime
#x = datetime.datetime(2019, 12, 1)

#-------------------------------------------------------------------------------- CREACION DE VENTANAS ---------------------------------------------------------------------------

def ventana_login():

    login = tk.Tk()
    login.geometry("200x300")
    login.title("Login")

    usuario = tk.StringVar()
    passw = tk.StringVar()

    tk.Label(login, text="Login").grid(row=0,column=0, padx=30, pady=30)

    tk.Label(login, text="Usuario").grid(row=1, column=0,padx=30)
    tk.Entry(login, textvariable=usuario).grid(row=2, column=0,padx=30)

    tk.Label(login, text="Password").grid(row=3, column=0,padx=30)
    tk.Entry(login, textvariable=passw).grid(row=4, column=0,padx=30)

    tk.Button(login, text="Ingresar", width=18, command=lambda :dologin(usuario, passw, login)).grid(row=5,column=0,padx=30, pady=15)

    login.mainloop()


def ventana_opciones(login):

    login.withdraw()

    opciones = tk.Toplevel()
    opciones.geometry("500x400")
    opciones.title("Main")

    tk.Label(opciones, text="Menu").grid(row=1, column=0)
    tk.Button(opciones, text="Salir",width=10, command=lambda:cerrar_ventana(opciones, login)).grid(row=1, column=1)

    tk.Button(opciones, text="Articulos", height=3, width=30, command=lambda:ventana_productos(opciones)).grid(row=3, column=0, columnspan=2)
    tk.Button(opciones, text="Clientes", height=3, width=30, command=lambda: ventana_clientes(opciones)).grid(row=4, column=0, columnspan=2)
    tk.Button(opciones, text="Pedidos", height=3, width=30, command=lambda: ventana_facturar(opciones)).grid(row=5, column=0, columnspan=2)
    tk.Button(opciones, text="Consultas", height=3, width=30, command=lambda: ventana_consultas(opciones)).grid(row=6,
                                                                                                                column=0,
                                                                                                                columnspan=2)


def ventana_clientes(main):

    main.withdraw()

    clientesForm = tk.Toplevel()
    clientesForm.geometry("700x400")
    clientesForm.title("CLIENTES")

    nombre = tk.StringVar()
    saldo = tk.IntVar()
    cedula = tk.StringVar()
    limCredito = tk.StringVar()

    tk.Button(clientesForm, text="Volver", width=25, command=lambda: cerrar_ventana(clientesForm, main)).grid(row=0, column=5, pady=10, columnspan=3)
    tk.Label(clientesForm, text="Registro").grid(row=1, column=0, padx=30, pady=15)

    tk.Label(clientesForm, text="Cedula").grid(row=2, column=0)
    tk.Entry(clientesForm, textvariable=cedula).grid(row=2, column=1)

    tk.Label(clientesForm, text="Nombre").grid(row=3, column=0)
    tk.Entry(clientesForm, textvariable=nombre).grid(row=3, column=1)

    tk.Label(clientesForm, text="Saldo").grid(row=4, column=0)
    tk.Entry(clientesForm, textvariable=saldo, state="readonly").grid(row=4, column=1)

    tk.Label(clientesForm, text="Lim. Credito").grid(row=5, column=0)
    tk.Entry(clientesForm, textvariable=limCredito).grid(row=5, column=1)

    tk.Button(clientesForm, text="Registrar", width=25, command=lambda:registrar_cliente(cedula, nombre, saldo, limCredito)).grid(row=6, column=0, pady=15, columnspan=2)
    tk.Button(clientesForm, text="Limpiar", command=lambda: limpiar_formularioclientes(cedula, nombre, limCredito)).grid(row=6, column=2)

    cedulaDir = tk.StringVar()
    direccion = tk.StringVar()

    tk.Label(clientesForm, text="identificacion").grid(row=7, column=0)
    tk.Entry(clientesForm, textvariable=cedulaDir).grid(row=7, column=1)

    tk.Label(clientesForm, text="Direccion").grid(row=8, column=0)
    tk.Entry(clientesForm, textvariable=direccion).grid(row=8, column=1)

    tk.Button(clientesForm, text="Agregar", width=25,
              command=lambda: agregar_direccion(cedulaDir, direccion)).grid(row=9, column=0, pady=15,
                                                                                         columnspan=2)


    tk.Label().grid(row=0, column=3, padx=30)

    # -------------- CONSULTAS CLIENTES

    buscarCedula = tk.StringVar()
    lbConsultaunica = tk.StringVar()
    lbConsultaMultiple = tk.StringVar()

    tk.Label(clientesForm, text="Consultar").grid(row=1, column=4, padx=30, pady=15)

    singleQuery = "SELECT * FROM clientes WHERE idcliente ="
    tk.Label(clientesForm, text="Cedula").grid(row=2, column=4,padx=30)
    tk.Entry(clientesForm, textvariable=buscarCedula).grid(row=2, column=5)
    tk.Button(clientesForm, text="Buscar", command=lambda:mostrar_uno(singleQuery, buscarCedula, lbConsultaunica)).grid(row=2, column=6)

    tk.Label(clientesForm, text="Cedula - Nombre - Saldo - Lim saldo").grid(row=3, column=4, columnspan=3)
    tk.Label(clientesForm, textvariable=lbConsultaunica).grid(row=4, column=4)

    query = "SELECT * FROM clientes"
    tk.Label(clientesForm, text="Lista de los usuario registrados").grid(row=5, column=4, columnspan=2)
    tk.Button(clientesForm, text="Mostrar", command=lambda: mostrar_muchos(query, lbConsultaMultiple)).grid(row=5, column=6)
    tk.Label(clientesForm, textvariable=lbConsultaMultiple).grid(row=6, column=4)


def ventana_productos(main):

    main.withdraw()

    productosForm = tk.Toplevel()
    productosForm.geometry("700x250")
    productosForm.title("PRODUCTOS")

    id = tk.StringVar()
    nombre = tk.StringVar()
    costo = tk.StringVar()

    tk.Button(productosForm, text="Volver", width=25, command=lambda: cerrar_ventana(productosForm, main)).grid(row=0, column=5, pady=10, columnspan=3)
    tk.Label(productosForm, text="Registro producto").grid(row=1, column=0, pady=15, columnspan=2)

    tk.Label(productosForm, text="ID").grid(row=2, column=0, padx=40)
    tk.Entry(productosForm, textvariable=id).grid(row=2, column=1)

    tk.Label(productosForm, text="nombre").grid(row=3, column=0)
    tk.Entry(productosForm, textvariable=nombre).grid(row=3, column=1)

    tk.Label(productosForm, text="Costo").grid(row=4, column=0)
    tk.Entry(productosForm, textvariable=costo).grid(row=4, column=1)

    tk.Button(productosForm, text="Registrar", command=lambda:registrar_producto(id, nombre, costo)).grid(row=5, column=0, pady=15)
    tk.Button(productosForm, text="Limpiar", command=lambda: limpiar_formularioproductos(id, nombre, costo)).grid(row=5, column=1)

    tk.Label(productosForm, text="").grid(row=0, column=2, padx=30)


    # -------------- CONSULTAS PRODUCTOS ---------------

    buscarcodigo = tk.StringVar()
    lbConsultaunica = tk.StringVar()
    lbConsultaMultiple = tk.StringVar()

    tk.Label(productosForm, text="Consultar productos").grid(row=1, column=4, padx=30, pady=15, columnspan=2)

    singleQuery = "SELECT * FROM articulo WHERE idarticulo ="
    tk.Label(productosForm, text="Cedula").grid(row=2, column=4)
    tk.Entry(productosForm, textvariable=buscarcodigo).grid(row=2, column=5)
    tk.Button(productosForm, text="Buscar", command=lambda:mostrar_uno(singleQuery, buscarcodigo, lbConsultaunica)).grid(row=2, column=6)

    tk.Label(productosForm, text="Nombre - Apellido - Cedula - Telefono").grid(row=3, column=4, columnspan=3)
    tk.Label(productosForm, textvariable=lbConsultaunica).grid(row=4, column=4)

    query = "SELECT * FROM articulo"
    tk.Label(productosForm, text="Lista de los usuario registrados").grid(row=5, column=4, columnspan=2)
    tk.Button(productosForm, text="Mostrar", command=lambda: mostrar_muchos(query, lbConsultaMultiple)).grid(row=5, column=6)
    tk.Label(productosForm, textvariable=lbConsultaMultiple).grid(row=6, column=4)


def ventana_consultas(main):
    main.withdraw()

    consultasForm = tk.Toplevel()
    consultasForm.geometry("700x350")
    consultasForm.title("CONSULTAS")

    cedula1 = tk.StringVar()
    desde = tk.StringVar()
    hasta = tk.StringVar()

    consulta1 = tk.StringVar()

    tk.Button(consultasForm, text="Volver", width=25, command=lambda: cerrar_ventana(consultasForm, main)).grid(row=0, column=5, pady=10, columnspan=3)
    tk.Label(consultasForm, text="Consultar").grid(row=1, column=0, pady=15, columnspan=2)

    tk.Label(consultasForm, text="Consultar los pedidos del cliente").grid(row=2, column=0, columnspan=2, pady=15)

    tk.Label(consultasForm, text="Cedula").grid(row=3, column=0)
    tk.Entry(consultasForm, textvariable=cedula1).grid(row=3, column=1)

    tk.Label(consultasForm, text="Rango de fechas ejem: 2019-12-01").grid(row=4, column=0, columnspan=2, pady=15)

    tk.Label(consultasForm, text="Desde").grid(row=5, column=0)
    tk.Button(consultasForm, text="Calendario", command=lambda :cal_func(consultasForm, desde)).grid(row=5, column=1)

    tk.Label(consultasForm, text="Hasta").grid(row=6, column=0)
    tk.Button(consultasForm, text="Calendario", command=lambda :cal_func(consultasForm, hasta)).grid(row=6, column=1)

    tk.Label(consultasForm, textvariable=desde).grid(row=7, column=0)
    tk.Label(consultasForm, textvariable=hasta).grid(row=7, column=1)

    tk.Button(consultasForm, text="Consultar", command=lambda:pedidocli_rangofec(cedula1, desde, hasta, consulta1)).grid(row=8, column=0, pady=15)

    tk.Label(consultasForm, textvariable=consulta1).grid(row=9, column=0, columnspan=3)

    tk.Label(consultasForm, text="").grid(row=0, column=4, columnspan=2)



    idproducto2= tk.StringVar()
    labelConsulta2 = tk.StringVar()
    tk.Label(consultasForm, text="Consultar todos los clientes que han comprado un producto").grid(row=2, column =5, columnspan=4)
    tk.Label(consultasForm, text="Id producto").grid(row=3, column=5)
    tk.Entry(consultasForm, textvariable=idproducto2).grid(row=3, column=6)
    tk.Button(consultasForm, text="Consultar", command=lambda:cliente_compranproducto(idproducto2, labelConsulta2)).grid(row=3, column=7)

    tk.Label(consultasForm, textvariable=labelConsulta2).grid(row=4, column=5, columnspan=2)

    nomcli = tk.StringVar()
    idproducto3 = tk.StringVar()
    fecha3 = tk.StringVar()
    lbConsulta3 = tk.StringVar()
    tk.Label(consultasForm, text="Consultar pedido mas fabricante").grid(row=5, column=5, columnspan=2)
    tk.Label(consultasForm, text="Nombre cliente").grid(row=6, column=5)
    tk.Entry(consultasForm).grid(row=6, column=6)

    tk.Label(consultasForm, text="ID producto").grid(row=7, column=5)
    tk.Entry(consultasForm).grid(row=7, column=6)

    tk.Label(consultasForm, text="Fecha").grid(row=8, column=5)
    tk.Button(consultasForm, text="Calendario", command=lambda: cal_func(consultasForm, hasta)).grid(row=8, column=6)
    tk.Button(consultasForm, text="Consultar").grid(row=9, column=5)

    tk.Label(consultasForm).grid(row=10, column=5, columnspan=2)



#-----------------------------------------------------------------  LOGIN  ---------------------------------------------------------------------------

def dologin(user, passw, loginform):
    if user.get() != "" and passw.get() != "":
        query = "SELECT usuario from usuarios WHERE usuario = '"+user.get()+"'"
        if contarregistros(query):
            logear(user, passw, loginform)
        else:
            messagebox.showinfo("","Usuario o contraseña erroneos")
    else:
        messagebox.showinfo("", "Campos sin completar")


#----------------------------------------------------------- FUNCIONES VENTANAS ---------------------------------------------------------------------------

# --------------------- VENTANA CLIENTES ------------------------
def agregar_direccion(cedula, direccion):
    if cedula.get() != "" and direccion.get() != "":
        if solo_numeros(cedula.get()):
            query = "SELECT idcliente FROM clientes WHERE idcliente ='"+cedula.get()+"'"
            if contarregistros(query):
                add_address(cedula, direccion)
            else:
                messagebox.showwarning("Advertencia", "La cedula no existe en la base de datos")
        else:
            messagebox.showwarning("Advertencia","Verifique los datos \nCedula -> solo numeros")
    else:
        messagebox.showwarning("Advertencia", "Faltan campos por completar del formulario")


def registrar_cliente(cedula, nombre, saldo, limcredito):
    if cedula.get() != "" and nombre.get() != "" and limcredito.get() != "":
        if solo_numeros(cedula.get()) and solo_letras(nombre.get())  and solo_numeros(limcredito.get()):

            consulta = "SELECT idcliente FROM clientes WHERE idcliente = '"+cedula.get()+"'"
            if not contarregistros(consulta):
                insert_clients(cedula, nombre, saldo, limcredito)
                messagebox.showerror("Error", "Se ha registrado un nuevo cliente")
            else:
                messagebox.showerror("Error", "Codigo de cliente duplicado")
        else:
            messagebox.showwarning("Advertencia","Verifique los datos \nNombre -> solo letras\nCedula y Limite de credito -> solo numeros")
    else:
        messagebox.showwarning("Advertencia", "Faltan campor por completar del formulario")


# --------------------- VENTANA ARTICULOS ------------------------
def registrar_producto(id, nombre, costo):
    if id.get() != "" and nombre.get() != "" and costo.get() != "":
        if solo_letras(nombre.get()) and solo_numeros(costo.get()):

            consulta = "SELECT idarticulo FROM articulo WHERE idarticulo = '"+id.get()+"'"
            if not contarregistros(consulta):
                insert_product(id, nombre, costo)
            else:
                messagebox.showerror("Error", "Codigo de producto duplicado")
        else:
            messagebox.showwarning("Advertencia","Verifique los datos \nNombre -> solo letras\nID y costo -> solo numeros")
    else:
        messagebox.showwarning("Advertencia", "Faltan campor por completar del formulario")


# --------------------- VENTANA CONSULTAS ------------------------
def cal_func(consultasForm, var):
    def calval():
        #messagebox.showinfo("", cal.get_date())
        data = cal.get_date()
        datalist = data.split("/")
        fecha = "20"+datalist[2]+"-"+datalist[0]+"-"+datalist[1]
        messagebox.showinfo("",fecha)
        var.set(fecha)
        top.destroy()
    top = tk.Toplevel(consultasForm)
    cal = Calendar(top, font= "Arial 14", selectmode= "day", year=2019, month=5, day=17)
    cal.pack(fill = "both", expand=True)
    btn3 = tk.Button(top, text="Escojer fecha", command=calval)
    btn3.pack()


def pedidocli_rangofec(cedula1, desde, hasta, consulta1): #Consultar todos los pedidos de un cliente en un rango de fechas
    if cedula1.get() != "" and desde.get() != "" and hasta.get() != "":
        if solo_numeros(cedula1.get()):
            query = "SELECT clientes.nombre, direccion, fecha, total FROM pedido INNER JOIN clientes ON clientes.idcliente = pedido.idcliente WHERE pedido.idcliente = '"+cedula1.get()+"' AND fecha >= '"+desde.get()+"' AND fecha <= '"+hasta.get()+"'"
            mostrar_muchos(query, consulta1)
        else:
            messagebox.showerror("","La cedula solo puede contener numeros")
    else:
        messagebox.showwarning("Advertencia", "Faltan campos por completar para la consulta")


def cliente_compranproducto(idproducto2, var):
    if idproducto2.get() != "":
        query = "SELECT clientes.nombre FROM pedido INNER JOIN clientes ON clientes.idcliente = pedido.idcliente INNER JOIN detallepedido ON detallepedido.idpedido = pedido.idpedido WHERE detallepedido.idarticulo = '"+idproducto2.get()+"'"
        mostrar_muchos(query, var)
#----------------------------------------------------------- CIERRE DE VENTANAS ---------------------------------------------------------------------------

def cerrar_ventana(ventana_cerrar, ventana_abrir):
    ventana_cerrar.destroy()
    ventana_abrir.deiconify()


def limpiar_formularioclientes(cedula, nombre, limcredito):
    cedula.set("")
    nombre.set("")
    limcredito.set("")

def limpiar_formuladireccion(cedula, direccion):
    cedula.set("")
    direccion.set("")

def limpiar_formularioproductos(id, nombre, costo):
    id.set("")
    nombre.set("")
    costo.set("")

#-------------------------------------------------------------------------------- VALIDACIONES DE CAMPOS ---------------------------------------------------------------------------


def solo_letras(texto):
    respuesta = True
    letras = list(texto)
    for letter in letras:
        if letter.isdigit():
            respuesta = False

    return respuesta


def solo_numeros(texto):
    respuesta = True
    letras = list(texto)
    for letter in letras:
        if not letter.isdigit():
            respuesta = False

    return respuesta


#--------------------------------------------------------- MANEJO DE BASE DE DATOS ---------------------------------------------------------------------------


def conexion():
    con = mysql.connector.connect(host="localhost", user="root", database="almacen", password="")
    return con

def logear(user, passw, loginform):
    try:
        con = conexion()
        cursor = con.cursor()
        query = "SELECT usuario, passw from usuarios WHERE usuario = '"+user.get()+"'"
        cursor.execute(query)
        data = cursor.fetchall()

        if data[0][0] == user.get() and data[0][1] == passw.get():
            user.set("")
            passw.set("")
            ventana_opciones(loginform)
        else:
            messagebox.showinfo("", "contraseña erronea")
    except Exception as error:
        print(error)


def contarregistros(consulta):
    respuesta = False
    try:
        con = conexion()
        cursor = con.cursor()
        query = consulta
        cursor.execute(query)
        cursor.fetchall()

        if cursor.rowcount > 0:
            respuesta = True

        con.close()

    except Exception as error:
        print(error)

    return respuesta

# --------------------- VENTANA CLIENTES ------------------------
def insert_clients(cedula, nombre, saldo, limcredito):
    try:
        con = conexion()
        cursor = con.cursor()
        query = "INSERT INTO clientes VALUES (%s, %s, %s, %s)"
        args = (cedula.get(), nombre.get(), saldo.get(), int(limcredito.get()))
        cursor.execute(query, args)
        con.commit()
        messagebox("Se ha registrado un cliente nuevo")
        limpiar_formularioclientes(cedula, nombre, limcredito)

    except Exception as error:
        print(error)

def add_address(cedula, direccion):
    try:
        con = conexion()
        cursor = con.cursor()
        query = "INSERT INTO direcciones VALUES (%s, %s)"
        args = (cedula.get(), direccion.get())
        cursor.execute(query, args)
        con.commit()
        messagebox.showinfo("","Se ha agregado la direccion correctamente")
        limpiar_formuladireccion(cedula, direccion)

    except Exception as error:
        print(error)


# --------------------- VENTANA ARTICULOS ------------------------
def insert_product(id, nombre, costo):
    try:
        con = conexion()
        cursor = con.cursor()
        query = "INSERT INTO articulo VALUES (%s, %s, %s)"
        args = (id.get(), nombre.get(), int(costo.get()))
        cursor.execute(query, args)
        con.commit()
        messagebox.showinfo("","Se ha registrado un producto nuevo")
        limpiar_formularioproductos(id, nombre, costo)
    except Exception as error:
        print(error)


# --------------------- MOSTRAR REGISTROS ------------------------
def mostrar_muchos(consulta, label):
    con = conexion()
    cursor = con.cursor()
    query = consulta
    cursor.execute(query)

    rows = cursor.fetchall()  # Trae muchos registros
    res = ""

    for row in rows:
        for data in row:
            res = res+ str(data)+" - "
        res = res +"\n"

    label.set(res)

    con.close()

def mostrar_uno(consulta ,parametro, label):
    con = conexion()
    cursor = con.cursor()
    query = consulta+" '"+parametro.get()+"'"
    cursor.execute(query)

    rows = cursor.fetchall()  # Trae muchos registros
    res = ""

    for row in rows:
        for data in row:
            res = res + str(data) + " - "

    label.set(res)

    con.close()
#--------------------------------------------------------- INICIO DE LA APP ---------------------------------------------------------------------------

ventana_login()