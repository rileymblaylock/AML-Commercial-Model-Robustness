# AML Commercial Model Robustness
 Testing the robustness of three state-of-the-art commercial image recognition models to adversarial attacks

 main.py generate adversarial images - specifies 20 images from imagenet, choice of either pretrained resnet or pretrained googlenet, 3 attacks, and 6 different perturbation epsilons per attack

 gcvtest.py runs adversarial images on the googlecloudvision API - tests a single folder of pertured images per model - wont actually run, needs user .json which is hidden from git
 
 pics folder contains final adversarial images used to test google classifier
