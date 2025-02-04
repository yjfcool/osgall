
from ._common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("boost" , list_name,getDependency)
    
    return list_name + [str_name]
    
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):
    # print(str_name)
    
    # if(b_only_download):
        # download_source(str_name,"https://github.com/eigenteam/eigen-git-mirror.git")
    
        # return
        
    STR_CFG = ''
    STR_CFG += ' -DBUILD_TESTING=0'
    STR_CFG += ' -DEIGEN_BUILD_BTL=0'
    # if(dict_config['static']):
        # STR_CFG += ''
    # else:
        # STR_CFG += ''
    
    if(dict_config['arch']=="unix"):
        return #error for -lpthreads
    
    # source_dir = os.getcwd() + '/../prebuild/eigen-eigen-5a0156e40feb'
    source_dir = os.getcwd() + '/../prebuild/eigen-3.4-rc1'
    
    configure(str_name,dict_config,STR_CFG,"",source_dir)
    build(str_name,dict_config)
    install(str_name,dict_config)
    
    