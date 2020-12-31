import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image
import tensorflow_hub as hub
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# mobilenet_v2
def get_image_classifier():
    url = 'https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4'

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Input(shape=[224, 224, 3]))
    model.add(hub.KerasLayer(url))
    model.summary()

    labels_path = tf.keras.utils.get_file(
        'ImageNetLabels.txt',
        'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt'
    )

    # labels = open(labels_path).read().split()       # 두 단어로 된 레이블이 있어서 실패
    # labels = open(labels_path).read().split('\n')   # 마지막에 빈 줄 있어서 실패
    # print(labels[:3], labels[-3:])                  # ['background', 'tench', 'goldfish'] ['ear', 'toilet tissue', '']
    # print(len(labels))                              # 1002

    labels = open(labels_path).read().splitlines()
    # print(len(labels))                              # 1001
    # labels = open(labels_path).readlines()          # 개행문자 포함
    # labels = [w.strip() for w in labels]
    # print(labels)       # ['background', 'tench', 'goldfish', ...]

    return model, np.array(labels)


def classify_image():
    img_url = 'https://storage.googleapis.com/download.tensorflow.org/example_images/grace_hopper.jpg'
    img_path = tf.keras.utils.get_file('grace_hopper.jpg', img_url)
    # print(img_path)       # /Users/jeonghoonkim/.keras/datasets/grace_hopper.jpg

    # 문제
    # 다운로드한 이미지를 그래프로 그려보세요
    img_hopper = Image.open(img_path).resize([224, 224])
    # print(img_hopper)       # <PIL.Image.Image image mode=RGB size=224x224 at 0x7F983C17BC50>

    # plt.imshow(img_hopper)
    # plt.show()

    array_hopper = np.array(img_hopper)
    print(array_hopper.shape)   # (224, 224, 3)

    plt.subplot(1, 2, 1)
    plt.title('original')
    plt.imshow(array_hopper)

    print(np.min(array_hopper), np.max(array_hopper))   # 0 255

    scaled_hopper = array_hopper / 255          # minmax scaling
    # scaled_hopper = array_hopper / 510
    # scaled_hopper = array_hopper / 127

    model, labels = get_image_classifier()
    # preds = model.predict([array_hopper])             # error
    # preds = model.predict(array_hopper[np.newaxis])
    # preds = model.predict(array_hopper.reshape(1, 224, 224, 3))
    # print(preds.shape)              # (1, 1001)
    #
    # preds_arg = np.argmax(preds[0])
    # print(preds_arg, labels[preds_arg])     # 722 pillow

    preds = model.predict(scaled_hopper.reshape(1, 224, 224, 3))
    preds_arg = np.argmax(preds[0])
    print(preds_arg, labels[preds_arg])     # 653 military uniform

    plt.subplot(1, 2, 2)
    plt.title('scaled: {}'.format(labels[preds_arg]))
    plt.imshow(scaled_hopper)
    plt.show()


# 문제
# 제너레이터를 사용해서 꽃 데이터 32개를 예측하세요
def classify_by_generator():
    img_url = 'https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz'
    img_path = tf.keras.utils.get_file('flower_photos', img_url, untar=True)
    # print(img_path)       # /Users/jeonghoonkim/.keras/datasets/flower_photos

    data_gen = ImageDataGenerator(rescale=1/255)

    batch_size = 32
    data_flow = data_gen.flow_from_directory(
        img_path,
        batch_size=batch_size,
        target_size=(224, 224),
        class_mode='sparse'
    )

    # for take in data_flow:
    #     print(type(take), len(take))        # <class 'tuple'> 2

    # for xx, yy in data_flow:
    #     print(xx.shape, yy.shape)           # (32, 224, 224, 3) (32,)

    xx, yy = data_flow.next()
    # print(xx.shape, yy.shape)               # (32, 224, 224, 3) (32,)

    model, labels = get_image_classifier()
    preds = model.predict(xx)
    print(preds.shape)          # (32, 1001)

    preds_arg = np.argmax(preds, axis=1)
    print(preds_arg)            # [946 884 717 986 986 320 ...]
    print(labels[preds_arg])    # ['bell pepper' 'vase' 'picket fence' 'daisy' ...]
    print(yy[:5])               # [3. 4. 1. 1. 0.]

    # 문제
    # 예측 결과를 한 줄에 8개씩 4줄에 피겨 1개에 그려주세요
    # 예측에 사용한 이미지를 출력하고, 그 위에 예측한 레이블을 출력합니다

    for i, (img, pred) in enumerate(zip(xx, preds_arg)):
        # print(i, img.shape, pred)
        plt.subplot(4, 8, i+1)
        plt.title(labels[pred])
        plt.axis('off')
        plt.imshow(img)

    plt.show()


# classify_image()
classify_by_generator()


# 아래 에러가 발생했을 때의 해결책
# OSError: SavedModel file does not exist at:
# C:\Users\308\AppData\Local\Temp\tfhub_modules\426589ad685896ab7954855255a52db3442cb38d/{saved_model.pbtxt|saved_model.pb}

# 원인 (아래 폴더는 가져온 모델이 사용하는 폴더로 항상 동일)
# 426589ad685896ab7954855255a52db3442cb38d 폴더에 파일이 생성되지 않음

# 해결책
# 정상적으로 생성된 해당 폴더를 복사해서 붙여넣기

# 폴더 위치 (308은 사용자 id)
# C:\Users\308\AppData\Local\Temp\tfhub_modules
