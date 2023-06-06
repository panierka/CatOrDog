from werkzeug.datastructures import FileStorage
import classifiers.neuralclassifier as clf


def classify(image: FileStorage):
    return clf.predict(image)
