# 第四章.文本和字节序列
1.  把码位转换成字节序列的过程是编码
2.  把字节序列转换成码位的过程是解码
3.  这一章讨论的是Unicode字符串、二进制序列以及在二者之间转换时使用的编码
4.  从python3的str对象获取的元素是Unicode字符
5.  字符的标识，即码位，是0～1114111的数字(十进制)，在Unicode标准中以4～6个十六进制表述数字，而且前缀'U+'
6.  字符的具体表述取决于所用的编码
7.  打开文本文件时，encoding=关键字参数不是必需的，但是应该指定。