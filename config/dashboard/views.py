from django.shortcuts import render
from leads.models import Lead
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required

@login_required
def home(request):

    total_leads = Lead.objects.count()

    new_today = Lead.objects.filter(
        created_at__date=now().date()
    ).count()

    won_deals = Lead.objects.filter(
        status="won"
    ).count()

    recent_activity = Lead.objects.order_by(
        "-created_at"
    )[:5]

    stats = {
        "total_leads": total_leads,
        "new_today": new_today,
        "won_deals": won_deals,
        "revenue": "$24,500"
    }

    context = {
        "stats": stats,
        "recent_activity": recent_activity
    }

    return render(request, "dashboard/home.html", context)