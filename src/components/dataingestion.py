import pandas as pd
import glob
import os

class FileProcessor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = glob.glob(os.path.join(folder_path, '*'))

    def process_files(self):
        for file in self.files:
            print(f"Processing file: {file}")
            df = pd.read_csv(file)
            print(df)
            print(f"Filename: {os.path.basename(file)}")

folder_path = r'C:\Users\febaj\Downloads\ft_03-07-24_04-07-24_4G_12Bit_pre_28Hz'
processor = FileProcessor(folder_path)
processor.process_files()
