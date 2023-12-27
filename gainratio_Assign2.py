import math

def calc_entropy(data):
    """to calculate the entropy of a given dataset."""
    num_instances = len(data)
    label_counts = {}
    for instance in data:
        label = instance[1] #we have taken index 1 in order to use the age attribute
        if label not in label_counts:
            label_counts[label] = 0
        label_counts[label] += 1
    entropy = 0.0
    for label in label_counts:
        probability = float(label_counts[label]) / num_instances
        entropy -= probability * math.log2(probability)
    return entropy

def calc_info_gain(data, attr_index):
    """to calculate the information gain of a given attribute in the dataset."""
    total_entropy = calc_entropy(data)
    attr_values = {}
    for instance in data:
        attr_value = instance[attr_index]
        if attr_value not in attr_values:
            attr_values[attr_value] = []
        attr_values[attr_value].append(instance)
    attr_entropy = 0.0
    intrinsic_value = 0.0
    for attr_value in attr_values:
        attr_instances = attr_values[attr_value]
        attr_probability = len(attr_instances) / len(data)
        attr_entropy += attr_probability * calc_entropy(attr_instances)
        intrinsic_value -= attr_probability * math.log2(attr_probability) if attr_probability != 0 else 0
    if intrinsic_value == 0:
        return 0
    info_gain = total_entropy - attr_entropy
    gain_ratio = info_gain / intrinsic_value
    return gain_ratio


def majority_label(data):
    """to get the majority label in the dataset."""
    label_counts = {}
    for instance in data:
        label = instance[-1] #class
        if label not in label_counts:
            label_counts[label] = 0
        label_counts[label] += 1
    majority_label = max(label_counts, key=label_counts.get)
    return majority_label

def create_decision_tree(data, attributes):
    """we are creating a decision tree recursively using the ID3 algorithm."""
    labels = [instance[-1] for instance in data]
    
    # Base case 1: All instances have the same label
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    
    # Base case 2: No more attributes to split on
    if len(attributes) == 0:
        return majority_label(data)
    
    best_attr_index = 0
    best_gain_ratio = 0.0
    
    # Calculate gain ratio for each attribute
    for i in range(len(attributes)):
        gain_ratio = calc_info_gain(data, i)
        if gain_ratio > best_gain_ratio:
            best_gain_ratio = gain_ratio  #the attribute with the maximum gain ratio is selected as the splitting attribute
            best_attr_index = i
    
    best_attr = attributes[best_attr_index]
    tree = {best_attr: {}}
    remaining_attributes = attributes[:best_attr_index] + attributes[best_attr_index+1:]
    attr_values = set([instance[best_attr_index] for instance in data])
    
    # Recursive construction of subtrees
    for attr_value in attr_values:
        attr_instances = [instance for instance in data if instance[best_attr_index] == attr_value]
        tree[best_attr][attr_value] = create_decision_tree(attr_instances, remaining_attributes)
    
    return tree

data=[
    ['1',   'youth',	    'high',     'no',	'fair',	        'no' ],
    ['2',	'youth',	    'high',     'no',	'excellent',	'no' ],
    ['3',	'middle aged',	'high',	    'no',	'fair',	        'yes'],
    ['4',	'senior',	    'medium',   'no',	'fair',	        'yes'],
    ['5',	'senior',	    'low',	    'yes',	'fair',	        'yes'],
    ['6',	'senior',	    'low',	    'yes',	'excellent',	'no' ],
    ['7',	'middle aged',	'low',	    'yes',	'excellent',	'yes'],
    ['8',	'youth',	    'medium',	'no',	'fair',     	'no' ],
    ['9',	'youth',	    'low',	    'yes',	'fair',     	'yes'],
    ['10',	'senior',	    'medium',	'yes',	'fair',	        'yes'],
    ['11',	'youth',	    'medium',	'yes',	'excellent',	'yes'],
    ['12',	'middle aged',	'medium',	'no',	'excellent',	'yes'],
    ['13',	'middle aged',	'high',	    'yes',	'fair',	        'yes'],
    ['14',	'senior',	    'medium',	'no',	'excellent',	'no' ]
]

attributes=['rid','age','income','student','credit_rating','buys_computer']

decision_tree = create_decision_tree(data, attributes)
print(decision_tree)