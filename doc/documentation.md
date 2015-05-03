## Soya车辆网Web API 接口文档 ##

<br />

#### 1. 通过地理位置关键字查询对应地区天气信息(GET: /api/weather) ####

通过指定地区关键字，获取相应地区的天气信息

**请求地址**

```
https://soyaapi.herokuapp.com/api/weather
```

**签名生成**

**系统级参数**

**应用级参数**

 参数名称         | 类型 | 是否必须 | 示例值 | 描述 
----------------|------|---------|-------|-----
location        | str  | 是      | 北京   | 查询天气信息的地区关键字
current_only    | int  | 否      | 0     | 是否只查询当天的天气信息
origin          | int  | 否      | 1     | 是否返回原始结果(为重新解析前的结果)


**示例url**

```
https://soyaapi.herokuapp.com/api/weather?location=北京&current_only=1&origin=0
```

**返回结果**

```
{
    code: 200,
    data: {
        city: "北京",
        weather_info: {
            date: "2015-05-03",
            name: "晴",
            pm25: "48",
            temperature: "25 ~ 10℃",
            wind: "北风4-5级"
        }
    },
    message: "ok"
}
```

**错误码**

错误码   |  代表含义
--------|----------
1000    | 上层服务错误，及百度API没有返回正确结果
601     | 缺少必要的请求参数，例如查询天气时没有指定location关键字
602     | 参数格式错误

<br />

#### 2. 通过地理位置关键字查询对应地区交通状况信息(GET: /api/traffic) ####

通过位置关键字获取指定区域的交通状况信息

**请求地址**

```
https://soyaapi.herokuapp.com/api/traffic
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
-------| -----| -------| -------| --------
location | str | 是    | 北京    | 查询交通状况的地区关键字
start_time | str | 否  | 2015-04-10 | 交通事件的起始时间
end_time | str | 否 | 2015-04-30 | 交通事件的结束时间

**示例url**

```
https://soyaapi.herokuapp.com/api/traffic?location=北京&start_time=2015-04-01&end_time=2015-05-05
```

**返回结果**

```
{
    code: 200,
    data: [
        {
            description: "5月1日零时至5月3日24时，广场西侧路，禁止车辆通行(持专项活动通行证的机动车除外)。",
            endTime: "2015-05-03 23:59:00",
            location: {
                lat: 39.90736968405,
                lng: 116.39580713777
            },
            startTime: "2015-05-01 00:00:00",
            title: "广场西侧路禁止通行",
            type: "暂不清楚"
        },
        {
            description: "5月1日零时至5月3日24时，广场东侧路，禁止车辆通行(持专项活动通行证的机动车除外)。",
            endTime: "2015-05-03 23:59:00",
            location: {
                lat: 39.900280217938,
                lng: 116.39987133835
            },
            startTime: "2015-05-01 00:00:00",
            title: "广场东侧路禁止通行",
            type: "暂不清楚"
        }
    ],
    message: "ok"
}
```

**错误码**

错误码   |  代表含义
--------|----------
1000    | 上层服务错误，及百度API没有返回正确结果
601     | 缺少必要的请求参数，例如查询天气时没有指定location关键字
602     | 参数格式错误

<br />

#### 3. 通过地理位置关键字查询当前城市热映影片(GET: /api/movie/hot) ####

通过地理位置关键字查询当前城市热映影片

**请求地址**

```
https://soyaapi.herokuapp.com/api/movie/hot
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
--------| ----| -------| ------| -------------
location| str | 是     | 北京   | 查询电影信息的地区关键字
is_new   | int | 否    | 1     | 是否是新上映的电影
is_imax  | int | 否    | 0     | 是否是imax
movie_score | float | 否 | 9.0 | 指定返回评分大于等于movie_score电影

**示例url**

```
https://soyaapi.herokuapp.com/api/movie/hot?location=北京&is_new=0&is_imax=1&movie_score=8.0
```

**返回结果**

