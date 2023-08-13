from django.shortcuts import render,redirect
import json,random
from django.http import JsonResponse
from .utils import load_data,save_data


def menu(request):
    data = load_data()
    return render(request, 'menu.html', {'data': data})
    # return JsonResponse(data,safe=False)

def add_menu(request):
    if request.method == 'POST':
        dish_name = request.POST.get('dish_name')
        price = request.POST.get('price')
        availability = request.POST.get('availability', False)

        new_dish = {
            "id":  random.randint(1,1543687648),# Assign a unique ID
            "dish_name": dish_name,
            "price": price,
            "availability": availability
        }

        data = load_data()
        data.append(new_dish)
        save_data(data)

        return redirect('menu')
    
    return render(request, 'add_menu.html')

def remove_menu(request, dish_id):
    data = load_data()

    # Find the dish with the specified ID and remove it
    for dish in data:
        if dish['id'] == dish_id:
            data.remove(dish)
            save_data(data)
            break

    return redirect('menu')

def update_availability(request, dish_id):
    data = load_data()

    # Find the dish with the specified ID and update its availability
    for dish in data:
        if dish['id'] == dish_id:
            dish['availability'] = not dish['availability']
            save_data(data)
            break

    return redirect('menu')