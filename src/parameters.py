import os

SEED = 666

ROOT = "/home/akash/CourseWork/chanakya/"
DATASET_NAME = "AccidentPrediction"
DATASET_PATH = os.path.join(ROOT, "dataset/train/")
MODELS_PATH = os.path.join(ROOT, "models/")

TRAIN_CLASSES = ["Accident"]
NORMAL_CLASS="Normal"

FEATURES_FILE = os.path.join(MODELS_PATH, "features.npy")
LABELS_FILE = os.path.join(MODELS_PATH, "labels.npy")

"""
# Feature Parameters
> For resizing the video frame dimension to a fixed size that is workable.
"""
IMAGE_WIDTH = 92
IMAGE_HEIGHT = 92
IMAGE_DIMENSION = (IMAGE_WIDTH, IMAGE_HEIGHT)
# Extracts a total of `SEQUENCE_LENGTH` number of frames form every video \
#    (sample) at every equal interval.
SEQUENCE_LENGTH = 40
# dataset partitions
TRAIN_TEST_SPLIT = 0.20
TRAIN_VALID_SPLIT = 0.20

# early stopping callback parameters
EARLY_STOPPING_CALLBACK_MONITOR = "val_loss"
EARLY_STOPPING_CALLBACK_MIN_DELTA = 0.001
EARLY_STOPPING_CALLBACK_PATIENCE = 15

# optimizer parameters
LEARNING_RATE = 0.001

# training parameters
EPOCHS = 80
BATCH_SIZE = 15
