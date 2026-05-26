import os
import datetime
import exec2
import exec3
def  main():

    filename="test1"
    if os.path.exists(filename):
        os.remove(filename)
        print(f"delete'{filename}'")

    currenttime=datetime.datetime.now().strftime("%Y-%m-%d")
    with open(filename,"w",encoding="utf-8") as f:
        myanswer=exec2.answer()    
        f.write(myanswer)
        myanswer=exec3.answer()
        f.write(myanswer)
        f.write(currenttime)
    print(f"create '{filename}'")

if __name__=="__main__": 
    main()