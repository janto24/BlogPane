from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from PaneApp.models import Post, Oportunidades
from PaneApp.forms import NuevoPost, AgregarDesc
from users.models import Avatar



# Create your views here.

def inicio(request):

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    context = {
        'avatar': avatar,
        'title': 'Inicio',
        'message': 'PaneAPP',
        'subtitle': '¿Planificando donde vas a comer? '
                'Lee las recomendaciones sobre donde comer al lugar al que vayas',
        }
    return render(request, 'PaneApp/index.html', context)


def oportunidades(request):
    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''
    
    # Oportunidades  
    oportunidades = Oportunidades.objects.order_by('-valid_through')
    
    # Buscar descuentos por categoria
    category = request.GET.get('categoria')

    if category:
        oportunidades = Oportunidades.objects.filter(categoria__icontains=category)
        context = {
            'title': 'oportunidades',
            'category': category,
            'search': 'Buscar por categoría (ej: "Alojamiento")',
            'oportunidades': oportunidades,
            'avatar': avatar,
        }
        return render(request, 'PaneApp/desc.html', context)

    else:
        # Listar todas las promociones
        context = {
            'oportunidades': oportunidades,
            'title': 'Desc',
            'subtitle': '¡Mira los descuentos que hay para en la ciudad',
            'search': 'Buscar por categoría',
            'avatar': avatar,
        }
        return render(request, 'PaneApp/desc.html', context)


def posts(request):
    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    posts = Post.objects.order_by('-date_added')

    # Busca rest por ciudades
    city = request.GET.get('city')
    if city:
        posts = Post.objects.filter(city__icontains=city)
        context = {
            'title': 'Posts',
            'city': city,
            'search': 'Buscar por ciudad',
            'posts': posts,
            'avatar': avatar,
        }
        return render(request, 'PaneApp/posts.html', context)
    
    else:
        # Listar todos los posts
        context = {
            'posts': posts,
            'title': 'Posts',
            'subtitle': '¡El listado completo de nuestros posts!',
            'search': 'Buscar por ciudad',
            'avatar': avatar,
        }
        return render(request, 'PaneApp/posts.html', context)


@login_required
def agregar_desc(request):

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    if request.method != 'POST':
        # No data submited. Paso formulario vacio
        form = AgregarDesc()

    else:
        # Data submitted. Paso formulario con datos ingresados por POST
        form = AgregarDesc(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PaneApp:Descs')

    context = {
        'form': form,
        'title': 'Agregar Desc',
        'avatar': avatar,
    }
    return render(request, 'PaneApp/new_desc.html', context)


@login_required
def agregar_post(request):
  

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    if request.method != 'POST':
        # No data submited. Paso formulario vacio
        form = NuevoPost()
    
    else:
        # Data submitted. Paso formulario con datos ingresados por POST
        form = NuevoPost(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
           
            return redirect('PaneApp:Posts')

    context = {
        'form': form, 
        'title': 'Nuevo Post',
        'avatar': avatar,
    }
    return render(request, 'PaneApp/new_post.html', context)


@login_required
def edit_post(request, post_id):

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    # Post que se va a editar
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        # No data submitted. Formulario ya poblado con los datos a editar (antes de enviar/guardar)
        form = NuevoPost(instance=post)

    else:
        # Data submitted. Formulario para guardar con los datos enviados por POST
        form = NuevoPost(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('PaneApp:Posts')

    context = {
        'title': 'Edit',
        'subtitle': post.resto,
        'form': form,
        'avatar': avatar,
    }
    return render(request, 'PaneApp/edit_post.html', context)
    

@login_required
def edit_desc(request, desc_id):
    """Edit an existing promo."""

    # el usuario tiene avatar?
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    # Descuentos a editar
    oportunidades = Oportunidades.objects.get(id=desc_id)

    if request.method != 'POST':
        # No data submitted. Formulario ya poblado con datos a editar (antes de enviar/guardar)
        form = AgregarDesc(instance=oportunidades)
    
    else:
        # Data submitted. Formulario para guardar con los datos enviados por POST
        form = AgregarDesc(instance=oportunidades, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('PaneApp:Oportunidades')

    context = {
        'title': 'Edit',
        'subtitle': oportunidades.descripcion,
        'form': form,
        'avatar': avatar,
    }
    return render(request, 'PaneApp/edit_desc.html', context)


@login_required
def post_detail(request, post_id):
    """Display full post."""
    
    # Post que se va a mostrar
    post = Post.objects.get(id=post_id)

    # Para buscar si el usuario tiene avatar
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''
    
    context = {
        'title': 'Detail',
        'subtitle': post.title,
        'avatar': avatar,
        'post': post
    }
    return render(request, 'PaneApp/post_detail.html', context)


# Class Based Views

class DeleteDesc(LoginRequiredMixin, DeleteView):
    model = oportunidades
    success_url = '/desc/'


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/pages/'


def about(request):

    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = ''

    context = {
        'avatar': avatar,
        'title': 'About',
        'message': 'Bienvenidos a City Travel',
        'subtitle': 'About'
        }
    return render(request, 'PaneApp/about.html', context)