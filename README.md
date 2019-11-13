# projectForPreWork
# prework-Todo List
## 目录
* todolist是后端（django），其中api目录是restframe
* todolistfont是前端框架（react）
* others里面包括了过程中创建到的其他材料（用于上手），比如教程文档中的helloworld，mysite投票系统，等等

## 要求
>使用 Django, Django Rest Framework, Bootstrap, PostgreSQL, React 等技术做一个待办事项的网站。

>当然，不必要做得像这个例子这么丰满，主要是要熟悉一下 Django + Django Rest Framework 以及前后端分离的这种架构模式以及 React 这种前端框架。需要注意的是，你必须使用 Django，Django Restframework 和 React 来完成这个项目。

>你可能在未来的工作中以写前端或者后台为主，但我们希望你也能对前后端都有一个初步的了解。

>请注意：我们会对代码原创性进行检查，如果你的代码通篇来自Github，我们会直接将你拒绝。 因为诚信是最重要的品质。当然你可以参考教程，但我们更希望看到你的原创。

**需要支持的功能：**
* 增加一个待办事项
* 删除一个待办事项
* 标记一个待办事项为已完成
* 编辑一个待办事项的具体内容
* 列出所有的待办事项


**可选的功能：**
* 列表界面支持翻页
* 待办事项可以设置优先级
* 待办事项可以设置expire date
* 支持按照不同的方式排序，如优先级，expire date


# 过程记录：

## 11.6

* 安装了python2 
* 配置pycharm，建立工程目录
* 参考restframework文档中要求的环境，在工程中配置： pip install django、markdown、django-filter
* 按照django入门教程，make startaproject "hello world", work it to templates/hello.html
* 按照教程配置api，install restframework，打算按照官网引导做一个小项目熟悉流程
* make a quickStart( in dir " tutorial " ) by https://www.django-rest-framework.org/tutorial/quickstart/. 
* 可以部署后看见接口 
* 下载postgresql ,安装过程中配置如下：
* password123
* port 5432


## 11.7

* 注意到自己的环境和要求的环境不匹配（django 1.1->1.8）
* upgrade django to 1.8.16 (set by pre-work requirement)
* 按照文档在系统服务设置中启动PostgreSQL服务
* pip install psycopg2
* 下载数据库可视化创建工具pgadmin
* 参照[官方文档](https://docs.djangoproject.com/en/1.8/ref/settings/#databases)中如何配置postgresql，将这些用于连接数据库的信息在setting中配置：'NAME': 'postgres','USER': 'postgres','PASSWORD': 'password123','HOST': 'localhost','PORT': '5433'
* 通过pgadmin创建了一个数据库，想在之前配置的model中添加数据字段结构，并按照django的官方文档添加字段类型和规范
* 因为没有系统的思路，感觉过程困难，部署中遇到的错误也相当头疼，当天网购了一本关于django和pythonWeb的书，希望能对我有所帮助

## 11.8

* 因为上一天折腾了很久的数据库，这天重启后台的时候我之前配置的后台今天无法启动了，出现报错，走了一下弯路，方才想起来之前升级过django，可能是有的环境不匹配，最后升级了本地项目中的其他环境，解决了无法启动后台的问题。
* 网上查阅学习了后端在开发中的作用，以及响应前端请求，修改数据库这样的过程，我在model中建立task类，添加了title、content、priority_level、status、create_time、expire_time、last_modify_time等属性，这样便于完成要求（接受前端的请求，在数据库中修改对应的字段，实现删改排序等等功能）
 * 按照教程，在view.py中建立TaskListView类，django文档中给出了mixmin类，类中包括了对于model的增删改查操作，可以直接调用的方法 
* 用指令注册，创建账户，将后端启动后，数据库中成功出现了我的表，在api_task_column中可见我在model中创建的字段


## 11.9
* 今天依据朋友建议，下载了postman用于测试接口和调试api，可以get到从后台发来的json格式数据
* 参照文档，创建并编写Serialization.py，以便将对象的状态信息序列化传输
* 拿到了之前买的书，对着书完善了后台的逻辑，比如url的匹配，也根据书上的字段常用类型加入了日期时间类型等等。但时间不太多，对于书中没有提到的前端向后端发送请求，以及还是不太懂。对react的不了解，前端经验不丰富，都困扰着我。


## 11.10
* 之前电脑中已经有nodejs环境以及cnpm等等工具，没有花太多时间在安装和环境变量等等
* 通过网上程中的create-new-app搭建出了react的环境，然后通过指令创建出来了默认的app欢迎页面。
* 通过bootstrap做出来了为了实现todolist所需要的栅格以及列表等等样式，实现了一个面板来渲染list事件，然后实现一个面板用于编辑和添加事件
* 通过模仿react官方文档的实例完成了纯前端验证，但这时候还没有涉及到后台数据，对于向接口请求数据，和服务端的交流过程，不太清楚怎么实现，询问了朋友，在指导下通过ajax请求能成功获取到接口传来的数据。

## 11.11
* 在之前建立的样式上花了许多时间，将样式中涉及到的事件用react完成了。稍微感觉遗憾的是时间仓促，用了条件渲染的方法在一个url里面完成了功能，没有充分体现出restful的风格
* 对之前的一些没有来得及写上的过程完善了本文的记录部分
* 回过头来发现要求中的finish功能没有实现，然后着手在之前的代码中修改

## 11.12
* 发布并且测试功能，并着手用工具截图做gif 
* 修改了前端显示的几个bug，例如edit无法点击，add后界面没有刷新好等等


# 实现的功能
# 
