import os,sys
class mega2:
    LOADED = False
    MEGANAME = ''
    offsets = []
    file_names = []
    data_main = []##filenames are assigned offsets
    def __init__(self,MEGA):
        if MEGA[-5:].upper() == '.MEGA':
            print('is')
        else:
            MEGA+='.MEGA'
            
        if os.path.isfile(MEGA) == True:
            self.load(MEGA)
        else:
            print('empty mega obj created!')
            self.writefile(MEGA,['1,,','test_entry,,','123456789'])#'New_MegaFile'
            self.load(MEGA)
            self.removefile('test_entry')
    ##usual
    def readfile(self,fname):
        print('reading file:'+str(fname))
        try:
            f = open(fname,'r')
            data = f.readlines()
            f.close()
        except:
            try:
                f.close()
            except:
                print('error/file already closed!')
        return data

    def writefile(self,fname,dat,ARRAY = True):
        print('writing to:'+str(fname))
        try:
            f = open(fname,'w')
            if ARRAY == True:
                for x in dat:
                    f.write(str(x)+'\n')
                    #print('ln=',x)
            else:
                f.write(dat)
            f.close()
        except:
            try:
                f.close()
            except:
                print('error/file already closed!')
                

    def array2csv(self,array):##from beelib
        temp = ''
        for fl in array:
            #print(fl)
            temp += str(fl)+','
        temp+=','
        return temp
    
    def csv2array(self,csvstr):##may need os.isfile() or whatever it is to check file is in dir before declaring eofsame for array2csv      ##from beelib
        arrayreturn = []
        temp = ''
        flag = False
        for x in csvstr:#range(len(csvnames)):
            if flag and (x==','):## ,, delimiter
                break
            if x ==',':
                arrayreturn.append(temp)
                temp = ''
                flag = True
            else:
                temp+=x
                flag = False
        return arrayreturn
    ##~~~~~
    ##MEGAFILEIO
    #utilites (will move to seperate)
    #pack is used for packing to a mega file
    def pack(self,files,Mname):
        offsets=[]
        file_names = []
        main_data = []
        temp = []
        if Mname[-5:].upper() == '.MEGA':
                pass
        else:
            Mname+='.MEGA'
            
        for dfiles in files:
            dat = self.readfile(dfiles)
            for x in range(len(dat)):
                dat[x] = dat[x].strip('\n')
                main_data.append(dat[x])##can probably remove this line
            file_names.append(dfiles)
            offsets.append(str(len(dat)))
        temp.append(self.csv2array(offsets))
        temp.append(self.csv2array(file_names))
        for x in main_data:
            temp.append(x)
        self.writefile(Mname,temp)
            
        #append data to file object
        #pack into mega

    #unpack creates directory in megafiles name and extracts contents
    def unpack(self,Mname):
        cwd = os.getcwd()
        #os.mkdir(
        #unpack mega to directory
        offsets = []
        file_names = []
        data_main = []##clear main
        offsettotal = 0
        Mname = self.megafilename_process(Mname)
        dat = self.readfile(str(Mname))#+'.MEGA')
        os.mkdir(str(Mname[:-5])+'_MEGA')
        os.chdir(str(Mname[:-5])+'_MEGA')
        offsets = self.csv2array(dat[0].strip('\n'))
        file_names = self.csv2array(dat[1].strip('\n'))
        for x in range(2,len(dat)):
            data_main.append(dat[x].strip('\n'))
            
        for y in range(len(file_names)):
            temp = []
            for z in range(offsettotal,(offsettotal+int(offsets[y]))):
                temp.append(data_main[z])
            self.writefile(file_names[y],temp)
        os.chdir(cwd)

        
    #adds file to mega and saves it 
    def pack_file(self,filename,Mname):
        MEGAFILE  = mega2(Mname)
    #extracts the specified file from a megafile on disk
    def unpack_file(self,fname,Mname):
        pass
