from django.shortcuts import render, redirect
from .models import Category, Photo


def image(request):

    category = request.GET.get('category')
    
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    # photos = Photo.objects.all()
    context = {'categories': categories, 'photos':photos}
    return render(request, 'images/galery.html', context)

def viewImage(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'images/image.html', {'photo':photo})


def addImage(request):
    categories = Category.objects.all()

    if request.method =='POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category = category,
            description=data['description'],
            image=image,
        )

        return redirect('images')

    context = {'categories': categories}
    return render(request, 'images/addImage.html', context)