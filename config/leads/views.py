from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Lead
from .forms import LeadForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def lead_list(request):

    query = request.GET.get("q")
    status = request.GET.get("status")

    leads = Lead.objects.all().order_by("-created_at")

    if query:
        leads = leads.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(company__icontains=query)
        )
    if status:
        leads = leads.filter(status=status)

    return render(request, "leads/lead_list.html", {
        "leads": leads,
        "query": query,
        "status": status
    })


def add_lead(request):

    if request.method == "POST":

        form = LeadForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Lead added successfully!")
            return redirect("leads:list")

    else:
        form = LeadForm()

    return render(request, "leads/add_lead.html", {
        "form": form
    })


def edit_lead(request, pk):

    lead = get_object_or_404(Lead, id=pk)

    if request.method == "POST":

        form = LeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()
            messages.success(request, "Lead updated successfully!")
            return redirect("leads:list")

    else:
        form = LeadForm(instance=lead)

    return render(request, "leads/edit_lead.html", {
        "form": form
    })


def delete_lead(request, pk):

    lead = get_object_or_404(Lead, id=pk)

    lead.delete()

    messages.success(request, "Lead deleted successfully!")


    return redirect("leads:list")