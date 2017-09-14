import sys,os,zipfile
def extract(path):
    for root,dirs,file in os.walk(path):
        for file_ in file:
            temp=os.path.join(root,file_)
            if 'zip' in temp.split('.'):
                z=zipfile.ZipFile(temp)
                z.extractall(temp.split('.')[0])
                z.close()
                extract(temp.split('.')[0])
                os.remove(temp)
if __name__=='__main__':
    extract(sys.argv[1])