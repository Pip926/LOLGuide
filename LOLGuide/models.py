from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Профиль для {self.user.username}"

class Region(models.Model):
    REGION_CHOICES = [
        ('Noxus', "Ноксус"),
        ('Demacia', "Демасия"),
        ('Freljord', "Фрельйорд"),
        ('Shurima', "Шурима"),
        ('Ionia', "Иония"),
        ('Targon', "Таргон"),
        ('Ixtal', "Ишталь"),
        ('Piltover', "Пилтовер"),
        ('Zaun', "Заун"),
        ('Bilgewater', "Билджвотер"),
        ('Shadow Isles', "Сумрачные острова"),
        ('The Void', "Бездна"),
        ('Bandle City', "Бандл Сити"),
    ]

    name = models.CharField(
        "Название",
        max_length=50,
        choices=REGION_CHOICES,
        unique=True
    )
    tagline = models.CharField(
        "Слоган",
        max_length=200,
        help_text="Например: Сила превыше всего!"
    )
    description = models.TextField("Лор региона")
    emblem = models.ImageField(
        "Герб",
        upload_to='regions/emblems/'
    )
    background = models.ImageField(
        "Фон страницы",
        upload_to='regions/backgrounds/'
    )
    color = models.CharField(
        "Цвет региона",
        max_length=7,
        default="#C8AA6E",
        help_text="Например: #C8AA6E"
    )

    def __str__(self):
        return self.get_name_display()
    
    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Item(models.Model):
    name = models.CharField(
        "Название артефакта", 
        max_length=100
    )
    image = models.ImageField(
        "Изображение", 
        upload_to='items/'
    )
    origin_story = models.TextField(
        "История артефакта", 
        help_text="Откуда взялся этот предмет в мире Рунтерры?"
    )
    stat_display = models.TextField(
        "Характеристики",
        max_length=200,
        help_text="Например: +65 Силы атаки, +20% Скорости атаки"
    )
    passive = models.TextField(
        "Пассивные уменя",
        help_text="Какие пассивные умения есть у этого предмета?",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Артефакт"
        verbose_name_plural = "Артефакты"



class Champion(models.Model):
    ROLE_CHOICES = [
        ('assasin', 'Уйбийца'),
        ('fighter', 'Воин'),
        ('mage', 'Маг'),
        ('marksman', 'Стрелок'),
        ('support', 'Поддержка'),
        ('tank', 'Танк'),

    ]

    FIGHT_TYPE_CHOICES = [
        ('melee', "Ближний бой"),
        ('ranged', "Дальний бой"),

    ]
    
    name = models.CharField(
        "Имя чемпиона", 
        max_length=100, 
        unique=True
    )
    title = models.CharField(
        "Титул", 
        max_length=200
    )
    region = models.ForeignKey(
        Region,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='champions',
        verbose_name="Регион"
    )
    lore = models.TextField("История(Лор)")
    role = models.CharField(
        "Основная роль",
        max_length=20,
        choices=ROLE_CHOICES,
        default='fighter'
    )
    secondary_role = models.CharField(
        "Дополнительная роль",
        max_length=20,
        choices=ROLE_CHOICES,
        blank=True,
        null=True
    )

    fight_type = models.CharField(
        "Тип боя",
        max_length=15,
        choices=FIGHT_TYPE_CHOICES,
        default='melee'
    )

    play_top = models.BooleanField("Топ", default=False)
    play_jungle = models.BooleanField("Лес", default=False)
    play_mid = models.BooleanField("Мид", default=False)
    play_bot = models.BooleanField("Бот", default=False)
    play_support = models.BooleanField("Саппорт", default=False)

    hp = models.PositiveIntegerField("Здоровье")
    mana = models.PositiveIntegerField(
        "Мана / Ресурс", 
        null=True, 
        blank=True
    )
    attack_damage = models.PositiveIntegerField("Сила атаки")
    armour = models.PositiveIntegerField("Броня")
    magic_resist = models.PositiveIntegerField("Сопротивление магии")
    attack_range = models.PositiveIntegerField("Дальность атак", default=125)
    movement_speed = models.PositiveIntegerField("Скорость передвижения", default=330)

    image_main = models.ImageField(
        "Главный арт", 
        upload_to='champions/splashes/'
    )
    image_icon = models.ImageField(
        "Иконка", 
        upload_to='champions/icons/'
    )

    item_slot_1 = models.ForeignKey(
        'Item',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='slot1_heroes',
        verbose_name="Первый лучший предмет"
    )
    item_slot_2 = models.ForeignKey(
        'Item',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='slot2_heroes',
        verbose_name="Второй лучший предмет"
    )
    item_slot_3 = models.ForeignKey(
        'Item',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='slot3_heroes',
        verbose_name="Третий лучший предмет"
    )
    items_reasoning = models.TextField(
        "Почему это лучшие предметы для него?", 
        blank=True, 
        default=''
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Чемпион"
        verbose_name_plural = "Чемпионы"


class Ability(models.Model):
    SLOT_CHOICES = [
        ("P", "Пассивное"),
        ("Q", "Q"),
        ("W", "W"),
        ("E", "E"),
        ("R", "Ульта"),

    ]

    champion = models.ForeignKey(
        Champion, 
        on_delete=models.CASCADE,
        related_name='abilities',
        verbose_name="Чемпион"
    )


    slot = models.CharField(
        "Клавиша", 
        max_length=1, 
        choices=SLOT_CHOICES
    )
    name = models.CharField(
        "Название умения", 
        max_length=100
    )
    description = models.TextField("Описание")
    image = models.ImageField(
        "Иконка умения", 
        upload_to='champions/abilities/'
    )

    def __str__(self):
        return f"{self.champion.name} - {self.slot} : {self.name}"
    
    
    class Meta:
        verbose_name = "Умение"
        verbose_name_plural = "Умения"


class JungleMonsters(models.Model):
    CATEGORY_CHOICES = [
        ('common', 'Обычное существо'),
        ('boss', 'Босс'),
    ]

    name = models.CharField(
        "Имя",
        max_length=100
    )
    category = models.CharField(
        "Категория",
        max_length=10,
        choices=CATEGORY_CHOICES
    )
    description = models.TextField("Описание/Лор")
    image = models.ImageField(
        "Изображение",
        upload_to='monsters/'
    )

    # Характеристики
    health = models.IntegerField(
        "Здоровье",
        default=0
    )
    gold_reward = models.IntegerField(
        "Награда(золото)",
        default=0
    )
    buff_description = models.TextField(
        "Описание баффа",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Лесное существо"
        verbose_name_plural = "Лесные существа"


