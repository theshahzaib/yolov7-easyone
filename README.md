# yolov7-easyone
 Easy One Process YOLOv7 Custom Dataset Training

## 1. Introduction
Easy One Process YOLOv7 Custom Dataset Training is a simple and easy way to train your own custom dataset with YOLOv7. It is a one-click process that can be completed in 1 minute. It is suitable for beginners who want to quickly train their own custom dataset.

## 2. Conda Environment
The conda environment is as follows:
```cmd
conda create -n yolov7 python=3.8
```
```cmd
conda activate yolov7
```

## 3. Download YOLOv7-easyone
```sh
git clone https://github.com/theshahzaib/yolov7-easyone.git
```

## 4. Install Requirements
```cmd
pip install -r requirements.txt
```

## 5. Settting Up Dataset
1. Create a folder named "[custom model name]" in the root directory.
2. Create a folder named "dataset" in the "[custom model name]" folder.
3. Place your custom LABELED dataset in the "dataset" folder.

## 6. One Process Autoscripts Generator
1. Update the parameters or variables in the "python one_process_yolov7.py" file.
2. Update config file(s) in the "cfg/custom" folder.
3. Run the following command in "[custom model name]" folder.  
    ```cmd
    python one_process_yolov7.py
    ```
# One Process Autoscript
## - Auto Split the dataset into 'Train' and 'Valid' folders.
## - Generate the custom "coco.yaml" file with all autoset paths.
## - Generate the custom "train.sh" file with all autoset paths.
#


## 7. Training.
```cmd
sh train.sh
```

## 8. Testing.

1. Run the following command to start testing.
    ```cmd
    python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source data/images/
    ```
2. Run the following command to start testing on video.
    ```cmd
    python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source data/video/test.mp4 --save-txt --save-conf --save-crop
    ```
3. Run the following command to start testing on webcam.
    ```cmd
    python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source 0
    ```
4. Run the following command to start testing on RTSP stream.
    ```cmd
    python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov
    ```
5. Run the following command to start testing on RTMP stream.
    ```cmd
    python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source rtmp://
    ```
6. Run the following command to start testing on HTTP stream.
    ```cmd
    python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source http://
    ```
7. Run the following command to start testing on image.
    ```cmd
    python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source data/images/zidane.jpg --save-txt --save-conf --save-crop
    ```
8. Run the following command to start testing on folder.
    ```cmd
    python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source data/images/ --save-txt --save-conf --save-crop
    ```
9. Run the following command to start testing on COCO val2017 dataset.
    ```cmd
    python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.25 --source data/coco/val2017 --save-txt --save-conf --save-crop
    ```

# Acknowledgements
This project is based on the following projects:
<details><summary> <b>Expand</b> </summary>

* [https://github.com/AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)
* [https://github.com/WongKinYiu/yolor](https://github.com/WongKinYiu/yolor)
* [https://github.com/WongKinYiu/PyTorch_YOLOv4](https://github.com/WongKinYiu/PyTorch_YOLOv4)
* [https://github.com/WongKinYiu/ScaledYOLOv4](https://github.com/WongKinYiu/ScaledYOLOv4)
* [https://github.com/Megvii-BaseDetection/YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)
* [https://github.com/ultralytics/yolov3](https://github.com/ultralytics/yolov3)
* [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
* [https://github.com/DingXiaoH/RepVGG](https://github.com/DingXiaoH/RepVGG)
* [https://github.com/JUGGHM/OREPA_CVPR2022](https://github.com/JUGGHM/OREPA_CVPR2022)
* [https://github.com/TexasInstruments/edgeai-yolov5/tree/yolo-pose](https://github.com/TexasInstruments/edgeai-yolov5/tree/yolo-pose)

</details>

Thank you for your support https://github.com/WongKinYiu/yolov7
