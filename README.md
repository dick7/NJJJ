# NJJJ ：南京睛界项目启动
##  本文档创建于github
### 系统架构(后端）：python + flask + nginx + uwsgi/wsgi + redis + mysql/psql/mongo + (celery+gnucorn)

### 系统架构（前端）：js + bootstrap + echart + ...

- 20191012 添加requirements.txt,git push 时保存用户名和密码

```code=bash
git clone https://.git  //码云里有克隆链接，避免出现错误，使用https方式
git config --global user.name "用户名"
git config --global user.email "邮箱"
git config --global credential.helper store

// 会生成.gitconfig 的文件，查看

cat .gitconfig   //报错cat: .gitconfig : No such file or directory
cat ~/.gitconfig  //显示内容
```

>[user]
>>        name = 输入的用户名
>>        email = 输入的邮箱
>[credential]
>>        helper = store

第一次pull会提示输入用户名密码

>[root@iZ25mi9h7ayZ test]# git pull
>>Username for 'https://github.com': xxxx@xxxx.com
>>Password for 'https://xxxx@xxxx.com@github.com':输入正确密码（看不到输入内容）

生成.git-credentials 隐藏文件
>cat ~/.git-credentials
>https://Username:Password@github.com
> vi ~/.git-credentials

可加多个用户名密码

