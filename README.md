# frabit-server
![PyPI - License](https://img.shields.io/github/license/frabitech/frabit-server)
![size](https://img.shields.io/github/repo-size/frabitech/frabit-server)
![lang](https://img.shields.io/pypi/pyversions/frabit-server)
[![status](https://img.shields.io/pypi/status/frabit-server)](https://github.com/frabitech/frabit-server/releases)
[![downloads](https://img.shields.io/github/downloads/frabitech/frabit-server/total.svg)](https://github.com/frabitech/frabit-server/releases)
[![pypi](https://img.shields.io/pypi/v/frabit)](https://github.com/frabitech/frabit-server/releases)
[![Upload Python Package](https://github.com/frabitech/frabit-server/actions/workflows/python-publish.yml/badge.svg)](https://github.com/frabitech/frabit-server/actions/workflows/python-publish.yml)

A remote orchestrator for frabit via gRPC. The core part of frabit stack.

## 部署

 - 源码获取
   ```bash
   shell> git clone https://github.com/frabitech/frabit-server.git
   ```
   
 - 创建虚拟环境 
   ```bash
   shell> virtualenv venv
   shell> source venv/bin/activate
   (ven) shell>
   ```
 - 安装依赖
   ```bash
   (ven) shell> pip install -r requirements.txt 
   ```
 - 修改配置文件
   ```bash
   (ven) shell> vim /etc/frabitd.cnf
   ```
 - 启动服务
   ```bash
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
