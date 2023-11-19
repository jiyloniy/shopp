from django.db import models


class Team(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to='team/')

    @property
    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        pass

    class Meta:
        db_table = 'TeamTable'
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    token = '6251800251:AAEv86CEuLjyEhyri8t_YQQMktbAE_TTdn8'

    chat_id = '1702651852'

    @property
    def send_from_telegram_bot(self):
        token = '6251800251:AAEv86CEuLjyEhyri8t_YQQMktbAE_TTdn8'
        chat_id = '1702651852'
        text = f'Name: {self.name}\nEmail: {self.email}\nMessage: {self.message}'
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        import requests
        requests.get(url)

        return True

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ContactTable'
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class COllection(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_banners(self):
        return self.banners.all()
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'CollectionTable'
        verbose_name = 'Collection'
        verbose_name_plural = 'Collections'


class Banner(models.Model):
    collection = models.ForeignKey(COllection, on_delete=models.RESTRICT, related_name='banners')
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='banner/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'BannerTable'
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
