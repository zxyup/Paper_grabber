import time
class mdsolver:
    def __init__(self,filename):
        self.f = open(filename, "w")
        self.f.write('# '+filename[:-3]+'\n')
    
    def __del__(self):
        self.f.close
        
    def write_title(self,title):
        self.f.write('## '+title+'\n')
        
    def write_key(self,keys):
        for key in keys:
            self.f.write('### Keywords:'+key+'\n')
        
    def write_link(self,link):
        self.f.write('### [PDF](https://openreview.net'+link+')\n')
        
    def write_abs(self,abs):
        self.f.write('  ```'+abs+'```\n')
    
    # def write_from_opnote(self,sb):
    #     self.write_title(sb.content['title']['value'])
    #     self.write_key(sb.content['keywords']['value'])
    #     self.write_link(sb.content['pdf']['value'])
    #     self.write_abs(sb.content['abstract']['value'])
        
    def write_from_opnote(self,sb):
        title=sb.content['title']['value']
        keys=sb.content['keywords']['value']
        pdf=sb.content['pdf']['value']
        abs=sb.content['abstract']['value']
        self.f.write(f'## [{title}]({pdf}) [PDF]({pdf})\n')
        key_s='   '.join(keys)
        self.f.write(f'#### Keywords:  {key_s}\n')
        self.f.write('  ```'+abs+'```\n')
        time.sleep(0.1)
        
if __name__ == '__main__':        
    demo=mdsolver('demo.md')
