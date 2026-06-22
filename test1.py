import csv
import time
import requests
import warnings
warnings.filterwarnings("ignore")

##############  一、编程题：抓取中国货币市场网的国债数据   ###################
def fetch_bond_data():
    # 定位隐藏的数据接口
    url = (
        "https://www.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"
    )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://www.chinamoney.com.cn/english/bdInfo/",
    }

    csv_filename = "bonds_data.csv"

    try:
        with open(csv_filename, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "ISIN",
                "Bond Code",
                "Issuer",
                "Bond Type",
                "Issue Date",
                "Latest Rating",
            ])

            page_no = 1
            total_records = 0

            # 无限循环进行自动翻页抓取
            while True:
                print(f"正在抓取第 {page_no} 页数据...")

                # 动态构造当前页的请求参数（100001代表国债，2023代表年份）
                payload = {
                    "bondType": "100001",
                    "issueYear": "2023",
                    "pageNo": str(page_no),
                    "pageSize": "15",
                }

                response = requests.post(
                    url, data=payload, headers=headers, timeout=15
                )
                res_json = response.json()

                # 提取当前页的数据列表
                bond_list = res_json.get("data", {}).get("resultList", [])

                # 翻页终止条件
                if not bond_list:
                    print(
                        f"提示：第 {page_no} 页数据已空，全量数据抓取完毕！"
                    )
                    break

                #  遍历当前页的数据并写入 CSV
                for bond in bond_list:
                    isin = bond.get("isin", "").strip()
                    code = bond.get("bondCode", "").strip()

                    issuer = (
                        bond.get("entName", "")
                        or bond.get("custName", "")
                        or bond.get("issuerName", "")
                    )
                    if not issuer.strip():
                        issuer = "Ministry of Finance of the People’s Republic of China"

                    b_type = "Treasury Bond"
                    date = bond.get("issueStartDate", "").strip()

                    # 评级特殊符号清洗
                    rating = bond.get("bondRating", "").strip()
                    if not rating or rating == "-":
                        rating = "---"

                    # 写入一行数据
                    writer.writerow([isin, code, issuer, b_type, date, rating])
                    total_records += 1

                #  准备进入下一页
                page_no += 1
                time.sleep(1)

        print(
            f"\n第一题全量抓取成功！"
            f"\n程序共自动翻页 {page_no-1} 次，成功保存了 {total_records} 条完整的国债数据至 [{csv_filename}]！"
        )

    except Exception as e:
        print(f"第一题全量抓取过程中发生错误: {e}")


if __name__ == "__main__":
    fetch_bond_data()