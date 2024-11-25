#!/usr/bin/env python3
import subprocess
import json
from datetime import datetime

class VnstatMonitor:
    def __init__(self):
        self.interface = self._get_default_interface()
    
    def _get_default_interface(self):
        try:
            result = subprocess.run(['vnstat', '--iflist'], 
                                 capture_output=True, text=True)
            interfaces = result.stdout.strip().split('\n')
            if len(interfaces) >= 2:
                available_interfaces = interfaces[1].strip().split()
                if available_interfaces:
                    return available_interfaces[0]
            return "ens5"
        except Exception as e:
            return "ens5"
    
    def get_monthly_stats(self):
        try:
            result = subprocess.run(['vnstat', '-m'], 
                                 capture_output=True, text=True)
            
            lines = result.stdout.split('\n')
            monthly_data = []
            
            # 跳过头部信息直到找到表头
            start_index = 0
            for i, line in enumerate(lines):
                if 'month' in line.lower() and 'rx' in line.lower():
                    start_index = i
                    break
            
            # 收集数据行
            data_lines = []
            for line in lines[start_index+2:]:  # 跳过表头和分隔线
                if line.strip() and '|' in line:
                    if 'estimated' in line.lower():
                        data_lines.append(line)
                        break
                    if any(unit in line for unit in ['GiB', 'TiB']):
                        data_lines.append(line)
            
            # 打印头部
            print(f"{self.interface} / monthly\n")
            print("     month           rx    |        tx    |     total    |")
            
            # 打印橙色分隔线
            print("------------------------+-------------+-------------+")
            
            # 打印数据行
            for line in data_lines:
                parts = line.split('|')
                if len(parts) >= 4:
                    month = parts[0].strip()
                    rx = parts[1].strip()
                    tx = parts[2].strip()
                    total = parts[3].strip()
                    
                    # 确保对齐
                    if 'estimated' not in month:
                        print(f"{month:8} {rx:>12} | {tx:>11} | {total:>11} |")
                    else:
                        print("------------------------+-------------+-------------+")
                        print(f"estimated {rx:>11} | {tx:>11} | {total:>11} |")
            
            if 'estimated' not in data_lines[-1]:
                print("------------------------+-------------+-------------+")
            
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == "__main__":
    monitor = VnstatMonitor()
    monitor.get_monthly_stats() 