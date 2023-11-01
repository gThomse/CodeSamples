import os
# Uses Recursion

# Assumes Windows 10, and start of file sructure is the Documents directory (under each user

def fle_find(name, path, i):

    for r, d, f in os.walk(path):
        for n_ in f:
            if n_ == name:
                return os.path.join(r, name)

        for d_ in d:
            fnd = fle_find(name,os.path.join(r,d_), i+1)
            if name in str(fnd).split("\\"):
                return fnd
        return

def find_doc_path():
    path_lst = os.getcwd().rsplit("\\",os.getcwd().count("\\")-2)
    doc_path = path_lst[0]
    for _ in path_lst:
        if _ == path_lst[0]:
            continue
        if _ == "Documents":
            return os.path.join(doc_path, _)
        else:
            doc_path = os.path.join(doc_path,_)