import re

###############  二、编程题：自定义正则匹配函数   ###################
def reg_search(text, regex_list):
    result_list = []

    for regex_dict in regex_list:
        match_result = {}

        # 解析“标的证券”代码
        if "标的证券" in regex_dict:
            pattern_stock = regex_dict["标的证券"]
            stock_match = re.search(pattern_stock, text)
            if stock_match:
                match_result["标的证券"] = stock_match.group(1)

        # 解析“换股期限”日期并标准化输出
        if "换股期限" in regex_dict:
            pattern_date = regex_dict["换股期限"]
            date_matches = re.findall(pattern_date, text)

            formatted_dates = []
            for item in date_matches:
                # 提取年、月、日并导零补全
                year = item[0]
                month = item[1].zfill(2)
                day = item[2].zfill(2)
                formatted_dates.append(f"{year}-{month}-{day}")

            match_result["换股期限"] = formatted_dates

        result_list.append(match_result)

    return result_list

if __name__ == '__main__':
    print("正在运行第二题正则函数匹配测试...")
    sample_text = """
    标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份
    有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债
    券。
    换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束
    之日满 12 个月后的第一个交易日起至可交换债券到期日止，即 2023 年 6 月 2
    日至 2027 年 6 月 1 日止。
    """

    sample_regex_list = [
        {
            "标的证券": r"股票代码：([0-9A-Z.]+)",
            "换股期限": r"(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日",
        }
    ]

    regex_output = reg_search(sample_text, sample_regex_list)
    print(f"返回结果：\n{regex_output}")