```
{
    code: 200,
    data: [
        {
            director: "詹姆斯·温",
            length: "138",
            message: "保罗·沃克最后一部作品",
            name: "速度与激情7",
            nation: "美国",
            picture: "http://b.hiphotos.baidu.com/movie/pic/item/35a85edf8db1cb13283e3377d954564e92584b7a.jpg",
            release_date: "2015-04-12",
            score: "9.5",
            starring: "范·迪塞尔/保罗·沃克/杰森·斯坦森/米歇尔·罗德里格兹/道恩·强森/卢卡斯·布莱克",
            tags: "动作,犯罪,剧情",
            time_table: null,
            type: "2D/3D/IMAX 3D"
        },
        {
            director: "让-雅克·阿诺",
            length: "121",
            message: "看冯绍峰上演人狼大战",
            name: "狼图腾",
            nation: "中国大陆,法国",
            picture: "http://c.hiphotos.baidu.com/movie/pic/item/8718367adab44aed44132ac4b71c8701a18bfbb5.jpg",
            release_date: "2015-02-19",
            score: "8.3",
            starring: "冯绍峰/窦骁/昂和妮玛/巴森扎布/尹铸胜",
            tags: "剧情,冒险",
            time_table: null,
            type: "2D/3D/IMAX 3D"
        }
    ],
    message: "ok"
}
``` 

**错误码**

错误码   |  代表含义
--------|----------
1000    | 上层服务错误，及百度API没有返回正确结果
601     | 缺少必要的请求参数，例如查询天气时没有指定location关键字
602     | 参数格式错误

<br />

#### 4. 通过地理位置关键字及影院名称查询指定影院影讯信息(GET: /api/search/cinema) ####

通过地理位置关键字及影院名称查询指定影院影讯信息

**请求地址**

```
https://soyaapi.herokuapp.com/api/search/cinema
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
-------| -----| --------|------| --------------------
location| str | 是      | 北京  | 查询影讯信息的地区关键字
cinema_name| str| 是    | 华星  | 影院名称
movie_score| float | 否 | 9.0   | 指定返回该影院上映电影中评分高于movie_score的电影影讯

**示例url**

```
https://soyaapi.herokuapp.com/api/search/cinema?location=北京&cinema_name=华星&movie_score=8.5
```

**返回结果**

```
{
    code: 200,
    data: [
        {
            address: "北京市海淀区双榆树科学院南路44号(双安商场对面)",
            location: {
                lat: 39.967836985325,
                lng: 116.32575026093
            },
            movies: [
                {
                    director: "詹姆斯·温",
                    length: "138",
                    message: "保罗·沃克最后一部作品",
                    name: "速度与激情7",
                    nation: "美国",
                    picture: "http://e.hiphotos.baidu.com/movie/pic/item/f7246b600c338744e7712018550fd9f9d72aa019.jpg",
                    release_date: "2015-04-12",
                    score: "9.5",
                    starring: "范·迪塞尔/保罗·沃克/杰森·斯坦森/米歇尔·罗德里格兹/道恩·强森/卢卡斯·布莱克",
                    tags: "动作,犯罪,剧情",
                    time_table: [
                        {
                            date: "2015-05-03",
                            lan: "原版",
                            price: 125,
                            time: "20:30",
                            type: "3D"
                        },
                        {
                            date: "2015-05-03",
                            lan: "原版",
                            price: 125,
                            time: "23:00",
                            type: "3D"
                        },
                        {
                            date: "2015-05-04",
                            lan: "原版",
                            price: 85,
                            time: "12:10",
                            type: "3D"
                        },
                        {
                            date: "2015-05-04",
                            lan: "原版",
                            price: 85,
                            time: "14:40",
                            type: "3D"
                        },
                        {
                            date: "2015-05-04",
                            lan: "原版",
                            price: 85,
                            time: "17:10",
                            type: "3D"
                        },
                        {
                            date: "2015-05-04",
                            lan: "原版",
                            price: 125,
                            time: "19:40",
                            type: "3D"
                        },
                        {
                            date: "2015-05-04",
                            lan: "原版",
                            price: 125,
                            time: "22:10",
                            type: "3D"
                        },
                        {
                            date: "2015-05-04",
                            lan: "原版",
                            price: 85,
                            time: "9:40",
                            type: "3D"
                        }
                    ],
                    type: "2D/3D/IMAX 3D"
                }
            ],
            name: "北京UME国际影城(华星店)",
            rating: "4.0",
            telephone: "(010)82115566,(010)82112851"
        }
    ],
    message: "ok"
}
```

**错误码**

错误码   |  代表含义
--------|----------
1000    | 上层服务错误，及百度API没有返回正确结果
601     | 缺少必要的请求参数，例如查询天气时没有指定location关键字
602     | 参数格式错误

<br />

#### 5. 通过地理位置信息及电影名称查询该电影在指定地区的上映信息(GET: /api/search/movie) ####

通过地理位置信息及电影名称查询该电影在指定地区的上映信息

**请求地址**

```
https://soyaapi.herokuapp.com/api/search/movie
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
-------| -----| --------|------| --------------------
location| str | 是      | 北京  | 查询影讯信息的地区关键字
movie_name| str| 是    | 速度与激情  | 影片名称
rating | float | 否 | 4.0   | 指定返回评价高于rating分的影院信息
page_number | int | 否 |  1 | 当返回数据信息较多时，可以通过page_number返回指定页码的影讯信息

