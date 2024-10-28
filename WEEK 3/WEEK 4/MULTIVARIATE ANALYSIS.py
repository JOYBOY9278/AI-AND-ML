import pandas as pd
import numpy as np
data =pd.read_csv('Y:\AI and ML\PY WEEKS\WEEK 4\iris.csv')
data
data.corr()

import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.randint(0, 10, size=(5, 3)), columns=['A', 'B', 'C'])
d=data.corr()
print (d)


