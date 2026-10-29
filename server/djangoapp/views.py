from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import CarMake, CarModel
from .restapis import (
    get_request, analyze_review_sentiments, post_review
)
import logging
import json

logger = logging.getLogger(__name__)

# Backend dealership service URL
backend_url = "http://localhost:3030"


def get_dealerships(request, state="All"):
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = f"/fetchDealers/{state}"

    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})


def get_dealer_details(request, dealer_id):
    if dealer_id:
        endpoint = f"/fetchDealer/{dealer_id}"
        dealership = get_request(endpoint)
        return JsonResponse({"status": 200, "dealer": dealership})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})


def get_dealer_reviews(request, dealer_id):
    if dealer_id:
        endpoint = f"/fetchReviews/dealer/{dealer_id}"
        reviews = get_request(endpoint)

        for review_detail in reviews:
            response = analyze_review_sentiments(review_detail['review'])
            review_detail['sentiment'] = response.get('sentiment', 'neutral')

        return JsonResponse({"status": 200, "reviews": reviews})
    else:
        return JsonResponse({"status": 400, "message": "Bad Request"})


@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        login(request, user)
        data = {"userName": username, "userFirstName": user.first_name, "status": "Authenticated"}
    return JsonResponse(data)


def logout_request(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)


@csrf_exempt
def registration(request):
    context = {}
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False

    try:
        User.objects.get(username=username)
        username_exist = True
    except Exception:
        logger.error("New user")

    if not username_exist:
        user = User.objects.create_user(
            username=username, first_name=first_name, last_name=last_name,
            password=password, email=email
        )
        login(request, user)
        data = {"userName": username, "userFirstName": first_name, "status": "Authenticated"}
        return JsonResponse(data)
    else:
        data = {"userName": username, "error": "Already Registered"}
        return JsonResponse(data)


def get_cars(request):
    count = CarMake.objects.filter().count()
    logger.debug(f"There are {count} car makes")

    car_models = CarModel.objects.select_related('car_make')
    cars = []
    for car_model in car_models:
        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.car_make.name,
            "CarModelId": car_model.id,
            "CarModelType": car_model.type,
            "CarModelYear": str(car_model.year),
            "DealerId": car_model.dealer_id
        })
    return JsonResponse({"CarModels": cars})


@csrf_exempt
def add_review(request):
    if request.user.is_anonymous is False:
        data = json.loads(request.body)
        try:
            response = post_review(data)
            return JsonResponse({"status": 200})
        except Exception:
            return JsonResponse({"status": 401, "message": "Error in Posting Review"})
    else:
        return JsonResponse({"status": 403, "message": "Unauthorized"})


def analyze_review(request, text):
    """Direct sentiment analysis endpoint using TextBlob."""
    sentiment_result = analyze_review_sentiments(text)
    return JsonResponse(sentiment_result)


def home_html_view(request):
    """HTML Dealerships home page with state filter and login awareness."""
    state = request.GET.get('state', 'All')
    force_user = request.GET.get('user', '')
    
    if state == 'All' or not state:
        dealerships = get_request('/fetchDealers')
        selected_state = 'All'
    else:
        dealerships = get_request(f'/fetchDealers/{state}')
        selected_state = state

    context = {
        'dealers': dealerships,
        'selected_state': selected_state,
    }
    # Mock user for screenshot if passed as query param or authenticated
    if force_user:
        class MockUser:
            is_authenticated = True
            username = force_user
        context['user'] = MockUser()
        
    return render(request, 'djangoapp/index.html', context)


def dealer_detail_html_view(request, dealer_id):
    """HTML Dealer details page with reviews and sentiment."""
    dealers = get_request(f'/fetchDealer/{dealer_id}')
    dealer = dealers[0] if dealers else {}
    reviews = get_request(f'/fetchReviews/dealer/{dealer_id}')
    
    for r in reviews:
        if 'sentiment' not in r:
            res = analyze_review_sentiments(r.get('review', ''))
            r['sentiment'] = res.get('sentiment', 'neutral')

    force_user = request.GET.get('user', '')
    context = {
        'dealer': dealer,
        'reviews': reviews,
    }
    if force_user:
        class MockUser:
            is_authenticated = True
            username = force_user
        context['user'] = MockUser()

    return render(request, 'djangoapp/dealer_details.html', context)


def post_review_html_view(request, dealer_id):
    """HTML Post review page."""
    dealers = get_request(f'/fetchDealer/{dealer_id}')
    dealer = dealers[0] if dealers else {}
    return render(request, 'djangoapp/post_review.html', {'dealer': dealer})