**示例url**

```
https://soyaapi.herokuapp.com/api/search/movie?location=北京&movie_name=速度与激情&rating=3.5
```

**返回结果**

```
{
    code: 200,
    data: [
        {
            address: "北京通州运河西大街乔庄卜蜂莲花超市1层佳合时光影城",
            location: {
                lat: 39.892026180354,
                lng: 116.68777296265
            },
            name: "佳合时光影城",
            rating: 3.5,
            telephone: "4000986865",
            time_table: [
                {
                    date: "2015-05-03",
                    lan: "英语",
                    price: 100,
                    time: "19:40",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "国语",
                    price: 100,
                    time: "12:30",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "国语",
                    price: 100,
                    time: "15:00",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "英语",
                    price: 100,
                    time: "16:10",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "国语",
                    price: 100,
                    time: "18:40",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "英语",
                    price: 100,
                    time: "21:10",
                    type: "3D"
                }
            ]
        },
        {
            address: "北京市丰台区靛厂路千禧购物街4号楼F1-F3",
            location: {
                lat: 39.889779749319,
                lng: 116.28733481941
            },
            name: "中影国际影城北京千禧街店",
            rating: 3.5,
            telephone: "(010)88177970,(010)88177863",
            time_table: [
                {
                    date: "2015-05-03",
                    lan: "英语",
                    price: 25,
                    time: "21:20",
                    type: "3D"
                },
                {
                    date: "2015-05-03",
                    lan: "英语",
                    price: 25,
                    time: "20:45",
                    type: "3D"
                },
                {
                    date: "2015-05-03",
                    lan: "英语",
                    price: 25,
                    time: "20:10",
                    type: "3D"
                },
                {
                    date: "2015-05-03",
                    lan: "国语",
                    price: 25,
                    time: "20:05",
                    type: "3D"
                },
                {
                    date: "2015-05-03",
                    lan: "英语",
                    price: 25,
                    time: "18:40",
                    type: "3D"
                }
            ]
        },
        {
            address: "北京昌平区回龙观同成街华联购物中心4楼(城铁回龙观站出口对面)",
            location: {
                lat: 40.071968085194,
                lng: 116.33742692114
            },
            name: "北京沃美影城(回龙观店)",
            rating: 3.5,
            telephone: "4006819819",
            time_table: [
                {
                    date: "2015-05-03",
                    lan: "无",
                    price: 0,
                    time: "19:50",
                    type: "3D"
                },
                {
                    date: "2015-05-03",
                    lan: "无",
                    price: 0,
                    time: "20:30",
                    type: "3D"
                },
                {
                    date: "2015-05-03",
                    lan: "无",
                    price: 0,
                    time: "18:50",
                    type: "3D"
                },
                {
                    date: "2015-05-03",
                    lan: "无",
                    price: 0,
                    time: "21:30",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "无",
                    price: 0,
                    time: "10:00",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "无",
                    price: 0,
                    time: "12:35",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "无",
                    price: 0,
                    time: "15:10",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "无",
                    price: 0,
                    time: "17:50",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "无",
                    price: 0,
                    time: "20:30",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "无",
                    price: 0,
                    time: "10:50",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "无",
                    price: 0,
                    time: "13:30",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "无",
                    price: 0,
                    time: "16:10",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "无",
                    price: 0,
                    time: "18:50",
                    type: "3D"
                },
                {
                    date: "2015-05-04",
                    lan: "无",
                    price: 0,
                    time: "21:30",
                    type: "3D"
                }
            ]
        }
    ],
    message: "ok"
}
```

**错误码**

错误码   |  代表含义
--------|----------
1000    | 上层服务错误，及百度API没有返回正确结果
601     | 缺少必要的请求参数，例如查询天气时没有指定location关键字
602     | 参数格式错误

<br />

#### 6. 将指定城市的指定地点转化为对应的经纬度坐标(GET: /api/geocoding) ####

将指定城市的指定地点转化为对应的经纬度坐标

**请求地址**

