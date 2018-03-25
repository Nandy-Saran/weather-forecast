from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, send_mail
from accounts.forms import SignUpForm, SubscriberForm
from accounts.tokens import account_activation_token
from accounts.models import Profile, Subscriber
from datamodel.models import Place, Crop, Weather
from django.template import loader


# Create your views here.


@login_required
def subscriberView(request, **kwargs):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            print(obj)
            print(request.user)

            print(obj)
            obj.save()
            return redirect('home1')
    else:
        form = SubscriberForm()
    form.fields['user'].initial = request.user
    return render(request, 'subscriber.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_mail(subject=subject,
                      message=message,
                      from_email='admin@gmail.com',
                      recipient_list=[user.email],
                      )
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


@login_required
def home1(request):
    instanc = Subscriber.objects.get(user=request.user)
    print(instanc.location)
    WeathObj = Weather.objects.filter(place=instanc.location).filter(datenum__gte=0)
    dic = {}
    dic['avail'] = True
    Forecast = []
    message = ''
    comm = ''
    if instanc.crop1.pH_min and instanc.crop1.pH_min > instanc.soil_ph:
        comm += 'Cultivate your crop according to your soil pH\nYour crop' + instanc.crop1.name + 'requires soil with pH range from' + str(
            instanc.crop1.pH_min) + ' to ' + str(instanc.crop1.pH_max)
    if instanc.crop1.pH_min and instanc.crop1.pH_max < instanc.soil_ph:
        comm += 'Cultivate your crop according to your soil pH\nYour crop' + instanc.crop1.name + 'requires soil with pH range from' + str(
            instanc.crop1.pH_min) + ' to ' + str(instanc.crop1.pH_max)
    for i in WeathObj:
        daily = {}
        daily['desc'] = i.WindDesc
        daily['max_temp'] = i.mintempC
        daily['min_temp'] = i.maxtempC
        daily['humid'] = i.humidity
        daily['rainMM'] = i.rainMM
        daily['sunrise'] = i.sunrise
        daily['sunset'] = i.sunset
        daily['moonrise'] = i.moonrise
        daily['moonset'] = i.moonset
        daily['pressure'] = i.pressure
        daily['windspMil'] = i.WindSpeedMil
        daily['windGstMil'] = i.WindGustMil
        daily['date'] = i.date
        daily['datenum'] = i.datenum
        daily['WindDirdeg'] = i.WindDirdeg
        daily['WinddirPt'] = i.Winddir16Point
        if instanc.crop1.MintempC and instanc.crop1.MintempC < i.mintempC:
            message += 'Your Crop ' + i.name + ' may get affected due to cold temperature(' + str(
                i.mintempC) + ' deg C) in' + str(i.datenum) + 'day(s)\n'
        if instanc.crop1.MaxtempC and instanc.crop1.MaxtempC > i.maxtempC:
            message += 'Your Crop ' + i.name + ' may get affected due to high temperature( ' + str(
                i.maxtempC) + ' deg C) in' + str(i.datenum) + 'day(s)\n'
        # daily['message'] = message
        Forecast.append(daily)
    dic['data'] = Forecast
    dic['advice'] = comm

    dic1 = {}
    totinst = Subscriber.objects.filter(location=instanc.location)
    req = {}
    for i in totinst:
        flag = 0
        for j in dic1:
            if j == instanc.crop1:
                dic1[j] += 1
                flag = 1
                break
        if flag == 0:
            dic1[instanc.crop1] = 1
    lis = sorted(req, key=lambda k: dic1[k])
    count = 0
    for a in lis:
        if a != instanc.crop1:
            ins = Crop.objects.get(name=a)
            if ins.pH_min and ins.pH_min > instanc.soil_ph and ins.pH_max and ins.pH_max < instanc.soil_ph:
                req['crop'] = a
                st = ins.seas_no
                seas = ''
                if st.find('-') != -1:
                    req['season'] = 'Any month from January to December'
                else:
                    dicsp = {1: 'January', 2: 'Febraury', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
                             8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
                    ar = st.split(',')
                    for x in ar:
                        seas += dicsp[x] + ','
                    req['season'] = seas
                count += 1
                break
    dic['required'] = req
    print(req)
    template = loader.get_template('home1.html')
    context = {'forecast': dic}
    return render(request, 'home1.html', context)


def home(request):
    return render(request, 'home.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')


def fill_profile(request):
    if request.method == 'POST':
        form = (request.POST)
        if form.is_valid():
            print('checked')
            pass
    else:
        form = ''
        pass
