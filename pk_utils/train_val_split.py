import os


image_pth = '/mnt/driver2/Github_project2/Object_Detection_torch/yolo5_docker/meat_type_identification/images/train2017'
label_pth = '/mnt/driver2/Github_project2/Object_Detection_torch/yolo5_docker/meat_type_identification/labels'
out_pth_name = 'meat_type_identification_new'

parent_pth = os.path.dirname(label_pth)
# make a new folder for gerenerated data
os.makedirs(parent_pth + '/' + out_pth_name)

