import os
import glob
from tqdm import tqdm
import xml.etree.ElementTree as ET

def read_file(path_file):
    file_name = path_file.split("/")[-1].split(".")[0]+".txt"
    root = ET.parse(path_file)
    for i in range(len(root.getroot()[0])):
        label = root.getroot()[0][i][0].text
        seg = root.getroot()[0][i][1].text
        content_file = (seg.replace("\n","").replace("\t","")+",####"+label.replace("\n","").replace("\t","")+"\n")
        f = open("label_train/"+file_name,"a")
        f.write(content_file)
for path in tqdm(glob.glob("data/train/train_labels/*")):
    read_file(path)