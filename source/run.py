
import tpl
import csv

path_csv = "../alimama/"
path_ret = "../coupon/"

name_hanfu  = "hanfu"
name_jk     = "jk"
name_lolita = "lolita"


# ['商品id', '商品名称', '商品主图', '商品详情页链接地址', '店铺名称', '商品价格(单位：元)',
# '商品月销量', '收入比率(%)', '佣金', '卖家旺旺', '淘宝客短链接(300天内有效)', '淘宝客链接',
# '淘口令(30天内有效)', '优惠券总量', '优惠券剩余量', '优惠券面额', '优惠券开始时间', '优惠券结束时间',
# '优惠券链接', '优惠券淘口令(30天内有效)', '优惠券短链接(300天内有效)', '是否为营销计划商品',
# '成团人数', '成团价', '成团佣金', '拼团开始时间', '拼团结束时间'],
col_title = 1
col_img_url = 2
col_current_price = 5
col_coupon_price = 15
col_coupon_url = 18
col_coupon_date_start = 16
col_coupon_date_end = 17

def csv_to_list(name):
    path = path_csv + name + '.csv'
    print(path)
    try:
        with open(path, newline='') as f:
            reader = csv.reader(f)
            csv_list = list(reader)
            return csv_list
    except Exception:
        return False

def create_final_html(name, content):
    path = path_ret + name + ".htm"
    if name == name_hanfu:
        title = '汉服优惠券'
    elif name == name_jk:
        title = 'JK优惠券'
    else:
        title = '洛丽塔优惠券'

    final_content = tpl.tpl_page.format(
        title = title,
        content = content,
    )
    with open(path, 'w') as f:
        f.write(final_content)

def date_format(strat_date, end_date):
    return strat_date[5:10].replace('-', '.') + '-' + end_date[5:10].replace('-', '.')

def convert(name):
    ret = ''
    csv_list = csv_to_list(name)
    if not csv_list:
        return False
    for x in csv_list[1:]:
        if not x:
            continue
        one_content = tpl.tpl_content.format(
            title = x[col_title],
            img_url = x[col_img_url],
            current_price = x[col_current_price],
            final_price = int(float(x[col_current_price]) - float(x[col_coupon_price])),
            coupon_price = int(float(x[col_coupon_price])),
            coupon_url = x[col_coupon_url],
            coupon_date = date_format(x[col_coupon_date_start], x[col_coupon_date_end]),
        )
        ret = ret + one_content
    create_final_html(name, ret)

if __name__ == "__main__":
    print('hanfu ---------------')
    convert(name_hanfu)
    print('jk ---------------')
    convert(name_jk)
    print('lolita ---------------')
    convert(name_lolita)

