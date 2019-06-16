import pandas as pd
import numpy as np


def merge_figure8_with_extracted_features(feature_path, annotation_path):

    features = pd.read_csv(feature_path)
    labels = pd.read_csv(annotation_path)

    merge = pd.merge(features, labels, on='Tweet_ID',  how='left')

    merge = merge[np.isfinite(merge['Crowd_Label'])]

    return merge

