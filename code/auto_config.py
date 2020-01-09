#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import paramiko
import time
import xlrd


def get_list():
    f = xlrd.open_workbook('list.xlsx')
    tables = f.sheet_by_index(0)
    ip_list = []
    user_list = []
    pass_list = []
    x = 1
    while True:
        try:
            data1 = tables.cell(x, 1)
            data2 = tables.cell(x, 2)
            data3 = tables.cell(x, 3)
            x += 1
            data1 = str(data1)
            data2 = str(data2)
            data3 = str(data3)
            ip_list.append(data1[6:][:-1])
            user_list.append(data2[6:][:-1])
            pass_list.append(data3[6:][:-1])
        except IndexError:
            print('Excel信息加载完成!!!')
            break
    print('待配置主机如下：')
    for i in range(0, x - 1):
        print('ip地址：' + ip_list[i] + '  用户名：' + user_list[i] + '  密码： ' + pass_list[i])
    print('合计', len(ip_list), '台主机')

    while True:
        cmd_line = input('输入命令，Y确认主机，N取消：')
        if (cmd_line == 'Y') or (cmd_line == 'y'):
            print('配置已确认')
            return ip_list, user_list, pass_list
        else:
            exit()
    else:
        print('未输入任何命令，程序退出！')
        exit()


def get_config():
    config = open("config.txt", "r")
    pcmd = config.read()
    config.close()
    print('\n将刷入的脚本如下\n')
    print(pcmd)
    while True:
        cmd_line = input('输入命令，Y确认配置，N取消：')
        if (cmd_line == 'Y') or (cmd_line == 'y'):
            print('配置已确认')
            return pcmd
        else:
            exit()
    else:
        print('未输入任何命令，程序退出！')
        exit()


def put_cmd(list):
    iplist = list[0]
    userlist = list[1]
    passwdlist = list[2]
    pcmd = get_config()
    for i in range(0, len(iplist)):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            print('ip地址：' + iplist[i] + '  用户名：' + userlist[i] + '  密码： ' + passwdlist[i] + '  测试')
            ssh.connect(iplist[i], 22, userlist[i], passwdlist[i], timeout=2)
            ssh_cmd = ssh.invoke_shell()
            time.sleep(1)
            ssh_cmd.send(pcmd)
            time.sleep(1)
            sshread = ssh_cmd.recv(4096)
            print(sshread)
            ssh.close()
            print(iplist[i], '完成！')
        except:
            print(iplist[i])
            print('用户名密码错误或者连接超时')
            continue


put_cmd(get_list())
os.system("pause")
