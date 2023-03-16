from django.db import IntegrityError
from django.db.models import When, Value, Case, Q, CharField
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import User
from profiles.models import Requests


class UserList(ListView):
    model = User

    def get_queryset(self):
        if self.request:
            username = self.request.GET.get('username')
            user = self.request.user
            invites = [i[0] for i in user.sender.all().values_list('recipient')]
            users = User.objects.filter(username__contains=username) \
                .exclude(id=self.request.user.id) \
                .annotate(invited=Case(When(Q(id__in=invites), then=Value('fa-user-check')),
                                       default=Value('fa-user-plus'), output_field=CharField()))
            return users
        return super().get_queryset()


def profile_friends(request, pk):
    if request.user.is_authenticated:
        user = User.objects.prefetch_related('friends').get(id=pk)
        friends_list = user.friends.all()
        context = {'user': user, 'friends_list': friends_list}
        return render(request, 'base/profilefriends.html', context)
    else:
        return redirect('login')


def profile_requests(request, pk):
    if request.user.is_authenticated:
        requests = Requests.objects.filter(recipient_id=request.user.id)
        context = {'requests': requests}
        return render(request, 'base/requests.html', context)
    else:
        return redirect('login')


def profile_subscribers(request, pk):
    if request.user.is_authenticated:
        subscribers_list = User.objects.prefetch_related('friends').get(id=request.user.id).friends.all()
        context = {'subscribers_list': subscribers_list}
        return render(request, 'base/subscribers.html', context)
    else:
        return redirect('login')


def profile_subscriptions(request, pk):
    if request.user.is_authenticated:
        subscriptions_list = User.objects.prefetch_related('friends').get(id=request.user.id).friends.all()
        context = {'subscriptions_list': subscriptions_list}
        return render(request, 'base/subscriptions.html', context)
    else:
        return redirect('login')


def profile_block(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        context = {'user': user}
        return render(request, 'base/block.html', context)
    else:
        return redirect('login')


def invite_friend(request):
    if request.GET:
        recipient_id = request.GET.get('inviter_id')
        recipient = User.objects.get(id=recipient_id)
        inviter = request.user
        if Requests.objects.filter(recipient=inviter, inviter=recipient).exists():  # they  will be friends
            recipient.friends.add(inviter)
            Requests.objects.filter(recipient=inviter, inviter=recipient).delete()
            return HttpResponse(status=201)
        try:
            Requests.objects.create(recipient=recipient, inviter=inviter)
            return HttpResponse(status=201)
        except IntegrityError:
            return HttpResponse(status=400)


def delete_friend(request):
    if request.GET:
        friend = request.GET.get('friend')
        User.objects.get(id=request.user.id).friends.remove(friend)
        return HttpResponse(status=204)