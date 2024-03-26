from django.shortcuts import render
import json
from django.http import JsonResponse
from .models import Task


def add_task(request):
    with open("tasks.json", "r") as file:
        data = json.load(file)
    title = input("Görev başlığını girin: ")
    description = input("Görev açıklamasını girin: ")
    Task.objects.create(title=title, description=description)
    return JsonResponse({"Görev başarıyla eklendi"})

def delete_task(request):
    with open("tasks.json", "r") as file:
        data = json.load(file)
    task_id = input("Görev id girin: ")
    Task.objects.filter(pk=task_id).delete()
    return JsonResponse({"Görev başarıyla silindi"})

def update_task(request):
    with open("tasks.json", "r") as file:
        data = json.load(file)
    task_id = input("Görev id giriniz ")
    title = input("Görev başlığını giriniz: ")
    description = input("Görev açıklamasını giriniz: ")
    Task.objects.filter(pk=task_id).update(title=title, description=description)
    return JsonResponse({"Görev başarıyla güncellendi"})

def list_tasks(request):
    with open("tasks.json", "r") as file:
        data = json.load(file)
    tasks = list(Task.objects.all().values())
    return JsonResponse({"Görevler": tasks})

