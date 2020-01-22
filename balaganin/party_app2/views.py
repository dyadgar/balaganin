from django.shortcuts import render, redirect
from .models import EventList, Category
from .forms import EventListImageForm
from django.views import View
from django.views.generic import ListView, DetailView
from .filters import EventFilter


def index2(request):
    events = EventList.objects.all()
    categories = Category.objects.all()
    form = EventListImageForm()

    if request.method == "POST":
        if "eventAdd" in request.POST:
            # form = ImageForm(request.POST, request.FILES)
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]
            venue = request.POST["venue"]
            link = request.POST["link"]
            country= request.POST["country_select"]
            price= request.POST["price_select"]
            content = title + " -- " + date + " " + category
            event = EventList(title=title, content=content, event_date=date, category=Category.objects.get(name=category), venue=venue, link=link, country=country, price= price)
            event.save()
            form = EventListImageForm(request.POST, request.FILES, instance=event)
            if form.is_valid():
                form.save()
            return redirect("index2")

        if "eventDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]
            event = EventList.objects.get(id=int(checkedlist))
            event.delete()

    return render(request, "party_app2/index.html", {"events": events, "categories":categories, "form": form, 'p_choices': EventList.price_choices, 'c_choices': EventList.country_choices  })


class EventListView(ListView):
    model = EventList
    template_name = 'party_app2/eventlist_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EventFilter(self.request.GET, queryset=self.get_queryset())
        return context
