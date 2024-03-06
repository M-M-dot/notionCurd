
## 安装
1. 新的conda 环境 
centos
```
mkdir -p ~/miniconda3 
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```
检查是否安装好了
```
conda --version 
```
建立并启用新环境
```
conda create --name myenv python=3.8
conda activate myenv
```
退出环境
```
conda deactivate
```
安装需要的包
```
conda install request,json
conda install json
```

## 操作
定义数据库, "properties" 的参数定义参考：["properties"参数定义文档参考][properties-def-link]
，[使用案例](create_database.py)
向数据库中插入一个条目,[使用案例](addpage_database2.py),["properties"参数值文档参考][properties-value-link]

[properties-value-link]: https://developers.notion.com/reference/property-value-object#number-property-values
[properties-def-link]: https://developers.notion.com/reference/property-object  




