from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=12, verbose_name='Телефон', blank=True, null=True)
    friends = models.ManyToManyField('self', through='friend')
    kind_activity = models.CharField(max_length=200, verbose_name='Вид деятельности', blank=True)
    open_for_contact = models.BooleanField('Открыт для контактов', default=False)
    projects = models.TextField('Проекты', blank=True)
    telegram_id = models.IntegerField('Телеграм ID')

    def __str__(self):
        return f'{self.name}, phone: {self.phone}'


class Friend(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='me')
    friend = models.ForeignKey(Guest, on_delete=models.CASCADE, related_name='friend')

    def __str__(self):
        return f'{self.friend}'


class Event(models.Model):
    topic = models.CharField(max_length=200, verbose_name='Тема')
    date = models.DateField('Дата')
    guests = models.ManyToManyField(Guest, through='EventGuests')

    def __str__(self):
        return self.topic


class EventGuests(models.Model):
    event = models.ForeignKey(Event, related_name='events', on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, related_name='events', on_delete=models.CASCADE)


class Schedule(models.Model):
    topic = models.CharField(max_length=200, verbose_name='Тема')
    date_start = models.DateTimeField('Дата')
    date_end = models.DateTimeField('Дата')
    speaker = models.ForeignKey(Guest, verbose_name='Спикер', on_delete=models.PROTECT, related_name='schedules')
    active = models.BooleanField(default=False)
    event = models.ForeignKey(Event, verbose_name='Событие', on_delete=models.CASCADE, related_name='schedules')

    def __str__(self):
        return self.topic


class Question(models.Model):
    question = models.TextField('Вопрос')
    schedule = models.ForeignKey(Schedule, verbose_name='Расписание', on_delete=models.SET_NULL, null=True, related_name='questions')
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE, null=True, related_name='questions')

    def __str__(self):
        return self.question[100]


class Donation(models.Model):
    amount = models.IntegerField('Сумма')
    schedule = models.ForeignKey(Schedule, verbose_name='Расписание', on_delete=models.SET_NULL, null=True, related_name='donations')
    guest = models.ForeignKey(Guest, verbose_name='Донатор', on_delete=models.SET_NULL, null=True, related_name='donations')

    def __str__(self):
        return self.guest












