#coefficient of correlation
#r value range from -1 to 1(0 means not related)

from scipy import stats
x=[1,2,3,4,5,6,7,8,9]
y=[20,18,16,30,63,53,7,4,34]

slope, intercept,r,p,std_err=stats.linregress(x,y)

print(r)