import os
import random
import shutil

#splits data in the given path into train and test datasets
def generate_test_train_dataset(path,train_data_split = 0.8, test_data_split = 0.2):
    if(os.path.isdir(path)):
        img_names = os.listdir(path)
        num_images = len(img_names)
        train_data_len = int(num_images * train_data_split)
        test_data_len = int(num_images * test_data_split)
        train_data_indices = random.sample(range(0,num_images),train_data_len)
        #generates random indices for train dataset
        train_data_copy_dir = os.path.join(path,"train")		
        if not os.path.exists(train_data_copy_dir):
            os.makedirs(train_data_copy_dir)
        
        for file_name_index in train_data_indices:
            full_file_name = os.path.join(path, img_names[file_name_index])
            if (os.path.isfile(full_file_name)):
                shutil.move(full_file_name, train_data_copy_dir)
        #generates test dataset
        img_names = os.listdir(path)
        
        test_data_copy_dir = os.path.join(path,"test")		
        if not os.path.exists(test_data_copy_dir):
            os.makedirs(test_data_copy_dir)
        
        for file_name in img_names:
            full_file_name = os.path.join(path, file_name)
            if (os.path.isfile(full_file_name)):
                shutil.move(full_file_name, test_data_copy_dir)
    else:
        print("%s does not exist"%path)
				
generate_test_train_dataset("E:\\IUB MS\\Spring 2017\\Computer_Vision\\Assignment\\project\\data_preparation\\NewYorkCity")