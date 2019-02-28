import sys,os,time , keyboard , datetime
import subprocess

month=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def odczyt_pl(lokalizacja,typ='r'):
    plik = open(lokalizacja,typ, encoding="utf-8")
    try:
        tekst=plik.read()
    finally:
	    plik.close()
    return tekst

def komOS(komenda):
    os.system(komenda+" > out.txt")
    return odczyt_pl('out.txt')

def komS(komenda):
    p = subprocess.Popen(komenda, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    return output

def lsFile(dirname):
    a=[f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, f))]
    return a

def moveFile(adres,newPlace):
    komS('mv -f '+adres+' '+newPlace)

def removeFolder(adres):
    komS('rm -rf '+adres)

def aktMonth():
    today = str(datetime.date.today());
    year = int(today[:4]);
    month = int(today[5:7]);
    return  month

def calldate():
    p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    print ("Today is", output)


def main():
 print(komS("date"))

 #komS("ls")
 fold="/mnt/disk1/PUB/"
 input=fold+"input/" ;     print("input=",input)
 miech=komS("date").decode()[4:7]  ; print(miech)
 day=komS("date").decode()[8:10].strip()   ; print(day)
 print(fold+miech+day,os.path.isdir(fold+miech+"/"+day))
 while (True):
    data   =komS("date").decode()
    miech  =data[4:7]
    day    =data[8:10].strip()
    dayFold=fold+miech+"/"+day
    x=month.index(miech)    # jaki index <miech>
    if os.path.isdir(fold+miech)==False:
       os.mkdir(fold+miech); y=x-2 # make folder <miech> if not exist
       if (y<0): y=11-x
       if os.path.isdir(fold+month[y]): komS('rm -rf '+fold+month[y])   # remove 2 month old folder
    if os.path.isdir(dayFold)==False:
       os.mkdir(dayFold); m=x-1;   #  make folder <day> if not exist
       if m<0: m=11
       if os.path.isdir(fold+month[m]+"/"+day):
          komS('rm -rf '+fold+month[m]+"/"+day)
    inp=lsFile(fold+"input")
    if len(inp)>0:
     print(len(inp)," files to ",dayFold)
     for plk in inp:
       moveFile(input+plk,dayFold)
    time.sleep(5); print("sleep")


if __name__ == '__main__':
    main()
