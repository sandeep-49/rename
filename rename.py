import os


# Folder path or dir where files are present.
filepath = ''
orgList = os.listdir(filepath)


# Pattern to split filename string and grab the required part.
pattern = ' - '


# List to store the required filename string.
newFilename = []


# Main Function for renaming.
def main():
    for count, name in enumerate(orgList):
        newFilename.append(name.split(pattern)[1])
        src = filepath + name
        dst = filepath + newFilename[count]
        os.rename(src, dst)


# Driver Code
if __name__ == '__main__':
    main()