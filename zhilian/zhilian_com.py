from zhilian.save  import *
from zhilian.spider import *

if __name__=='__main__':
    pos_data,p=getalldata('北京','python',3)
    print(p)
    save_mysql('123.206.90.65','root','130129','zhilian',pos_data)