import tensorflow as tf
import numpy as np
import os
import shutil # copy

def make_dataset_folders(): # 폴더 생성
    def make_if_not(dst_folder):  # 부모폴더가 없으면 안됨(mkdir)
        if not os.path.exists(dst_folder):
            os.mkdir(dst_folder)  # 코드가 선명하다

    def make_if_not_2(dst_folder):  # 위에랑 똑같은데 부모폴더가 없어도 직접 만들어서 사용가능
        if not os.path.exists(dst_folder):
            os.makedirs(dst_folder)  # 폴더가 숨어서 헷갈릴수도 있다

    make_if_not('dogs_and_cats/small')

    make_if_not('dogs_and_cats/small/train')
    make_if_not('dogs_and_cats/small/validation')
    make_if_not('dogs_and_cats/small/test')

    make_if_not('dogs_and_cats/small/train/cat')
    make_if_not('dogs_and_cats/small/train/dog')
    make_if_not('dogs_and_cats/small/validation/cat')
    make_if_not('dogs_and_cats/small/validation/dog')
    make_if_not('dogs_and_cats/small/test/cat')
    make_if_not('dogs_and_cats/small/test/dog')

# make_dataset_folders()

# 문제
# 원본 train 폴더의 이미지를
# small/train에 1000개, small/validation에 500개, small/test에 500개 복사하세요.
# (파일 이름에 들어있는 규칙을 활용하세요)

# cat.0.jpg
# dog.0.jpg
def make_small_datasets():
    def copy_animals(kind,start,end,dst_folder):
        for i in range(start, end):
            filename = '{}.{}.jpg'.format(kind,i)

            # train에 있는것을 dst_folder로
            src_path = os.path.join('dogs_and_cats/train', filename)
            dst_path = os.path.join(dst_folder, filename)

            shutil.copy(src_path, dst_path)

    copy_animals('cat', 0, 1000, 'dogs_and_cats/small/train/cat')
    copy_animals('dog', 0, 1000, 'dogs_and_cats/small/train/dog')
    copy_animals('cat', 1000, 1500, 'dogs_and_cats/small/validation/cat')
    copy_animals('dog', 1000, 1500, 'dogs_and_cats/small/validation/dog')
    copy_animals('cat', 1500, 2000, 'dogs_and_cats/small/test/cat')
    copy_animals('dog', 1500, 2000, 'dogs_and_cats/small/test/dog')

# make_small_datasets()

def generator_basic():
    gen = tf.keras.preprocessing.image.ImageDataGenerator()

    flow = gen.flow_from_directory('dogs_and_cats/small/train',
                                   batch_size=7,
                                   target_size=(224,224),
                                   class_mode='binary')

    for i, (x,y) in enumerate(flow):
        print(x.shape, y.shape)
        print(y[:3])

        if(i >= 2):
            break

# generator_basic()

# d = {'name': 'kim', 'age':21}
# a = [d, d, d]
# # b = [d] * 3
# b = [{'name': 'kim', 'age':21}]*3 + [{'name': 'kim', 'age':21}]
# print(a)
# print(b)