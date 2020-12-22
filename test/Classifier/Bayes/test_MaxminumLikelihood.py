from unittest import TestCase

from main.Classifier.Bayes.GaussianNB import GaussianNB
import pandas as pd


class Test(TestCase):
    def setUp(self) -> None:
        df = pd.read_excel(r'D:\Development\focus\ML\data\Bayes.xlsx', engine='openpyxl')
        # split into the output and the input
        self.attributes = df.iloc[:, 1:4]
        self.labels = df.iloc[:, 0]

    def test_maximum_likelihood(self):
        bc = GaussianNB([0.5, 0.5], self.attributes, self.labels, 0.25)
        x_train, x_test, y_train, y_test = bc.leave_out()
        bc.train(x_train, y_train)
        print(bc.test(x_test, y_test))

