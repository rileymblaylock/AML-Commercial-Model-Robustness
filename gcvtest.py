import os
path = os.getcwd()
from google.cloud import vision
import io
import glob
import matplotlib.pyplot as plt


#dict of labels
labelsApprox = {243: 'bull mastiff, dog',
            559: 'folding chair, seat, furniture',
            438: 'beaker, bottle, liquid',
            990: 'buckeye, horse chestnut, conker, plant',
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
epsilons = [0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5]
epsCorrect = {
            'original': 0,
            0.0005 : 0,
            0.001 : 0,
            0.005 : 0,
            0.01 : 0,
            0.05 : 0,
            0.1 : 0,
            0.5 : 0,
            1.0 : 0
            }
epsWrong = {
            'original': 0, 
            0.0005 : 0, 
            0.001 : 0, 
            0.005 : 0, 
            0.01 : 0, 
            0.05 : 0, 
            0.1 : 0, 
            0.5 : 0, 
            1.0 : 0
            }
#set paths
path = path + '\\pics\\resnet\\'
biapath = path + '\\bia\\'
fgsmpath = path + '\\fgsm\\'
fpgdpath = path + '\\fgpd\\'
testpath = path + '\\test\\'

def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()
    numCorrectTotal = 0; numTotal = 0
    with open(path+"TestingResults.txt",'w') as file:
        for filename in glob.glob(os.path.join(path, '*.png')):
            numTotal+=1
            #get filename dict key and epsilon value from name
            for key in labelsApprox:
                if str(key) in filename:
                    classLabel = labelsApprox[key]
                    break
            for eps in epsilons:
                if str(eps) in filename:
                    epsVal = eps
            #query classifier with image and get response
            with io.open(filename, 'rb') as image_file:
                content = image_file.read()
            image = vision.Image(content=content)
            response = client.label_detection(image=image)
            labels = response.label_annotations

            #determine if output labels match true and record
            numCorrectLocal=0
            print('Labels:')
            for label in labels:
                print(label.description.lower())
                if(label.description.lower() in classLabel):
                    numCorrectLocal+=1
                    numCorrectTotal+=1
                    epsCorrect[epsVal]+=1
                    break
            if(numCorrectLocal == 0):
                epsWrong[epsVal]+=1
                file.writelines(os.path.basename(filename) + ' Missed: TRUE: ' 
                        + classLabel + ' // GIVEN: ' + labels[0].description.lower() 
                        + ' or ' + labels[1].description.lower() 
                        + ' or '+ labels[2].description.lower() + ' EPSVAL: ' + str(epsVal))
                file.writelines('\n')
        #final calculations
        percentCor = (numCorrectTotal/numTotal)*100
        file.writelines('Overall Accuracy: ' + str(percentCor) + '%')
        file.writelines('\n')
        file.writelines('Accuracy per Epsilon: \n')
        for key in epsilons:
            if epsWrong[key] > 0:
                file.writelines('Epsilon value ' + str(key) + ' accuracy: ' 
                            + str((epsWrong[key]/(epsCorrect[key]+epsWrong[key])*100)) + '%\n')
                file.writelines('Epsilon of ' + str(key) 
                + ' was misclassified ' + str(epsWrong[key]) 
                + ' times.')
                file.writelines('\n')
            else:
                file.writelines('Epsilon value ' + str(key) + ' accuracy: ' 
                            + str(100) + '%\n')
    
    #graphs
    newepsCorrect = {str(key): value for key, value in epsCorrect.items()}
    plt.bar(newepsCorrect.keys(), newepsCorrect.values())
    plt.title('Per Epsilon Number Correct - BIA Attack')
    plt.xlabel('Epsilon value')
    plt.ylabel('Number correct')
    plt.show()


detect_labels(testpath)