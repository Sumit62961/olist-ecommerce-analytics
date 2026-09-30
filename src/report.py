import numpy as np
import pandas as pd


class Report:
    def __init__(self):
        self.results = {}

    def add_result(self, name, result):
        self.results[name] = result

    def get_result(self, name):
        return self.results.get(name)

    def get_all_results(self):
        return self.results

    def clean_dictionary(self, result):
        cleaned = {}
        for key,value in result.items():
            if isinstance(value,dict):
                cleaned[key] = self.clean_dictionary(value)

            elif hasattr(value, "item"):
                cleaned[key] = value.item()

            else:
                cleaned[key] = value

        return cleaned

    def print_summary(self):
        for name, result in self.results.items():
            display_name = name.replace("_", " ").title()
            print(f"\n=== {display_name} ===")

            if isinstance(result, dict):
                result = self.clean_dictionary(result)

            elif isinstance(result, pd.DataFrame):
                print(result)
                continue

            elif isinstance(result,pd.Series):
                print(result)
                continue

            print(result)



