from datamodel.models import Place

a=['Coimbatore','Chennai','pondicherry','madurai','mannargudi','cuddalore','villupuram','shillong','mathura','delhi','cherrapunji','thiruvananthapuram']
for i in a:
    s=Place.objects.create(name=i)
