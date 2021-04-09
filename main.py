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

def showCompare(image, adverseImage):
    print(image.shape)
    image = image.permute(1,2,0)
    print(image.shape)
    adverseImage = adverseImage.reshape(channels, size, size)
    print(adverseImage.shape)
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
    plt.axis('off')
    # Difference
    plt.subplot(1, 3, 3)
    plt.title('Difference')
    difference = adverseImage - image
    plt.imshow((difference / abs(difference).max() * 0.2 + 0.5))
    plt.axis('off')
    plt.show()

resnet = models.resnet34(pretrained=True).eval()
preprocessing = dict(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225], axis=-3)
model = foolbox.models.PyTorchModel(resnet, bounds=(0,1), preprocessing=preprocessing)
images, labels = foolbox.utils.samples(model, dataset='imagenet', batchsize=batch, data_format='channels_first', bounds=(0, 1))
images = images.reshape(batch, channels, size, size)
labels = labels.type(torch.long)
print(images.shape)
print("Labels: ", labels)
clean_acc = foolbox.utils.accuracy(model, images, labels)
print(f"clean accuracy:  {clean_acc * 100:.1f} %")

attacks = [
    foolbox.attacks.LinfPGD(),
    foolbox.attacks.FGSM(),
    foolbox.attacks.LinfDeepFoolAttack()
]
attackNames = ['fpgd', 'fgsm', 'df']
epsilons = [
    # 0.0005,
    # 0.001,
    # 0.0015,
    # 0.002,
    # 0.003,
    # 0.005,
    0.01
]
for x, attack in enumerate(attacks):
    raw_advs, clipped_advs, success = attack(model, images, labels, epsilons=epsilons)
    for i in range(batch):
        for j in range(len(epsilons)):
            #this currently jus names each images after its epsilon value, and the (useless) float value class label.
            #this is less than ideal, need to get proper class label
            filepath = 'pics/'+str(attackNames[x])+'/_'+str(epsilons[j])+'_'+str(labels[i])+'.png'
            save_image(raw_advs[j], filepath)
            #showCompare(images[i],raw_advs[i])
    for y in raw_advs:
        adv_acc = foolbox.utils.accuracy(model, y, labels)
        print(f"adv accuracy:  {adv_acc * 100:.1f} %")
