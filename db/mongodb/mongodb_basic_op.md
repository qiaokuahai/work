```
创建数据库：
use your_db_name;  //但是创建完之后在navicat中不会显示，除非向里面插入一张表，并插入一条数据
查看数据库：
show dbs;

查看表：
show collections;

创建表
db.createCollection("order")
db.createCollection("order", {"autoIndexId": true})  //自动添加_id主键字段

删除表：
db.your_table_name.drop();
db.student.drop();

创建记录：
// insert方法，插入一条记录，如果表中的_id记录已经存在，则会报错
db.order.insert({"order_name": "computer", "_id": ObjectId("5e9bae25d0430000ee005bf8")})
// 与insert方法不同的是，如果_id记录不存在，则创建一条记录，如果存在，是更新操作
db.order.save({"order_name": "it", "_id": ObjectId("5e9bae25d0430000ee005bf8")})

// 一次性插入多条记录
db.order.insert([
	{
		"order_name": "apple"
	},
	{
		"order_name": "orange"
	}
])

db.order.save([
	{
		"order_name": "apple1"
	},
	{
		"order_name": "orange1"
	}
])

#  更新
db.good.update(
	{"name":"hhhh"},
	{"$set": {"price": 10000, "order_name": "helloo"}},
	{
		"multi": true, // 表示更新多条， 默认值是false，只更新一条
		"upsert": true  // 存在则更新，否则插入
	}
)

#  删除 //尽量不要用
db.good.remove({"name": "apple"}, {"justOne": true})  // 只删除符合条件的一条
db.good.remove({"name": "apple"})  // 删除全部符合条件的记录

删除尽量使用下面的
db.good.deleteOne({"name": "apple"})
db.good.deleteMany({"name": "apple"})

# 查询
db.good.find(
    {
        "$or": [
            {
                "name": "pear"
            },
            {
                "price": {
                    "$gt": 20
                }
            }
        ]
    }
);

// name中以a结尾的列
db.good.find(
	{
		"name": {
			"$regex": "a$"
		}
	}
)

// 查询非空的数据，空字符串不是非空
db.good.find(
	{
		"desc": {
			"$ne": null
		}
	}
)

// 1
{
    "_id": ObjectId("5e9bbc44a6050000d700630c"),
    "name": "hhhh",
    "price": 10000,
    "desc": "hhhh"
}

// 2
{
    "_id": ObjectId("5e9bbc44a6050000d700630d"),
    "name": "gggg",
    "price": 10000,
    "desc": "gggg"
}

// 3  desc字段是空字符串不是非空，所以会被查出来
{
    "_id": ObjectId("5e9bbc4fa6050000d700630e"),
    "name": "kkkk",
    "price": 10000,
    "desc": ""
}

#  查出是字段是数字类型
db.good.find(
	{
		"price": {
			"$type": "number"
		}
	}
)

#  查出price是字符串类型的数据
db.good.find(
	{
		"price": {
			"$type": "string"
		}
	}
)


# skip 和 limit
# 注意：skip中的数据是从第几条数据开始，如果是0,则limit(1)取的是第一条数据
db.good.find().skip(1).limit(1)


# 排序，1是正序，-1是倒序
skip(), limilt(), sort()三个放在一起执行的时候，执行的顺序是先 sort(), 然后是 skip()，最后是显示的 limit()。！！！
db.good.find(
	{
		"price": {
			"$type": "number"
		}
	}
).skip(0).limit(100).sort({"price": -1})


# mongodb分组
# mongodb比起mysql较为麻烦, 语法非常不严谨
db.user.aggregate([
    {
        "$match": {
            "_created": {            // _created前面不要加$，否则会报错
                "$ne": null
            }
        },
    },
    {
        "$group": {                          // group中涉及的数据库字段前面都要加$, 如果是自己定义的字段如total_register_cnt， first_register_name等，不需要加$
            "_id": "$company_id",          //  company_id前面必须加$，否则结果不对
            "total_register_cnt": {
                "$sum": 1             
            },
            "first_register_name": {
                "$first": "$name"
            },
            "first_register_time": {
                "$first": "$_created"
            }
        }
    },
		{
			"$sort": {
				"first_register_time": -1        // 排序必须是group中的字段才行，前面不加$
			}
		}
])

```