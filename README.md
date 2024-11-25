# Vnstat 网络流量监控插件

这是一个基于 vnstat 的网络流量监控插件，用于查看服务器每月的网络使用情况。

## 前置要求

在使用此插件之前，请确保您的系统已安装以下组件：

1. Python 3.6 或更高版本
2. vnstat

## 安装步骤

### 1. 安装 vnstat

#### Ubuntu/Debian:
```shell
sudo apt update
sudo apt install vnstat
```

#### CentOS/RHEL:
```shell
sudo yum install vnstat
```

### 2. 启动 vnstat 服务
```shell
# 启动服务
sudo systemctl start vnstat

# 设置开机自启
sudo systemctl enable vnstat
```

### 3. 配置 vnstat

1. 确认您的网络接口名称：
```shell
ip addr
```

2. 如果需要，修改 vnstat 配置：
```shell
sudo nano /etc/vnstat.conf
```

## 使用方法

1. 给脚本添加执行权限：
```shell
chmod +x vnstat_monitor.py
```

2. 运行脚本：
```shell
./vnstat_monitor.py
```

## 输出示例
```text
ens5 / monthly

     month         rx   |        tx   |     total   |
------------------------+-------------+-------------+
  2024-03      1.25 GiB |    2.30 GiB |    3.55 GiB |
  2024-02      31.2 GiB |    42.5 GiB |    73.7 GiB |
------------------------+-------------+-------------+
estimated      1.50 GiB |    2.80 GiB |    4.30 GiB |
```

## 功能说明

- 自动检测默认网络接口
- 显示每月的接收(rx)和发送(tx)流量
- 显示当月预估使用量
- 支持 GiB 和 TiB 单位显示

## 故障排除

如果遇到权限问题，请确保：

1. vnstat 服务正在运行：
```shell
sudo systemctl status vnstat
```

2. 用户具有足够权限：
```shell
sudo usermod -a -G vnstat $USER
```

## 注意事项

- 首次安装后，vnstat 需要一些时间来收集数据
- 确保系统时间正确，以便准确统计流量
