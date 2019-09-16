import call_dataset
import numpy as np

Call = call_dataset.calldata("data/delicious/user_taggedbookmarks-timestamps.dat")
array = Call.tagDClens()
HowMake = np.array(array)