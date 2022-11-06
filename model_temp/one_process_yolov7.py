import shutil,os,glob

###################################################
## 1-Place labeled dataset in 'dataset' folder
## 2-Delete 'train' and 'valid' folder if exsists
###################################################

#########################################################
## Update the below parameters or variables accordingly
#########################################################

# Classes Names
classes = ['nfpa']
no_of_classes = len(classes)

# Image Window Size
window_size = [416,416]
# GPUs i.e '0,1,2,3' for training 'cpu' if training on CPU
gpu_count = 'cpu'
# Batch
batch = 32
# Epochs
epochs = 3

##################################################
try:

    current_dir = './dataset'

    os.mkdir("train")
    os.mkdir("valid")

    percentage_test = 20;
    counter = 1  
    index_test = round(100 / percentage_test)  
    for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):  
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))

        # print('prossessing ...')
        if counter == index_test:
            counter = 1
            #file_test.write(path_data + title + '.jpg' + "\n")
            shutil.move(current_dir+"/"+title+".jpg","./valid")
            shutil.move(current_dir+"/"+title+".txt","./valid")
            #print(title)
        else:
            #file_train.write(path_data + title + '.jpg' + "\n")
            print(title+ext)
            shutil.move(current_dir+"/"+title+".jpg","./train")
            shutil.move(current_dir+"/"+title+".txt","./train")
            counter = counter + 1

    current_dir_valid="./valid"

    os.mkdir(current_dir_valid+"/images")
    os.mkdir(current_dir_valid+"/labels")

    lbl=current_dir_valid+"/labels/"
    img=current_dir_valid+"/images/"

    for files in glob.glob(current_dir_valid+'/*.*'):
         if files.endswith(".jpg"):
                pwd=files[:-4]+".jpg"
                print(pwd)
                shutil.move(pwd,img)
                
         elif files.endswith(".txt"):
                pwd=files[:-4]+".txt"
                print(pwd)
                shutil.move(pwd,lbl)
           
    current_dir_train="./train"


    os.mkdir(current_dir_train+"/images")
    os.mkdir(current_dir_train+"/labels")


    lbl=current_dir_train+"/labels/"
    img=current_dir_train+"/images/"

    for files in glob.glob(current_dir_train+'/*.*'):
         if files.endswith(".jpg"):
                pwd=files[:-4]+".jpg"
                print(pwd)
                shutil.move(pwd,img)
                
         elif files.endswith(".txt"):
                pwd=files[:-4]+".txt"
                print(pwd)
                shutil.move(pwd,lbl)
    
    print('Dataset Split Done! 🙌')

except:
    print('Folders Already Exsists! 🙅')

##################################################
## Generating Files
##################################################

FILE_PATH_yml = '../coco.yaml'
f = open(FILE_PATH_yml, 'w')

dataset_folder_name = os.getcwd().split('/')[-1]

f.write('train: '+dataset_folder_name+'/train/images\n')
f.write('val: '+dataset_folder_name+'/valid/images\n')

f.write('nc: '+str(no_of_classes)+'\n')
f.write('names: '+str(classes)+'\n')

f.close()


##########################################


FILE_PATH_trainsh = '../train.sh'
f = open(FILE_PATH_trainsh, 'w')
# yolov7-tiny
f.write('python train.py --img '+str(window_size[0])+' --batch '+str(batch)+' --epochs '+str(epochs)+' --data ./coco.yaml --cfg ./cfg/custom/yolov7-tiny.yaml --weights yolov7-tiny.pt --name '+dataset_folder_name+' --device '+gpu_count+'\n')
# yolov7
f.write('# python train.py --img '+str(window_size[0])+' --batch '+str(batch)+' --epochs '+str(epochs)+' --data ./coco.yaml --cfg ./cfg/custom/yolov7.yaml --weights yolov7.pt --name '+dataset_folder_name+' --device '+gpu_count+'\n')
# yolov7x
f.write('# python train.py --img '+str(window_size[0])+' --batch '+str(batch)+' --epochs '+str(epochs)+' --data ./coco.yaml --cfg ./cfg/custom/yolov7x.yaml --weights yolov7x.pt --name '+dataset_folder_name+' --device '+gpu_count+'\n')
# yolov7-d6
f.write('# python train.py --img '+str(window_size[0])+' --batch '+str(batch)+' --epochs '+str(epochs)+' --data ./coco.yaml --cfg ./cfg/custom/yolov7-d6.yaml --weights yolov7-d6.pt --name '+dataset_folder_name+' --device '+gpu_count+'\n')
f.close()

print('Scripts Updated!')
print('--- THANKS! --- 🐇')
#############################################