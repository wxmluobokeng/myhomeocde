# This Python file uses the following encoding: utf-8

str0 = "央视网消息（新闻联播）：中共中央政治局6月29日下午就“深入学习领会和贯彻落实新时代党的组织路线”举行第二十一次集体学习。中共中央总书记习近平在主持学习时强调，组织建设是党的建设的重要基础。党的组织路线是为党的政治路线服务的。我们党要长期执政、永葆活力，团结带领全国各族人民沿着中国特色社会主义道路实现中华民族伟大复兴，最重要的是把党建设得更加坚强有力。新时代党的组织路线为加强党的组织建设提供了科学遵循，为增强党的创造力、凝聚力、战斗力提供了重要保证。我们要毫不动摇坚持和完善党的领导、继续推进党的建设新的伟大工程，贯彻落实好新时代党的组织路线，不断把党建设得更加坚强有力。"

str2 = str0[1::2]
str1 = str0[0::2]
print(str1)
print(str2)
