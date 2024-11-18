from django.shortcuts import render, redirect

from .forms import Step1Form, Step2Form, Step3Form
from .models import SurveyResponse


def index(request):
    responses = SurveyResponse.objects.all()
    return render(request, "survey/index.html", {"responses": responses})


def step1(request):
    if request.method == "POST":
        form = Step1Form(request.POST)
        if form.is_valid():
            request.session["step1"] = form.cleaned_data
            return redirect("step2")
    else:
        form = Step1Form(initial=request.session.get("step1", {}))

    return render(request, "survey/step1.html", {"form": form})


def step2(request):
    if "step1" not in request.session:
        return redirect("step1")

    if request.method == "POST":
        form = Step2Form(request.POST)
        if form.is_valid():
            request.session["step2"] = form.cleaned_data
            return redirect("step3")
    else:
        form = Step2Form(initial=request.session.get("step2", {}))

    return render(request, "survey/step2.html", {"form": form})


def step3(request):
    if "step2" not in request.session:
        return redirect("step2")

    if request.method == "POST":
        form = Step3Form(request.POST)
        if form.is_valid():
            request.session["step3"] = form.cleaned_data

            name = request.session.get("step1").get("name")
            SurveyResponse.objects.create(
                name=name if name else None,
                step1_data=request.session.get("step1"),
                step2_data=request.session.get("step2"),
                step3_data=request.session.get("step3"),
            )

            for key in ["step1", "step2", "step3"]:
                if key in request.session:
                    del request.session[key]

            return redirect("thank_you")
    else:
        form = Step3Form(initial=request.session.get("step3", {}))

    return render(request, "survey/step3.html", {"form": form})


def thank_you(request):
    return render(request, "survey/thank_you.html")
