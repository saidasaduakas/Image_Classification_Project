import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
import json
from .models import ImageDB

img_height, img_width = 224, 224
with open('./models/imagenet_classes.json', 'r') as f:
    labelInfo = f.read()

labelInfo = json.loads(labelInfo)
model = load_model('./models/MobileNetModelImagenet.h5')


def index(request):
    context = {'a': 1}
    return render(request, 'index.html', context)


def predictImage(request):
    print(request)
    print(request.POST.dict())
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    testimage = '.' + filePathName
    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x = x / 255
    x = x.reshape(1, img_height, img_width, 3)
    predi = model.predict(x)
    import numpy as np
    predictedLabel = labelInfo[str(np.argmax(predi[0]))]
    context = {'filePathName': filePathName, 'predictedLabel': predictedLabel}
    ImageDB.objects.create(paths=filePathName, des=predictedLabel)

    return render(request, 'index.html', context)


def viewDataBase(request):
    listofImages = os.listdir('./media/')
    listofImagesPath = ['./media/' + i for i in listofImages]
    context = {'listofImagesPath': listofImagesPath}
    return render(request, 'viewDB.html', context)