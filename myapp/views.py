from django.shortcuts import render, get_object_or_404, redirect
from .models import producto_notebook, producto_pc, producto_celulare, transicione
from .forms import CustomUserCreationForm, ProductoForm, ProductoForm2, ProductoForm3
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse


def home(request):
    productos_notebooks = producto_notebook.objects.all()
    productos_pcs = producto_pc.objects.all()
    productos_celulares = producto_celulare.objects.all()
    transiciones = transicione.objects.all()
    data = {
        'productos_notebooks': productos_notebooks,
        'productos_pcs': productos_pcs,
        'productos_celulares': productos_celulares,
        'transiciones': transiciones
    }
    return render(request, 'home.html', data)

def Notebook(request):
    productos_notebooks = producto_notebook.objects.all()
    transiciones = transicione.objects.all()
    data1 = {
        'productos_notebooks': productos_notebooks,
        'transiciones': transiciones
    }
    return render(request,'Notebook.html', data1)

def pc(request):
    productos_pcs = producto_pc.objects.all()
    transiciones = transicione.objects.all()
    
    data2 = {
        'productos_pcs': productos_pcs,
        'transiciones': transiciones
    }
    return render(request,'PC.html', data2)

def modal(request):
    return render(request,'modal.html')

def formulario(request):
    return render(request,'formulario.html')

def Celulares(request):
    productos_celulares = producto_celulare.objects.all()
    transiciones = transicione.objects.all()
    data3 = {
        'productos_celulares': productos_celulares,
        'transiciones': transiciones
    }
    return render(request,'Celulares.html', data3)

@login_required
def agregar(request):
    data = {}

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            producto = formulario.save(commit=False)
            clase = formulario.cleaned_data['clase']
            
            if clase == 'pc':
                producto_pc.objects.create(
                    nombre=producto.nombre,
                    precio=producto.precio,
                    descripcion=producto.descripcion,
                    marca=producto.marca,
                    imagen=producto.imagen
                )
            elif clase == 'notebook':
                producto_notebook.objects.create(
                    nombre=producto.nombre,
                    precio=producto.precio,
                    descripcion=producto.descripcion,
                    marca=producto.marca,
                    imagen=producto.imagen
                )
            elif clase == 'celular':
                producto_celulare.objects.create(
                    nombre=producto.nombre,
                    precio=producto.precio,
                    descripcion=producto.descripcion,
                    marca=producto.marca,
                    imagen=producto.imagen
                )
            
            data["mensaje"] = "Guardado correctamente"
        else:
            data['form'] = formulario
    else:
        data['form'] = ProductoForm()

    return render(request, 'producto/agregar.html', data)


@login_required
@permission_required('myapp.view_productos_pcs')
@permission_required('myapp.view_productos_notebooks')
@permission_required('myapp.view_productos_celulares')
def listar(request):
    productos_notebooks = producto_notebook.objects.all()
    productos_pcs = producto_pc.objects.all()
    productos_celulares = producto_celulare.objects.all()

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos_pcs, 5)
        productos_pcs = paginator.page(page)
        paginator = Paginator(productos_pcs, 5)
        productos_pcs = paginator.page(page)
        paginator = Paginator(productos_celulares, 5)
        productos_celulares = paginator.page(page)
        paginator = Paginator(productos_notebooks, 5)
        productos_notebooks = paginator.page(page)
    except:
        raise Http404

    data5 = {
        'entity2': productos_notebooks,
        'entity': productos_pcs,
        'paginator': paginator,
        'entity3': productos_celulares,
    }

    return render(request, 'producto/listar.html', data5)



@login_required
@permission_required('myapp.change_productos_pcs')
def modificar_pc(request, id):
    producto = get_object_or_404(producto_pc, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'producto/modificar_pc.html', {'form': form, 'producto': producto})


