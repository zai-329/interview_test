# 笔试作答
仓库地址：https://github.com/zai-329/interview_test

## 文件功能说明
1. test1.py：债券数据爬虫
- 目标站点：https://www.chinamoney.com.cn/english/bdInfo/
- 筛选规则：Bond Type=Treasury Bond、Issue Year=2023
- 输出：筛选结果导出为CSV文件，内置请求头、网络异常捕获

2. test2.py：通用正则匹配函数 reg_search
- 支持传入多组自定义正则规则批量提取文本内容
- 输出结构化字典列表，统一匹配结果格式

## 运行命令
# 执行爬虫任务
python test1.py
# 测试正则提取工具
python test2.py
