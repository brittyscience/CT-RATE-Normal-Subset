import pandas as pd

# Load the CT-RATE training dataset
train = pd.read_csv("train_predicted_labels.csv")

# Preview the first five rows
print(train.head())

# Check the number of rows and columns
print(train.shape)

# Select all columns except VolumeName
labels = train.drop(columns=["VolumeName"])

# Check the number of label columns
print(labels.shape)

#checks which values equals to 0 and whether it is true (=0) 
# across each rows and axis check for columns within each row.
normal_mask = (labels == 0).all(axis=1)

# print results, first ten rows this is boolean mask.
print(normal_mask.head(10))

#if I want the entire rows to print, this is the code
# print(normal_mask.sum())

# Next, count how many CT volumes has 18 labels equal to 0
normal_count = normal_mask.sum()

print("Number of normal training volumes:", normal_count)

#Find the percentage
normal_percentage = (normal_count / len(train)) * 100

print("Percentage of normal volumes:", round(normal_percentage, 2), "%")

#Now, need to check validation dataset, same procedure as above

valid = pd.read_csv("valid_predicted_labels.csv")

#remove the identifier, volumename from the validation data

valid_labels = valid.drop(columns=["VolumeName"])

# Again, identify the normal CT scan using boolean mask 

valid_normal_mask = (valid_labels == 0).all(axis=1)

# Now, count the number of dataset that equals to 0 

valid_normal_count = valid_normal_mask.sum()

print("Number of normal validation volumes:", valid_normal_count)



