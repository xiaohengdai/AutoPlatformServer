#这样做的缺点是，当一个子类的父类发生变化时（如类B的父类由A变为C时），必须遍历整个类定义，把所有的通过非绑定的方法的类名全部替换过来，例如代码段2，
#python super()：https://www.cnblogs.com/lovemo1314/archive/2011/05/03/2035005.html