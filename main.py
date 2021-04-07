#script to generate and save adversarial images
#mostly taken from foolbox docs/examples
#---------------------------------------
#imagenet image params
batch = 1
channels = 3
size = 224
classes = 1000

import foolbox, torch
import matplotlib.pyplot as plt
import numpy as np
from torchvision.utils import save_image
import torchvision.models as models
from PIL import Image 

resnet = models.resnet34(pretrained=True).eval()
model = foolbox.models.PyTorchModel(resnet, bounds=(0,1))
images, labels = foolbox.utils.samples(model, dataset='imagenet', batchsize=batch, data_format='channels_first', bounds=(0, 1))
images = images.reshape(batch, channels, size, size)
labels = labels.type(torch.long)
print(images.shape)
print("Labels: ", labels)
clean_acc = foolbox.utils.accuracy(model, images, labels)
print(f"clean accuracy:  {clean_acc * 100:.1f} %")
#attack
attack = foolbox.attacks.LinfPGD()
epsilons = [
    0.005
]
raw_advs, clipped_advs, success = attack(model, images, labels, epsilons=0.005)
#for x in raw_advs:
    #adv_acc = foolbox.utils.accuracy(model, x, labels)
    #print(f"adv accuracy:  {adv_acc * 100:.1f} %")
for i in range(batch):
    image = images[i]
    image = image.permute(1,2,0)
    adverseImage = raw_advs[i]
    adverseImage = adverseImage.permute(1,2,0)
    plt.figure()
    # Original
    plt.subplot(1, 3, 1)
    plt.title('Label: '+ str(labels[i]))
    plt.imshow(image)
    plt.axis('off')
    # Adversarial
    plt.subplot(1, 3, 2)
    plt.title('Adversarial: ')
    plt.imshow(adverseImage)
    save_image(raw_advs[i], str(labels[i]) + '.png')
    plt.axis('off')
    # Difference
    plt.subplot(1, 3, 3)
    plt.title('Difference')
    difference = adverseImage - image
    plt.imshow((difference / abs(difference).max() * 0.2 + 0.5))
    plt.axis('off')

    plt.show()