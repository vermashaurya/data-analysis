import pandas as pd
from collections import Counter
from math import log2
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import graphviz

df = pd.read_csv('classifier.csv')
print("Original DataFrame:")
print(df)

age_bins = pd.cut(df['Age'], bins=3, labels=["Young", "Middle-aged", "Senior"])
na_k_bins = pd.cut(df['Na_to_K'], bins=3, labels=["Low", "Medium", "High"])
df['Age_group'] = age_bins
df['Na_to_K_group'] = na_k_bins
print("\nDataFrame after Binning:")
print(df)

def entropy(column):
    counts = Counter(column)
    total_count = len(column)
    probabilities = [count / total_count for count in counts.values()]
    return -sum([p * log2(p) for p in probabilities if p > 0])

entropies = {}
for column in df.columns[:-1]:
    entropies[column] = entropy(df[column])
    print(f"Entropy of {column}: {entropies[column]}")

total_entropy = entropy(df['Drug'])

info_gains = {}
for column in df.columns[:-1]:
    weighted_entropy = 0
    for value in df[column].unique():
        subset = df[df[column] == value]
        weighted_entropy += (len(subset) / len(df)) * entropy(subset['Drug'])
    info_gains[column] = total_entropy - weighted_entropy
    print(f"Information Gain of {column}: {info_gains[column]}")

max_info_gain_attribute = max(info_gains, key=info_gains.get)
print(f"\nThe max information gain is of this attribute: {max_info_gain_attribute}")

clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
X = df[['Age_group', 'Sex', 'BP', 'Cholesterol', 'Na_to_K_group']]
y = df['Drug']
X_encoded = pd.get_dummies(X)
clf.fit(X_encoded, y)

dot_data = tree.export_graphviz(clf, out_file=None,
                                feature_names=X_encoded.columns,
                                class_names=clf.classes_,
                                filled=True, rounded=True,
                                special_characters=True, proportion=False)

graph = graphviz.Source(dot_data)
graph.render("decisiontree")
graph.view()

print(f"The attribute '{max_info_gain_attribute}' provides the most information about the target variable 'Drug'.")
