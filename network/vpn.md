###  理解vpn, shadowsocks
```
参考博客： https://www.vpndada.com/what-is-vpn-cn/
解释：翻墙只是vpn技术的一种应用方式而已。shadowsocks是翻墙的一个工具。

VPN有什么用：
1. VPN可以提高上网的安全性
因为使用VPN时所用的网络访问都是加密进行的，所以使用VPN上网，安全性就更高，黑客很难截取用户的重要信息。如果你使用
公共WIFI上网（例如在咖啡馆上网）时，需要做安全性强的操作（比如使用网上银行或网上投资账户），那么建议你连上VPN，
因为这样会大大提高安全性。

2. VPN可以隐藏上网者的身份
因为VPN用户访问任何网站都是通过VPN服务器间接访问的，所以被访问的网站看到的访问者是VPN服务器，而不是VPN用户本人的电脑，
这样VPN用户就能对要访问的网站隐藏自己的真正身份。

3. VPN可以突破网站的地域限制
很多网站都有地域限制，比如视频网站Netflix在不同国家提供不同的内容，美国用户访问Netflix时看到的是美国版的内容，
香港用户看到的是香港版的内容。网站的这种功能是通过查看访问者的IP地址属于哪个国家来实现的。而VPN可以用来突破这种IP限制。
比如：香港的用户想要看到美国版Netflix的内容，可以先连接到一台位于美国的VPN服务器。这样Netflix网站就会以为访问着来自美国，
而提供美国版的内容。同理，使用日本VPN可以以日本用户的身份访问日本网站和服务。基于同样的道理，海外华人可以通过VPN翻墙回国，
观看仅限国内用户观看的视频内容。另外，VPN还可以用来在网上购物时省钱，因为一些酒店和机票网站对不同国家有不同的价格，
通过VPN换成不同国家的IP往往可以省钱。

4. 突破网络封锁（翻墙）
为什么VPN可以用来翻墙呢？先让我们看看网站是如何被墙的。当用户在中国大陆直接访问被封网站（比如Google）时，网络监控发现你
要连接到被墙网站，直接就把你拦截了。而如果你通过VPN访问这个网站，我们前面提到，VPN用户访问任何网站都是通过VPN服务器代为
访问的，用户连接的其实是VPN服务器，而不是Google（只是告诉VPN服务器你要访问Google），然后VPN服务器去连接Google，把Google
的内容回传给你。这样的话，网络监控看到的是你在连接VPN服务器，而不是在连接Google，同时因为VPN传输是加密的，网络监控也无法
破解你和VPN服务器之间在传输什么信息，所以，（除非VPN服务器也在被墙网址之内）网络监控就不会切断你的连接，于是你就成功翻墙了。

```