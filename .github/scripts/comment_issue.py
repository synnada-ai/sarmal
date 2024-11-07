import sys
import yaml # type[ignore]
import subprocess

# Load labels from GitHub Action input
labels = sys.argv[1].split(',')
number = sys.argv[2]
body = sys.argv[3]

# Load the label-user mapping from the YAML file
with open('.github/label_to_devs.yml', 'r') as file:
    label_user_mapping = yaml.safe_load(file)

print("Body:", body)
print()
print(labels)
print()
print(number)
# Find reviewers based on labels
# for label in labels:
#     reviewers = set()
#     label = label.strip()
#     if label in label_user_mapping:
#         reviewers.update(label_user_mapping[label])
#     if reviewers:
#         prefix_arg = "gh pr edit --add-assignee "
#         reviewers_arg = "".join(f"{reviewer} " for reviewer in reviewers)
#         arg = prefix_arg + reviewers_arg
#         subprocess.run(arg, shell=True)
            
