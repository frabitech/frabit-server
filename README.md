# frabit-server
![PyPI - License](https://img.shields.io/github/license/frabitech/frabit-server)
![lang](https://img.shields.io/pypi/pyversions/frabit-server)
[![status](https://img.shields.io/pypi/status/frabit-server)](https://github.com/frabitech/frabit-server/releases)
[![pypi](https://img.shields.io/pypi/v/frabit-server)](https://github.com/frabitech/frabit-server/releases)
[![Upload Python Package](https://github.com/frabitech/frabit-server/actions/workflows/python-publish.yml/badge.svg)](https://github.com/frabitech/frabit-server/actions/workflows/python-publish.yml)
[![CI](https://github.com/frabitech/frabit-server/actions/workflows/main.yml/badge.svg)](https://github.com/frabitech/frabit-server/actions/workflows/main.yml)

## 一个通过gRPC协议远程操作frabit的编排器，也是frabit系列的核心组件
## 部署

- **pip安装(推荐)**
  ```bash
  shell> pip install frabit-server 
  or
  shell> pip3 install frabit-server 
  ```


 - 源码安装
   ```bash
   # 从github下载源码
   shell> git clone https://github.com/frabitech/frabit-server.git
   
   # 创建虚拟环境 
   shell> virtualenv venv
   shell> source venv/bin/activate
   (ven) shell>
   # 安装依赖
   (ven) shell> pip install -r requirements.txt 
   # 修改配置文件
   (ven) shell> vim /etc/frabitd.cnf
   # 启动服务
   (ven) shell> start.sh
   ```


## 功能

 - 备份信息查看

 - 备份实例管理

 - 备份恢复

 - 在线支持

## 文档

[简体中文](docs/zh/README.md)

[English](docs/en/README.md)
