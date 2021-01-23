from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Pet
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy


def showcase(request):
    pet = Pet.objects.filter(active=True)
    return render(request, 'sos_pet/showcase.html', {'pet':pet})

def showdetail(request, id):
    pet = Pet.objects.get(active=True, id=id)
    return render(request, 'sos_pet/showdetail.html', {'pet':pet})


@login_required(login_url='/login/')
def set_pet(request):
    petname = request.POST.get('petname')
    name = request.POST.get('name')
    zone = request.POST.get('zone')
    tipo = request.POST.get('tipo')
    sexo = request.POST.get('sexo')
    city = request.POST.get('city')
    castrado = request.POST.get('castrado')
    temperamento = request.POST.get('temperamento')
    vacinado = request.POST.get('vacinado')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    description = request.POST.get('description')
    file = request.FILES.get('file')
    file2 = request.FILES.get('file2')
    file3 = request.FILES.get('file3')
    user = request.user
    pet_id = request.POST.get('pet_id')
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if user == pet.user:
            pet.petname = petname
            pet.name = name
            pet.phone = phone
            pet.city = city
            pet.zone = zone
            pet.tipo = tipo
            pet.sexo = sexo
            pet.castrado = castrado
            pet.temperamento = temperamento
            pet.vacinado = vacinado
            pet.description = description 
            if file:
                pet.photo = file
            pet.save()
                                     
    else:
        pet = Pet.objects.create( temperamento=temperamento, castrado=castrado,
        zone=zone, name=name, petname=petname, sexo=sexo, tipo=tipo, vacinado=vacinado, 
        phone=phone, city=city, description=description, user=user, photo=file)
    url = '/pet/detail/{}/'.format(pet.id)
    return redirect(url)

@login_required(login_url='/login/')
def delete_pet(request, id):
    pet = Pet.objects.get(id=id)
    if pet.user == request.user:
        pet.delete()
    return redirect('/pet/all/')


@login_required(login_url='/login/')
def register_pet(request):
    pet_id = request.GET.get('id')
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        if pet.user == request.user:
            return render(request, 'sos_pet/register-pet.html', {'pet':pet})
    return render(request, 'sos_pet/register-pet.html')


@login_required(login_url='/login/')
def list_all_pets(request):
    pet = Pet.objects.filter(active=True)
    return render(request, 'sos_pet/list.html', {'pet':pet})

@login_required(login_url='/login/')
def list_user_pets(request):
    pet = Pet.objects.filter(active=True, user=request.user)
    return render(request, 'sos_pet/list.html', {'pet':pet})

@login_required(login_url='/login/')
def list_dog_pets(request):
    pet = Pet.objects.filter( tipo='Cachorro')
    return render(request, 'sos_pet/list.html', {'pet':pet})

@login_required(login_url='/login/')
def list_cat_pets(request):
    pet = Pet.objects.filter( tipo='Gato')
    return render(request, 'sos_pet/list.html', {'pet':pet})


@login_required(login_url='/login/')
def pet_detail(request, id):
    pet = Pet.objects.get(active=True, id=id)
    return render(request, 'sos_pet/pet.html', {'pet':pet})

def logout_user(request):
    logout(request)
    return redirect('/login/')

def login_user(request):
    return render(request, 'sos_pet/login.html')
    
@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/pet/all/')
        else:
            messages.error(request, 'Usuário/Senha inválidos. Favor tentar novamente.')
    return redirect('/login/')     


