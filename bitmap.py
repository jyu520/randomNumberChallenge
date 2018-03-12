import pylab as plt
import numpy as np
import urllib2

def getRandomNums():
    url = "https://www.random.org/integers/?num=8192&min=0&max=255&col=1&base=10&format=plain&rnd=new"
    request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)
        if response:
            return np.array(map(int, response.read().split('\n')[:-1]))
    except urllib2.HTTPError, e:
        print 'HTTPError = ' + str(e.code)
    except urllib2.URLError, e:
        print 'URLError = ' + str(e.reason)
    except httplib.HTTPException, e:
        print 'HTTPException'
    except Exception:
        import traceback
        print 'generic exception: ' + traceback.format_exc()

randNums = np.concatenate((getRandomNums(), getRandomNums()))
bitmap = randNums.reshape((128,128))

plt.imshow(bitmap, interpolation='nearest')
plt.show()