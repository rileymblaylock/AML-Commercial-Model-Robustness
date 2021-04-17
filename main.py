#script to generate and save adversarial images
#mostly taken from foolbox docs/examples
#---------------------------------------
#image params
batch = 20
channels = 3
#size for imagenet is 224, for cifar10 and cifar100 is 32, for mnist is 28
size = 224
#classes for imagenet is 1000, for cifar10 is 10
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

#only trained on imagenet
resnet = models.resnet34(pretrained=True).eval()
preprocessing = dict(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225], axis=-3)
model = foolbox.models.PyTorchModel(resnet, bounds=(0,1), preprocessing=preprocessing)
images, labels = foolbox.utils.samples(model, dataset='imagenet', batchsize=batch, data_format='channels_first', bounds=(0, 1))
#labels are numbers but correspond to imagenet human readable labels in the actual imagenet class label list
print(images.shape)
images = images.reshape(batch, channels, size, size)
labels = labels.type(torch.long)
print(images.shape)
print("Labels: ", labels)
clean_acc = foolbox.utils.accuracy(model, images, labels)
print(f"clean accuracy:  {clean_acc * 100:.1f} %")
labelsReal = {243: 'bull mastiff',
            559: 'folding chair',
            438: 'beaker',
            990: 'buckeye, horse chestnut, conker',
            949: 'strawberry',
            853: 'thatch, thatched roof',
            609: 'jeep, landrover',
            915: 'yurt',
            455: 'bottlecap',
            541: 'drum, membranophone, tympan',
            630: 'Loafer',
            741: 'prayer rug, prayer mat',
            471: 'cannon',
            129: 'spoonbill',
            99: 'goose',
            251: 'dalmatian, coach dog, carriage dog',
            22: 'bald eagle, American eagle, Haliaeetus leucocephalus',
            317: 'leafhopper',
            305: 'dung beetle'}
labelsApprox = {243: 'bull mastiff, dog',
            559: 'folding chair, seat, furniture',
            438: 'beaker',
            990: 'buckeye, horse chestnut, conker',
            949: 'strawberry, fruit',
            853: 'thatch, thatched roof, house',
            609: 'jeep, landrover, vehicle, car',
            915: 'yurt, tent, house, hut',
            455: 'bottlecap',
            541: 'drum, membranophone, tympan, instrument',
            630: 'Loafer, shoe',
            741: 'prayer rug, prayer mat, carpet',
            471: 'cannon',
            129: 'spoonbill, bird',
            99: 'goose, bird',
            251: 'dalmatian, coach dog, carriage dog',
            22: 'bald eagle, American eagle, Haliaeetus leucocephalus, bird',
            317: 'leafhopper, insect, bug',
            305: 'dung beetle, insect, bug'}

attacks = [
    foolbox.attacks.LinfPGD(),
    foolbox.attacks.FGSM(),
    foolbox.attacks.LinfBasicIterativeAttack()
]
attackNames = ['pgd', 'fgsm', 'bia']
epsilons = [
    0.0,
    0.0005,
    0.001,
    0.005,
    0.01,
    0.1,
    0.5,
    1
]
for x, attack in enumerate(attacks):
    raw_advs, clipped_advs, success = attack(model, images, labels, epsilons=epsilons)
    #first index is epsilon, 2nd is batch index
    for i in range(len(epsilons)):
        for j in range(batch):
            if (epsilons[i] == 0.0):
                filepath = 'pics/'+str(attackNames[x])+'/original'+str(labels[j])+'_.png'
                save_image(raw_advs[i][j], filepath)
            else: 
                #this currently jus names each images after its epsilon value, and the (useless) float value class label.
                #this is less than ideal, need to get proper class label
                filepath = 'pics/'+str(attackNames[x])+'/'+str(epsilons[i])+'_'+str(labels[j])+'_.png'
                save_image(raw_advs[i][j], filepath)
                #showCompare(images[i],raw_advs[j])
        for y in raw_advs:
            adv_acc = foolbox.utils.accuracy(model, y, labels)
            print(f"adv accuracy:  {adv_acc * 100:.1f} %")

