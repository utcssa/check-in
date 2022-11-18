import pandas as pd
from uuid import uuid4

uuid_csv = pd.DataFrame({
    "_id": range(1, 301),
    "uuid": [uuid4() for _ in range(300)]
}).to_csv(index=False)

with open('uuid.csv', 'w') as f:
    f.write(uuid_csv)
