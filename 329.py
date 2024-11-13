# try to open and write to file that is not writable

try:
    f = open("demo file.txt")
    try:
        f.write("lorum ipsum")
    except:
        print("somthing went wrong when writing to the file")
    finally:
        f.close()
except:
    print("somthing went wrong when opening the file")
    