# 使用开源 itchat 库抓取微信好友信息

可抓取所有好友的信息，具体内容如下，使用一个好友进行举例说明：

```
{'MemberList': <ContactList: []>, 'Uin': 0, 'UserName': '@52c38b2d95ecf1bd7265ed76425dabc0253db93cad35ba5b3e52b9ddjs23kx49', 'NickName': '好好学习', 'HeadImgUrl': '/cgi-bin/mmwebwx-bin/webwxgeticon?seq=692fdaf9213&username=@52c3fdqf95ecf1bd7265ed76425dabc0253db93cad35ba5b3e52b9ddc0548d49&skey=@crypt_6a141191_e6e1188b4e94e4ac4a1859e32c027032', 'ContactFlag': 1, 'MemberCount': 0, 'RemarkName': '王二丫', 'HideInputBarFlag': 0, 'Sex': 2, 'Signature': '爱一个人，不是一时的牵手，而是一世的牵心！', 'VerifyFlag': 0, 'OwnerUin': 0, 'PYInitial': 'FSWX', 'PYQuanPin': 'haohaoxuexi', 'RemarkPYInitial': 'WN', 'RemarkPYQuanPin': 'wangerya', 'StarFriend': 0, 'AppAccountFlag': 0, 'Statues': 0, 'AttrStatus': 4477, 'Province': '北京', 'City': '朝阳', 'Alias': '', 'SnsFlag': 1, 'UniFriend': 0, 'DisplayName': '', 'ChatRoomId': 0, 'KeyWord': '', 'EncryChatRoomId': '', 'IsOwner': 0}
```

所以，可以抓取到昵称、备注、签名、省份、城市等等等等。
