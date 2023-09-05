import os
import openai
import time
import json
from tqdm import tqdm


openai.api_key = "insert key here"

read_path = "./class_descrs/cifar/s2_unseen_classes/cifar_classnames_notemplate.labels"
WRITE_PATH = "./openai_descrs/desc.json"

def list_of_classnames(file):
    classname_list = []
    # This function will open the file, and take the classname from each line, and give a list of all classnames
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            dict = line.strip()
            # Here we load the text dictionary(which is a json) into python
            get_text = json.loads(dict)
            classname_list.append(get_text['label'])
    return classname_list


def openai_descriptions(classnames):
    desc_dic = {}
    for classname in tqdm(classnames):
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"In 50-100 words, describe what features are typically present in an image of a {classname}. Do not say \"As an AI language model\" or similar disclaimers."}
        ],
        max_tokens=500
        )
        desc = completion.choices[0].message.content
        desc_dic[classname] = desc
        print(classname)
        # time.sleep(0.5)

    with open(WRITE_PATH, 'w') as fout:
        fout.write(json.dumps(desc_dic, indent=1))
    return desc_dic
        

classnames = list_of_classnames(read_path)
print()
print(openai_descriptions(classnames))

print()
