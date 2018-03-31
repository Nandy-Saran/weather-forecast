from accounts.models import Subscriber
for i in Subscriber.objects.all():
    i.delete()
# for
# user=user.objects.create()
Subscriber.objects.create(user=)