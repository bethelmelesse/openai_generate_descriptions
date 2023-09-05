import json

read_path = "./class_descrs/cifar/s2_unseen_classes/cifar_classnames_notemplate.labels"

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



def wirte_list_to_file(list):
    with open(r'openai_descrs/classnames.txt', 'w') as fp:
        for item in list:
            # write each item on a new line
            fp.write("%s\n" % item)
    print('Done')
    
classnames = list_of_classnames(read_path)
wirte_list_to_file(classnames)

print()