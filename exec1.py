import os
import datetime
import exec2
def  main():

    filename="test1"
    print(f"begin 5.22")
    if os.path.exists(filename):
        os.remove(filename)
        print(f"delete'{filename}'")

    currenttime=datetime.datetime.now().strftime("%Y-%m-%D:%h:%m:%S")
    with open(filename,"w",encoding="utf-8") as f:
        myanswer=exec2.answer()    
        f.write(myanswer)
        f.write(currenttime)
    print(f"create '{filename}'")

if __name__=="__main__": 
    main()