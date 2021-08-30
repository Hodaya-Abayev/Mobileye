import numpy as np
from tensorflow.keras.models import load_model
def crop_images(red_points, green_points, img):
    crops = []
    for red_p in red_points:
        cropped_im = img.crop((red_p[0] - 40, red_p[1] - 40, red_p[0] + 41, red_p[1] + 41))
        crops.append({'image': cropped_im, 'color': 'red', 'point': red_p})
    for green_p in green_points:
        cropped_im = img.crop((green_p[0] - 40, green_p[1] - 40, green_p[0] + 41, green_p[1] + 41))
        crops.append({'image': cropped_im, 'color': 'green', 'point': green_p})
    return crops


def predict(crops):



    loaded_model = load_model("Model\model.h5")
    l_predictions = loaded_model.predict(np.asarray([np.asarray(crop['image']) for crop in crops]))
    return l_predictions


def get_treshold(predictions, crops):
    red_points = []
    green_points = []
    for index in range(len(predictions)):
        if predictions[index][1] >= 0.995:
            if crops[index]['color'] == 'red':
                red_points.append(crops[index]['point'])
            else:
                green_points.append(crops[index]['point'])
    return red_points, green_points







