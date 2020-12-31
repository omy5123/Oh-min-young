import tensorflow_datasets as tfds

# 오로지 사용법
def tfds_basic_1():
    names = tfds.list_builders()    # 실제로는 사용안할듯 실제로는 해당사이트에서 이름을 가져와서 사용
    print(names)                # ['abstract_reasoning', 'accentdb', 'aeslc', ...]
    print(len(names))           # 231
    print('-' * 30)

    imdb = tfds.load('imdb_reviews')    # 읽어오는방법은 이거하나
    print(imdb)
    print(type(imdb))           # <class 'dict'>
    print(imdb.keys())          # ['test', 'train', 'unsupervised']
    print()

    print(type(imdb['train']))  # <class 'tensorflow.python.data.ops.dataset_ops.PrefetchDataset'>
    print(imdb['train'])     # train안에 데이터들이 이와같은 형상을 띔 ->  # <PrefetchDataset shapes: {label: (), text: ()}, types: {label: tf.int64, text: tf.string}>
    print('-' * 30)

    # 문제
    # imdb 학습 데이터로부터 리뷰 2개만 출력하세요
    for take in imdb['train'].take(2):
        print(take)             # {'label': <tf.Tensor: shape=(), dtype=int64, numpy=0>, 'text': <tf.Tensor: shape=(), dtype=string, numpy=b"This was an absolutely terrible movie. Don't be lured in by Christopher Walken or Michael Ironside. Both are great actors, but this must simply be their worst role in history. Even their great acting could not redeem this movie's ridiculous storyline. This movie is an early nineties US propaganda piece. The most pathetic scenes were those when the Columbian rebels were making their cases for revolutions. Maria Conchita Alonso appeared phony, and her pseudo-love affair with Walken was nothing but a pathetic emotional plug in a movie that was devoid of any real meaning. I am disappointed that there are movies like this, ruining actor's like Christopher Walken's good name. I could barely sit through it.">}
        print(type(take))       # <class 'dict'>
        print(take['label'].numpy(), take['text'].numpy())
    print('-' * 30)

    for take in imdb['train'].take(2).as_numpy_iterator():
        print(take)
        print(take['label'], take['text'])


def tfds_basic_2():
    imdb, info = tfds.load('imdb_reviews', with_info=True)
    print(info)
    print(info.splits)
    # {'test': <tfds.core.SplitInfo num_examples=25000>,
    # 'train': <tfds.core.SplitInfo num_examples=25000>,
    # 'unsupervised': <tfds.core.SplitInfo num_examples=50000>}

    print(info.splits['train'])
    print(info.splits['train'].num_examples)    # 25000
    print('-' * 30)

    # cardinality쓰면 굳이 info 안해도됨
    print(imdb['train'])                        # <PrefetchDataset shapes: {label: (), text: ()}, types: {label: tf.int64, text: tf.string}>
    print(imdb['train'].cardinality())          # tf.Tensor(25000, shape=(), dtype=int64)
    print(imdb['train'].cardinality().numpy())  # 25000
    print('-' * 30)

    train_set, test_set = tfds.load('imdb_reviews', split=['train', 'test'])
    print(type(train_set))                      # <class 'tensorflow.python.data.ops.dataset_ops.PrefetchDataset'>

    # split 옵션에는 존재하는 키만 전달해야 한다
    # valid하면 오류
    # train_set, valid_set, test_set = tfds.load('imdb_reviews', split=['train', 'validation', 'test'])     # error

    # 할거면 이렇게
    # train_set, valid_set, test_set = tfds.load('imdb_reviews', split=['train', 'train', 'test'])
    train_set, valid_set, test_set = tfds.load('imdb_reviews', split=['train[:60%]', 'train[60%:]', 'test'])
    print(train_set.cardinality().numpy())      # 15000
    print(valid_set.cardinality().numpy())      # 10000
    print(test_set.cardinality().numpy())       # 25000


def tfds_basic_3():
    imdb_1 = tfds.load('imdb_reviews')
    print(type(imdb_1))         # <class 'dict'>
    print(imdb_1['train'])      # <PrefetchDataset shapes: {label: (), text: ()}, types: {label: tf.int64, text: tf.string}>

    for take in imdb_1['train'].take(2):
        print(type(take))       # <class 'dict'>
        print(take['label'])    # tf.Tensor(0, shape=(), dtype=int64)

    print('-' * 30)

    imdb_2 = tfds.load('imdb_reviews', as_supervised=True)  # as_supervised쓰는 이유? 모르겟음 검색
    print(type(imdb_2))         # <class 'dict'>
    print(imdb_2['train'])      # <PrefetchDataset shapes: ((), ()), types: (tf.string, tf.int64)>

    for take in imdb_2['train'].take(2):
        print(type(take))       # <class 'tuple'>
        print(take[1])          # tf.Tensor(0, shape=(), dtype=int64)

    print('-' * 30)

    for xx, yy in imdb_2['train'].take(2):
        print(xx.numpy())       # b"This was an absolutely
        print(yy.numpy())       # 0


tfds_basic_1()
# tfds_basic_2()
# tfds_basic_3()
