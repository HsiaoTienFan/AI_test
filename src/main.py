import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import docopt
from sklearn.svm import SVC
from joblib import dump, load
from sklearn.model_selection import cross_val_score

def main():
    arguments = docopt.docopt(
            """AI document classifier

            Usage:
                main.py <inputs>...
                main.py (-r | --retrain) [-s=<S>] [-p=<P>]
                main.py (-v | --validate) [-f=<P>]
                main.py (-h | --help)
                main.py --version

            Options:
              -r --retrain                  Retrain model
              -s --seed=<S>                 The seed [default: 0]
              -p --percentage=<P>           Training data size as a percentage of all data [default: 0.8]
              -v --validate                 Perfrom cross-validation
              -f --folds=<F>                Number of folds for cross-validation [default: 5]
              -h --help                     Show this screen.
              --version                     Show version.

            """,
            version='AI document classifier'
            )


    if arguments['--retrain']:
        print("retrain")
        data = pd.read_csv("../data/t-data.csv")
        transformed_data = np.log(data[['pagesCount', 'wordCount', 'fileSize']])
        standardised_data = transformed_data.copy()
        standardised_data[:] = pd.DataFrame(preprocessing.StandardScaler().fit_transform(transformed_data[['pagesCount', 'wordCount', 'fileSize']]))
        standardised_data['category'] = data['category']
        
        X_train, X_test, y_train, y_test = train_test_split(standardised_data[['pagesCount', 'wordCount', 'fileSize']],
                                                            standardised_data['category'], test_size=float(arguments['--percentage']), random_state=int(arguments['--seed']))

        clf = SVC(gamma='auto', random_state=0)
        clf.fit(X_train, y_train)

        print("Accuracy of the model is {}".format(clf.score(X_test, y_test) * 100))

        dump(clf, '../model/model.joblib')

    if arguments['<inputs>']:
        inputs = pd.DataFrame(arguments['<inputs>'][0:3]).T
        clf = load('../model/model.joblib')
        preds = clf.predict(inputs)
        print("The document is predicted to be type '{}'".format(preds[0]))


    if arguments["--validate"]:
        print("validate")
        data = pd.read_csv("../data/t-data.csv")
        transformed_data = np.log(data[['pagesCount', 'wordCount', 'fileSize']])
        standardised_data = transformed_data.copy()
        standardised_data[:] = pd.DataFrame(preprocessing.StandardScaler().fit_transform(transformed_data[['pagesCount', 'wordCount', 'fileSize']]))
        standardised_data['category'] = data['category']

        clf = SVC(gamma='auto', random_state=0)
        scores = cross_val_score(clf, standardised_data[['pagesCount', 'wordCount', 'fileSize']], standardised_data['category'], cv=int(arguments['--folds']))
        print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


if __name__ == '__main__' :
    main()