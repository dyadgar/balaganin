import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'balaganin.settings')
django.setup()

from django.contrib.auth.models import User
from faker import Faker
import random
import secrets

fake = Faker()

# for i in range(1,4):
#    event = EventList(
#        title= fake.color_name(),
#        content= fake.color_name(),
#        created= fake.date_this_year(before_today=True, after_today=False),
#        event_date= fake.date_this_year(before_today=False, after_today=True),
#        category= Category.objects.get(id=),
#        link= fake.url(),
#        venue= fake.company(),
#    )
#    event.save()
#


for i in range(1,200):
    fname= fake.first_name()
    lname= fake.last_name()
    user = User.objects.create_user(
        first_name = fname,
        last_name = lname,
        username=fname+lname,
        email = fake.email(),
        # phone = fake.Phone.EnUs.phone(),
        # city = fake.Address.city(),
        # country = fake.Address.country(),
        password='123456ASK',
    )
    user.save()
    # class EventList(models.Model):
    #     title = models.CharField(max_length=250)
    #     content = models.TextField(blank=True)
    #     created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    #     event_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    #     category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    #     link = models.URLField(max_length=200, default='www.google.com')
    #     venue = models.CharField(max_length=200, null=True)