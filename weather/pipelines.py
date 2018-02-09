#LE Phuong Anh_12416075
class WeatherPipeline(object):
    def __init__(self):
        self.file = open('wea.txt', 'w+')
    def process_item(self, item, spider):
        city = item['city'][0].encode('utf-8')
        self.file.write('city:' + str(city) +'\n\n')
        date = item['date']
        desc = item['dayDesc']
        dayDesc = desc[1::2]
        nightDesc = desc[0::2]
        dayTemp = item['dayTemp']
        weaitem = zip(date, dayDesc, nightDesc, dayTemp)
        for i in range(len(weaitem)):
            item = weaitem[i]
            d = item[0]
            dd = item[1]
            nd = item[2]
            ta = item[3].split('/')
            dt = ta[0]
            nt = ta[1]
            txt = 'data:{0}\t\tday:{1}({2})\t\tnight:{3}({4})\n\n'.format(
            d,
            dd.encode('utf-8'),
            dt.encode('utf-8'),
            nd.encode('utf-8'),
            nt.encode('utf-8')
            )
            self.file.write(txt)
            df.to_csv('out.csv')

        return item