##        offsets = []
##        file_names = []
##        data_main = []##clear main
##        if Mname[-5:].upper() == '.MEGA':
##                pass
##        else:
##            Mega+='.MEGA'
##        self.MEGANAME = Mega
####        if Mega[-5:].upper() == '.MEGA':
####            dat = self.readfile(Mega)
####        else:
####            
##        dat = self.readfile(str(Mega))#+'.MEGA')
##        self.offsets = self.csv2array(dat[0].strip('\n'))
##        self.file_names = self.csv2array(dat[1].strip('\n'))
##        self.data_main = []##clear main
##        for x in range(2,len(dat)):
##            self.data_main.append(dat[x].strip('\n'))

    def make_mega(self,files,Mname):##files in array
        offsets = []
        file_names = []
        data_main = []
        megacache = []##will optimise later
        Mname = self.megafilename_process(Mname)

        file_names = files
        for file in files:##each file
            
            dat = self.readfile(file)
            for x in range(len(dat)):
                dat[x] = dat[x].strip('\n')##writefile replaces this stripped newlinechar
                data_main.append(dat[x])
            offsets.append(len(dat))
        megacache.append(self.array2csv(offsets))
        megacache.append(self.array2csv(file_names))
        for x in data_main:
            megacache.append(x)
        self.writefile(Mname,megacache)
            
            
        
        
    ##MEGAFILE VDIR
    #peek()
    #peeks the file contents of the megafile loaded as vdir
    def load(self,Mega):##loads new megafile into object
        Mega = self.megafilename_process(Mega)
        if os.path.isfile(Mega):
            
            self.offsets = []
            self.file_names = []
            self.data_main = []##clear main
            self.LOADED = True
            self.MEGANAME = Mega
    ##        if Mega[-5:].upper() == '.MEGA':
    ##            dat = self.readfile(Mega)
    ##        else:
    ##            
            dat = self.readfile(str(Mega))#+'.MEGA')
            self.offsets = self.csv2array(dat[0].strip('\n'))
            self.file_names = self.csv2array(dat[1].strip('\n'))
            self.data_main = []##clear main
            for x in range(2,len(dat)):
                self.data_main.append(dat[x].strip('\n'))
            ##check for the test entry if there is only one entry that is the test entry
            if str(len(self.peek())) == '1':
                if 'test_entry' in self.peek():
                    if self.fetch('test_entry') == ['123456789']:
                        print('Test entry detected, removing..')
                        self.removefile('test_entry')
    def reload(self):#reloads current megafile data
        if self.isloaded()== True:
            self.load(self.MEGANAME)
        
    def save(self):##saves current object 2disk as megafile(loaded name)
        if self.isloaded() == True:
            dat = [str(self.array2csv(self.offsets)),str(self.array2csv(self.file_names))]##edit remived newline
            for x in self.data_main:
                dat.append(str(x))#+'\n')##dont need added by save(\n)
            print('writing\n',dat)
            self.writefile(self.MEGANAME,dat)
            
    def saveas(self,Mname):##saveas newmega
        if self.isloaded() == True:
            Mname = self.megafilename_process(Mname)
            dat = [str(self.array2csv(self.offsets))+'\n',str(self.array2csv(self.file_names))+'\n']
            for x in self.data_main:
                dat.append(str(x)+'\n')
            self.writefile(Mname,dat)
        
    def saveas_reload(self,Mname):##saveas then reload as the new mega
        if self.isloaded() == True:
            self.saveas(Mname)
            self.MEGANAME = Mname
            self.load(Mname)
        
    def addfile(self,file):##add new file to mega
        if self.isloaded() == True:
            if file  not in self.file_names:
                dat = self.readfile(file)
                for x in range(len(dat)):
                    dat[x] = dat[x].strip('\n')##writefile replaces this stripped newlinechar
                    self.data_main.append(dat[x])
                self.offsets.append(len(dat))
                self.file_names.append(file)
            else:
                print('cannot add file to open mega as file already exists!')
    def adddata(self,fdat):##allows for adding data as 'file' manually from within a program without crating a file to read [file,[data]]
        if self.isloaded() == True:
            if fdat[0]  not in self.file_names:
                dat = fdat[1]
                for x in range(len(dat)):
                    dat[x] = dat[x].strip('\n')##writefile replaces this stripped newlinechar
                    self.data_main.append(dat[x])
                self.offsets.append(len(dat))
                self.file_names.append(fdat[0])
            else:
                print('cannot add fake file to open mega as file already exists!')
            
    def replacefile(self,file):##finds file data,recalculates offsets then appends data
        if self.isloaded() == True:
            self.removefile(file)##moved code to removefile
            ##adding file data to file(could use add?)
            self.addfile(file)
    def replacedata(self,fdat):##finds file data,recalculates offsets then appends data
        if self.isloaded() == True:
            self.removefile(fdat[0])##moved code to removefile
            ##adding file data to file(could use add?)
            self.adddata(fdat[0],fdat[1])
    
    def removefile(self,file):##remove file from mega
        print(self.isloaded(),',',file in self.file_names)
        if self.isloaded() == True:
            if file in self.file_names:##if loaded and exists
                print('is')
                offsetstart = 0
                offset = int(self.offsets[self.file_names.index(file)])##finds offset data of file
                file_data = []##for holding new data
                offset_data = []##for holding offset data
                for x in range(0,self.file_names.index(file)):#self.file_names.index(file)):##add offsests to get starting line
                    offsetstart +=int(self.offsets[x])
                    #offset +=1
        ##        for x in range(offsetstart,(offsetstart+offset)):#appends data to buffer for returning(optimise by returning entries by number form the main instead)
        ##            file_data.append(self.data_main[x])
        ##            #print(offset,'.',offsetstart)
                    
                for x1 in range(0,offsetstart):##copies first half
                    file_data.append(self.data_main[x1])
                for x2 in range((offsetstart+offset),len(self.data_main)):
                    file_data.append(self.data_main[x2])
                    
                for y1 in range(len(self.file_names)):
                    if y1 == self.file_names.index(file):##ignore entry associated with filename
                        pass
                    else:
                        offset_data.append(self.offsets[y1])
                ##update values
                self.offsets = offset_data
                self.data_main = file_data
                self.file_names.remove(file)
    
    def peek(self):##returns filenames from megafile
        if self.isloaded() == True:
            return self.file_names
    
    def fetch(self,file):##fetches data from internal megadata object
        if self.isloaded() == True:
            offsetstart = 0
            offset = int(self.offsets[self.file_names.index(file)])##finds offset data of file
            file_data = []
            for x in range(0,self.file_names.index(file)):#self.file_names.index(file)):##add offsests to get starting line
                offsetstart +=int(self.offsets[x])
                #offset +=1
            for x in range(offsetstart,(offsetstart+offset)):#appends data to buffer for returning(optimise by returning entries by number form the main instead)
                file_data.append(self.data_main[x])
                #print(offset,'.',offsetstart)
            return file_data
        
    def close(self):##wipes object
        self.offsets = []
        self.file_names = []
        self.data_main = []##clear main
        self.LOADED = False
        
    def clear(self):##clears object data
        self.offsets = []
        self.file_names = []
        self.data_main = []##clear main
        
    
    def isloaded(self):
        return self.LOADED
    
    def megafilename_process(self,Mfile):##processes megfile name and changes if nessecary
        if Mfile[-5:].upper() == '.MEGA':
            pass
        else:
            Mfile+='.MEGA'
        return Mfile
        
        
        

    #responsible for actually loading the megafile and setting up the object
    def internal_vdir(self):##extracts files into mega object
        pass

    #debug
    def dumpall(self,DATA = False):
        print(self.offsets,'\n',
        self.file_names)
        if DATA == True:
            print(self.data_main)
    #def qq(self):
        #pass
    def emu_addfile(self,file):##add new file to mega
        if file  not in self.file_names:
            dat = self.readfile(file)
            print('DATA-~-~\n\n')
            for x in range(len(dat)):
                dat[x] = dat[x].strip('\n')##writefile replaces this stripped newlinechar
                print(dat[x],'\n\n')
            print('len = ;',len(dat))
            print('name:',str(file))
        else:
            print('cannot add file to open mega as file already exists!')
    
#main = mega2('test')
#main.load('testing')
