import mysql.connector
from db import weaponMajorKindSeeder
from db import weaponMinorKindSeeder
from db import stageSeeder
from db import weaponSeeder

# seederの実行
weaponMajorKindSeeder.seed()
weaponMinorKindSeeder.seed()
stageSeeder.seed()
weaponSeeder.seed()