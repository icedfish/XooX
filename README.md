## Env init
```
sudo pip install fabric
git clone https://github.com/icedfish/XooX.git
cd XooX
```

### Show usage & cmd list
```
# fab l
```
when useing password to auth, plz add -I

```
# fab -I l:'dev-*' uptime
```
More on [Fabric Official Docs](http://docs.fabfile.org/en/latest/index.html)

## server_list folder
1. 文件名格式：   
	name**.conf**  (约定的后缀名)

2. 推荐的命名规则
	env-function[-addon].conf
	eg:
		
		prod-db-master.conf
		prod-web-api.conf
		dev-web-h5.conf
	这样写的好处是讲列表和角色结合，方便fab时通过文件名通配指定一批list一起执行，减少list的维护成本。

3. 列表格式：   
	pssh格式 （方便兼容pscp pssh命令，省得同时维护多份配置文件了）

	Sample: [server_list/sample-db.conf](server_list/sample-db.conf)


## 鸣谢
1. [Fabric](http://www.fabfile.org/)
2. [cabric](https://github.com/baixing/cabric)
