from dolfin import *
from time_view import *



  
view = TimeView(input_file)

# Times
ts = view.get_ts() / pcs['spm']