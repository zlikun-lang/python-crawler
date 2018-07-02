# python-crawler

Python3 爬虫练习工程


- 爬取豆瓣读书(互联网标签列表页)书籍信息
```
# 插入Mongo的数据(这里只倒数3条，用于展示效果)
> db.books.find().sort({'_id':-1}).limit(3)
{ "_id" : ObjectId("5b398a30e7c87e43846d37f8"), "href" : "https://book.douban.com/subject/1496049/", "title" : "技术文化的时代.从信息社会到虚拟生活", "remark" : "(英国)凯文·罗宾斯等著、何朝阳等译 / 凯文·罗宾斯 / 安徽科学技术出版社 / 1900-01-01 / 22.8" }
{ "_id" : ObjectId("5b398a30e7c87e43846d37f7"), "href" : "https://book.douban.com/subject/26856296/", "title" : "探寻网络法的政治经济起源", "remark" : "胡凌 / 上海财经大学出版社 / 2016-8-1", "star" : "9.0" }
{ "_id" : ObjectId("5b398a30e7c87e43846d37f6"), "href" : "https://book.douban.com/subject/3482862/", "title" : "走进交互设计", "remark" : "刘伟 / 中国建筑工业出版社 / 2013-3 / 35.00元", "star" : "7.5" }
```