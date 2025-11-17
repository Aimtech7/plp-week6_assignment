import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import os
import pathlib

def create_model(num_classes=5, input_shape=(224, 224, 3)):
    model = keras.Sequential([
        layers.Rescaling(1./255, input_shape=input_shape),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])

    return model

def load_dataset(data_dir='./data', img_height=224, img_width=224, batch_size=32):
    data_dir = pathlib.Path(data_dir)

    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir / 'train',
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
        validation_split=0.2,
        subset='training'
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir / 'train',
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size,
        validation_split=0.2,
        subset='validation'
    )

    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

    return train_ds, val_ds, train_ds.class_names

def train_model(epochs=10, save_path='./models/recyclable_classifier.h5'):
    print("Loading dataset...")
    train_ds, val_ds, class_names = load_dataset()

    print(f"Classes: {class_names}")

    print("Creating model...")
    model = create_model(num_classes=len(class_names))

    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    print("Training model...")
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs
    )

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    model.save(save_path)
    print(f"Model saved to {save_path}")

    with open('./models/class_names.txt', 'w') as f:
        for class_name in class_names:
            f.write(f"{class_name}\n")

    return model, history

if __name__ == "__main__":
    model, history = train_model(epochs=10)
    print("Training completed successfully!")
