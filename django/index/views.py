from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto, Categoria, Genero, Persona

# Create your views here.

# Pagina principal del proyecto
def index(request):
    lista_producto = Producto.objects.all()
    context = {"producto":lista_producto}
    return render(request,'index/index.html',context)

# Menu
@login_required
def menu(request):
    context = {}
    return render(request,'index/menu.html',context)

# Tabla "Gestor" 
@login_required
def gestor(request):
    lista_producto = Producto.objects.all() 
    context = {"producto":lista_producto}
    return render(request,'index/gestor.html',context)

# CRUD Producto y Categoria
def listaProducto(request):
    lista_producto = Producto.objects.raw('SELECT * FROM producto') 
    context = {"producto":lista_producto}
    return render(request,'index/gestor.html',context)

def listaCategoria(request,):
    lista_categoria = Categoria.objects.all() 
    context = {"categoria":lista_categoria}
    return render(request,'index/categoria.html',context)

@login_required
def agregarProducto(request):
    if request.method != "POST":
        lista_categoria = Categoria.objects.all() 
        context = {"categoria":lista_categoria}
        return render(request,'index/gestoradd.html',context)
    else:
        codigo = request.POST['codigo']
        categoria = request.POST['categoria']
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        imagen = request.POST['imagen']
        referencia = request.POST['referencia']
        color = request.POST['color']
        cantidad = request.POST['cantidad']
        origen = request.POST['origen']
        serie = request.POST['serie']

        objCategoria = Categoria.objects.get(id_categoria = categoria)

        objProducto = Producto.objects.create(
            codigo_producto = codigo,
            id_categoria = objCategoria,
            nombre = nombre,
            descripcion = descripcion,
            imagen = imagen,
            referencia = referencia,
            color = color,
            cantidad = cantidad,
            origen = origen,
            serie = serie
        )

        objProducto.save() #insert en la BD
        lista_categoria = Categoria.objects.all()
        context = {"mensaje":"Se agregó producto", "categoria":lista_categoria}
        return render(request,'index/gestoradd.html',context)

def eliminarProducto(request,pk):
    try:
        producto = Producto.objects.get(codigo_producto=pk)
        producto.delete() #delte en la BD
        mensaje = "El producto se eliminó"
        lista_producto = Producto.objects.all() 
        context = {"producto":lista_producto, "mensaje":mensaje}
        return render(request,'index/gestor.html',context)
    except:
        mensaje = "El producto NO se eliminó"
        lista_producto = producto.objects.all() 
        context = {"producto":lista_producto, "mensaje":mensaje}
        return render(request,'index/gestor.html',context)
    
def buscarProducto(request,pk):
    if pk != "":
        producto = Producto.objects.get(codigo_producto=pk)
        lista_categoria = Categoria.objects.all()
        context = {"producto":producto, "categoria":lista_categoria}
        if producto:
            return render(request,'index/gestoredit.html',context)
        else:
           context = {"mensaje":"No se encontró el producto"} 
           return render(request,'index/gestor.html',context)
    
def actualizarProducto(request):
    if request.method == "POST":
        codigo = request.POST['codigo']
        categoria = request.POST['categoria']
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        imagen = request.POST['imagen']
        referencia = request.POST['referencia']
        color = request.POST['color']
        cantidad = request.POST['cantidad']
        origen = request.POST['origen']
        serie = request.POST['serie']


        objCategoria = Categoria.objects.get(id_categoria = categoria)

        objProducto = Producto()
        objProducto.codigo_producto = codigo
        objProducto.id_categoria = objCategoria
        objProducto.nombre = nombre
        objProducto.descripcion = descripcion
        objProducto.imagen = imagen
        objProducto.referencia = referencia
        objProducto.color = color
        objProducto.cantidad = cantidad
        objProducto.origen = origen
        objProducto.serie = serie
        
        objProducto.save() 
        lista_categoria = Categoria.objects.all()
        context = {"mensaje":"Se modificó Producto", "categoria":lista_categoria,"producto":objProducto}
        return render(request,'index/gestoredit.html',context)
    else:
        lista_producto = Producto.objects.all()
        context = {"producto":lista_producto}
        return render(request,'index/gestor.html',context)
    
# CRUD Usuario y Genero
@login_required
def gestorPersona(request):
    lista_persona = Persona.objects.all() 
    context = {"persona":lista_persona}
    return render(request,'index/gestorusuario.html',context)

def listaPersona(request):
    lista_persona = Persona.objects.raw('SELECT * FROM persona') 
    context = {"persona":lista_persona}
    return render(request,'index/gestorusuario.html',context)

def listaGenero(request,):
    lista_genero = Genero.objects.all() 
    context = {"genero":lista_genero}
    return render(request,'index/genero.html',context)

@login_required
def agregarPersona(request):
    if request.method != "POST":
        lista_genero = Genero.objects.all() 
        context = {"genero":lista_genero}
        return render(request,'index/gestorusuarioadd.html',context)
    else:
        codigo = request.POST['codigo']
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        genero = request.POST['genero']
        username = request.POST['username']
        email = request.POST['email']
        telefono = request.POST['telefono']
        password = request.POST['password']

        objGenero = Genero.objects.get(id_genero = genero)

        objPersona = Persona.objects.create(
            codigo_persona = codigo,
            nombres = nombres,
            apellidos = apellidos,
            id_genero = objGenero,
            nombre_usuario = username,
            email = email,
            telefono = telefono,
            contrasena = password
        )

        objPersona.save() #insert en la BD
        lista_genero = Genero.objects.all()
        context = {"mensaje":"Se agregó Persona", "genero":lista_genero}
        return render(request,'index/gestorusuarioadd.html',context)
    
def eliminarPersona(request,pk):
    try:
        persona = Persona.objects.get(codigo_persona=pk)
        persona.delete() #delte en la BD
        mensaje = "La persona se eliminó"
        lista_persona = Persona.objects.all() 
        context = {"persona":lista_persona, "mensaje":mensaje}
        return render(request,'index/gestorusuario.html',context)
    except:
        mensaje = "La persona NO se eliminó"
        persona = Persona.objects.all() 
        context = {"persona":lista_persona, "mensaje":mensaje}
        return render(request,'index/gestorusuario.html',context)
    
def buscarPersona(request,pk):
    if pk != "":
        persona = Persona.objects.get(codigo_persona=pk)
        lista_genero = Genero.objects.all()
        context = {"persona":persona, "genero":lista_genero}
        if persona:
            return render(request,'index/gestorusuarioedit.html',context)
        else:
           context = {"mensaje":"No se encontró la persona"} 
           return render(request,'index/gestorusuario.html',context)
        
def actualizarPersona(request):
    if request.method == "POST":
        codigo = request.POST['codigo']
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        genero = request.POST['genero']
        username = request.POST['username']
        email = request.POST['email']
        telefono = request.POST['telefono']
        password = request.POST['password']

        objGenero = Genero.objects.get(id_genero = genero)

        objPersona = Persona()
        objPersona.codigo_persona = codigo
        objPersona.nombres = nombres
        objPersona.apellidos = apellidos
        objPersona.id_genero = objGenero
        objPersona.nombre_usuario = username
        objPersona.email = email
        objPersona.telefono = telefono
        objPersona.contrasena = password
        
        objPersona.save() 
        lista_genero = Genero.objects.all()
        context = {"mensaje":"Se modificó Persona", "genero":lista_genero,"persona":objPersona}
        return render(request,'index/gestorusuarioedit.html',context)
    else:
        lista_persona = Persona.objects.all()
        context = {"persona":lista_persona}
        return render(request,'index/gestorusuario.html',context)