```
https://soyaapi.herokuapp.com/api/geocoding
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
-------| -----| --------|------| --------------------
cityname | str | 是      | 上海  | 城市名称
keyword | str |   是    | 近铁城市广场  | 地点名称

**示例url**

```
https://soyaapi.herokuapp.com/api/geocoding?cityname=上海&keyword=近铁城市广场
```

**返回结果**

```
{
    code: 200,
    data: {
        location: {
            lat: 31.233189678235,
            lng: 121.38149998807
        },
        precise: 1
    },
    message: "ok"
}
```

**错误码**

错误码   |  代表含义
--------|----------
1000    | 上层服务错误，及百度API没有返回正确结果
601     | 缺少必要的请求参数，例如查询天气时没有指定location关键字
602     | 参数格式错误

<br />

#### 7. 获取指定坐标表示的地点信息(GET: /api/geocoding/reverse) ####

获取指定坐标表示的地点信息

**请求地址**

```
https://soyaapi.herokuapp.com/api/geocoding/reverse
```

**签名生成**

**系统级参数**

**应用级参数**

参数名称 | 类型 | 是否必须 | 示例值 | 描述
-------| -----| --------|------| --------------------
longitude | float | 是      | 31.233189678235  | 经度
latitude | float |   是    | 121.38149998807 | 维度

**示例url**

```
https://soyaapi.herokuapp.com/api/geocoding/reverse?longitude=121.38149998807&latitude=31.233189678235
```

**返回结果**

```
{
    code: 200,
    data: [
        {
            address: "上海市普陀区金沙江路1518弄2号",
            distance: "0",
            location: {
                lat: 31.227536224709,
                lng: 121.37488222633
            },
            name: "近铁城市广场",
            telephone: "",
            type: "购物"
        },
        {
            address: "上海市普陀区金沙江路1518弄2号近铁城市广场B2层",
            distance: "0",
            location: {
                lat: 31.227536224709,
                lng: 121.37488222633
            },
            name: "kawaii",
            telephone: "",
            type: "购物"
        },
        {
            address: "上海市普陀区金沙江路1518弄2号近铁城市广场B2层",
            distance: "0",
            location: {
                lat: 31.227536224709,
                lng: 121.37488222633
            },
            name: "明翼舞蹈旗舰店",
            telephone: "",
            type: "运动健身"
        },
        {
            address: "上海市普陀区金沙江路1518弄2号近铁城市广场B2层",
            distance: "0",
            location: {
                lat: 31.227536224709,
                lng: 121.37488222633
            },
            name: "汇晶美甲美容",
            telephone: "",
            type: "丽人"
        },
        {
            address: "上海市普陀区金沙江路1518弄2号近铁城市广场B2层",
            distance: "0",
            location: {
                lat: 31.227536224709,
                lng: 121.37488222633
            },
            name: "中信银行ATM",
            telephone: "",
            type: "金融"
        },
        {
            address: "金沙江路1698弄2～9号",
            distance: "174",
            location: {
                lat: 31.228879563757,
                lng: 121.37495411831
            },
            name: "绿洲湖畔花园",
            telephone: "",
            type: "房地产"
        },
        {
            address: "上海普陀区金沙江路1628弄绿洲中环8号楼5楼近真北路",
            distance: "134",
            location: {
                lat: 31.22801010004,
                lng: 121.37381445945
            },
            name: "刘家香(绿洲中环店)",
            telephone: "",
            type: "美食"
        },
        {
            address: "上海市普陀区金沙江路1685号",
            distance: "370",
            location: {
                lat: 31.226582188845,
                lng: 121.37175234579
            },
            name: "118广场",
            telephone: "",
            type: "购物"
        },
        {
            address: "真北路930弄41号6号楼",
            distance: "181",
            location: {
                lat: 31.228519117251,
                lng: 121.37605838937
            },
            name: "启木地暖",
            telephone: "",
            type: "公司企业"
        },
        {
            address: "上海普陀区金沙江路1628号10号绿洲中环中心10号楼5层",
            distance: "133",
            location: {
                lat: 31.227677588197,
                lng: 121.37370680704
            },
            name: "申银万国证券金沙江路营业部",
            telephone: "",
            type: "金融"
        }
    ],
    message: "ok"
}
```

**错误码**

错误码   |  代表含义
--------|----------
1000    | 上层服务错误，及百度API没有返回正确结果
601     | 缺少必要的请求参数，例如查询天气时没有指定location关键字
602     | 参数格式错误
