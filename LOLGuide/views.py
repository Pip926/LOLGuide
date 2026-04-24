from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Champion, Item, Region, JungleMonsters
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm


def auth_view(request):
    # Инициализируем формы
    login_form = AuthenticationForm()
    register_form = RegisterForm()

    if request.method == 'POST':
        if 'login_submit' in request.POST:
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                auth_login(request, user) 
                return redirect('index')
            # Если login_form невалидна, она сама сохранит ошибки внутри себя

        elif 'register_submit' in request.POST:
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save() # Теперь это сработает и сохранит в БД
                auth_login(request, user)
                return redirect('index')
            # Если здесь ошибка (пароль слабый или юзер есть), 
            # register_form теперь содержит список этих ошибок.

    return render(request, 'LOLGuide/auth.html', {
        'login_form': login_form,
        'register_form': register_form
    })

def index(request):
    return render(request, 'LOLGuide/index.html')

def champions_list(request):
    champions = Champion.objects.all()
    return render(request, 'LOLGuide/champions_list.html', {'champions' : champions})

def champion_detail(request, pk):
    champion = get_object_or_404(Champion, pk=pk)
    return render(request, 'LOLGuide/champion_detail.html', {'champion' : champion})

def regions_list(request):
    regions = Region.objects.all()
    return render(request, 'LOLGuide/regions_list.html', {'regions': regions})

def region_detail(request, pk):
    region = get_object_or_404(Region, pk=pk)
    return render(request, 'LOLGuide/region_detail.html', {'region': region})

def items_list(request):
    items = Item.objects.all()
    return render(request, 'LOLGuide/items_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'LOLGuide/item_detail.html', {'item': item})

def monsters_hub(request):
    return render(request, 'LOLGuide/monsters_hub.html')

def common_monsters_list(request):
    monsters = JungleMonsters.objects.filter(category='common')
    return render(request, 'LOLGuide/common_monsters_list.html', {'monsters': monsters})

def boss_monsters_list(request):
    bosses = JungleMonsters.objects.filter(category='boss')
    return render(request, 'LOLGuide/boss_monsters_list.html', {'bosses': bosses})

def boss_detail(request, pk):
    boss = get_object_or_404(JungleMonsters, pk=pk, category='boss')
    return render(request, 'LOLGuide/boss_detail.html', {'boss': boss})

def monster_detail(request, pk):
    monster = get_object_or_404(JungleMonsters, pk=pk, category='common')
    return render(request, 'LOLGuide/monster_detail.html', {'monster': monster})
