import matplotlib.pyplot as plt
import matplotlib.font_manager as fonter
myfont = fonter.FontProperties(fname="Songti.ttc")

x = [i for i in range(1, 25)]
buying = [0.369,0.369,0.369,0.369,0.369,0.369,0.832,0.832,0.832,1.322,1.322,1.322,1.322,1.322,1.322,0.832,0.832,0.832,1.322,1.322,1.322,0.832,0.832,0.369]
selling = [1.4749999999999999, 1.4749999999999999, 1.4749999999999999, 1.4749999999999999, 1.4749999999999999, 1.4749999999999999, 1.4749999999999999, 2.0637499999999998, 2.0637499999999998, 2.7725, 2.7725, 2.7725, 2.7725, 2.7725, 2.7725, 2.0637499999999998, 2.0637499999999998, 2.0637499999999998, 2.7725, 2.7725, 2.0637499999999998, 2.0637499999999998, 2.0637499999999998, 1.4749999999999999]
optisell = [1.593326360932395, 1.395333048693535, 1.5196803480583185, 1.5580291411691218, 1.1383573167070427, 1.6565362798532401, 1.3688948781662404, 2.263969048153723, 2.142583582222681, 2.792604971220557, 2.68761907565876, 2.7529449005312796, 2.7992797286872158, 2.7780030319875384, 2.779322321591551, 1.966650559437774, 1.8104827821820153, 2.262203968234748, 2.796447197421088, 2.788795471121769, 2.124489321152705, 2.137099067197299, 1.8113070585195161, 1.5591370840221854]

currentP = [96.65, 96.65, 96.65, 96.65, 96.65, 96.65, 96.65, 23.680680839716366, 23.680680839716366, 4.1693191602836315, 4.1693191602836315, 4.1693191602836315, 4.1693191602836315, 4.1693191602836315, 4.1693191602836315, 23.680680839716366, 23.680680839716366, 23.680680839716366, 4.1693191602836315, 4.1693191602836315, 23.680680839716366, 23.680680839716366, 23.680680839716366, 96.65]
originalP = [26.5, 26.5, 26.5, 26.5, 26.5, 26.5, 26.5, 56.75, 56.75, 41.25, 41.25, 41.25, 41.25, 41.25, 41.25, 56.75, 56.75, 56.75, 41.25, 41.25, 56.75, 56.75, 56.75, 26.5]

plt.plot(x, currentP, 'g')
plt.plot(x, originalP, 'b')
plt.xlabel(u'时段 / 小时', fontproperties=myfont)
plt.ylabel(u'人数 / 人', fontproperties=myfont)
plt.legend([u'实行分时配价后用户需求量', u'实时分时配价前用户需求量'], prop=myfont)
plt.show()

plt.plot(x, buying, 'r')
plt.plot(x, optisell, 'b')
plt.plot(x, selling, 'g')
plt.xlabel(u'时段 / 小时', fontproperties=myfont)
plt.ylabel(u'价格 / 元', fontproperties=myfont)
plt.legend(['工业电价', '每时段充电配价', '峰、平、谷时段充电配价'], prop=myfont,
           loc='upper left')
plt.show()