import torch;
import cv2;
import os;
from PIL import Image
import numpy as np
import torchvision.transforms as transforms
from Model_Class_From_the_Scratch import MODEL_From_Scratch


class Classifier() :
    def __init__(self, model_name) :
        self.script_dir = os.path.dirname(os.path.abspath(__file__)) + '\\';

        USE_CUDA = torch.cuda.is_available();
        self.DEVICE = torch.device("cuda" if USE_CUDA else "cpu");

        self.label_map = np.loadtxt(self.script_dir+"label_map.txt", str, delimiter='\t')
        num_classes = len(self.label_map)

        self.model = MODEL_From_Scratch(num_classes).to(self.DEVICE);
        self.transform_info = transforms.Compose([
                transforms.Resize(size=(224, 224)),
                transforms.ToTensor()
                ])
        
        model_str = model_name
        self.model.load_state_dict(torch.load(model_str, map_location=self.DEVICE))
        self.model.eval()

    def classify(self, frame) :
        opencv_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(opencv_rgb)
        image_tensor = self.transform_info(image)
        image_tensor = image_tensor.unsqueeze(0)
        image_tensor = image_tensor.to(self.DEVICE)
        inference_result = self.model(image_tensor)
        inference_result = inference_result.squeeze()
        inference_result = inference_result.detach().numpy()

        return self.label_map, inference_result;
