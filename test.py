import argparse
import joblib
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import NuSVC



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--test_data', type=str, default='testdataexample')
    parser.add_argument('-m', '--model', type=str, default='model')

    args = parser.parse_args()
    testData = args.test_data
    model = args.model


    f = open(testData,'r',encoding='utf-8')
    test = json.load(f)
    clf = joblib.load(model)
    res = clf.predict(test)
    f.close()
    f = open("output.txt",'a+',encoding='utf-8')
    for i in res:
        f.write(str(i))
        f.write("\n")
    f.close()