@login_required
@permission_required('myapp.change_productos_notebooks')
def modificar_notebook(request, id):
    producto = get_object_or_404(producto_notebook, id=id)
    if request.method == 'POST':
        form = ProductoForm3(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ProductoForm3(instance=producto)

    return render(request, 'producto/modificar_notebook.html', {'form': form, 'producto': producto})


@login_required
@permission_required('myapp.change_productos_celulares')
def modificar_celular(request, id):
    producto = get_object_or_404(producto_celulare, id=id)
    if request.method == 'POST':
        form = ProductoForm2(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ProductoForm2(instance=producto)

    return render(request, 'producto/modificar_celular.html', {'form': form, 'producto': producto})


@login_required
def eliminar_pc(request, id):
    producto = get_object_or_404(producto_pc, id=id)
    producto.delete()
    return redirect('listar')

@login_required
def eliminar_notebook(request, id):
    producto = get_object_or_404(producto_notebook, id=id)
    producto.delete()
    return redirect('listar')

@login_required
def eliminar_celular(request, id):
    producto = get_object_or_404(producto_celulare, id=id)
    producto.delete()
    return redirect('listar')


def registrar(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            # Autenticar y iniciar sesión automáticamente después del registro
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        data["form"] = formulario

    return render(request, 'registration/registrar.html', data)

def comprar(request):
    return render(request,'comprar.html')


def notebook_detail(request, notebook_id):
    # Lógica para obtener los detalles del producto notebook con el ID proporcionado
    notebook = producto_notebook.objects.get(id=notebook_id)
    return render(request, 'notebook_detail.html', {'notebook': notebook})

def pc_detail(request, pc_id):
    # Lógica para obtener los detalles del producto PC con el ID proporcionado
    pc = producto_pc.objects.get(id=pc_id)
    return render(request, 'pc_detail.html', {'pc': pc})

def celular_detail(request, celular_id):
    # Lógica para obtener los detalles del producto celular con el ID proporcionado
    celular = producto_celulare.objects.get(id=celular_id)
    return render(request, 'celular_detail.html', {'celular': celular})

def agregar_al_carrito(request, producto_id, tipo_producto):
    if tipo_producto == 'notebook':
        producto = get_object_or_404(producto_notebook, id=producto_id)
    elif tipo_producto == 'pc':
        producto = get_object_or_404(producto_pc, id=producto_id)
    elif tipo_producto == 'celular':
        producto = get_object_or_404(producto_celulare, id=producto_id)
    else:
        return redirect('ver_carrito')
    
    if request.session.get('carrito'):
        carrito = request.session['carrito']
    else:
        carrito = []
    
    carrito.append(producto)
    request.session['carrito'] = carrito
    request.session.save()  # Guardar la sesión

    # Preparar los datos para la respuesta JSON
    producto_data = {
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio': producto.precio,
        # Agrega más campos si son necesarios
    }

    return JsonResponse(producto_data)

def eliminar_del_carrito(request, producto_id):
    if request.session.get('carrito'):
        carrito = request.session['carrito']
        producto = get_object_or_404(
            [producto_notebook, producto_pc, producto_celulare], id=producto_id
        )
        carrito.remove(producto)
        request.session['carrito'] = carrito
    
    return redirect('ver_carrito')

def sumar_cantidad(request, producto_id):
    if request.session.get('carrito'):
        carrito = request.session['carrito']
        producto = get_object_or_404(
            [producto_notebook, producto_pc, producto_celulare], id=producto_id
        )
        producto.cantidad += 1
        request.session['carrito'] = carrito
        producto.save()  # Guardar los cambios en el producto
    
    return redirect('ver_carrito')

def restar_cantidad(request, producto_id):
    if request.session.get('carrito'):
        carrito = request.session['carrito']
        producto = get_object_or_404(
            [producto_notebook, producto_pc, producto_celulare], id=producto_id
        )
        if producto.cantidad > 1:
            producto.cantidad -= 1
            request.session['carrito'] = carrito
            producto.save()  # Guardar los cambios en el producto
    
    return redirect('ver_carrito')

def vaciar_carrito(request):
    if request.session.get('carrito'):
        del request.session['carrito']
    
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = request.session.get('carrito', [])
    total = sum(producto.precio * producto.cantidad for producto in carrito)
    
    return render(request, 'ver_carrito.html', {'carrito': carrito, 'total': total})

def listar_notebooks(request):
    productos_notebooks = producto_notebook.objects.all()
    return render(request, 'producto/listar.html', {'entity': productos_notebooks})

def listar_pcs(request):
    productos_pcs = producto_pc.objects.all()
    return render(request, 'producto/listar.html', {'entity': productos_pcs})

def listar_celulares(request):
    productos_celulares = producto_celulare.objects.all()
    return render(request, 'producto/listar.html', {'entity': productos_celulares})



