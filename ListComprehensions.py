# Görev 1:  ListComprehension yapısı kullanarak car_crashes verisindeki numeric
# değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# Numeric olmayan değişkenlerin de isimleri büyümeli.Tek bir list comprehension yapısı kullanılmalı.

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns


["NUM_" + col.upper() if df[col].dtype != 'O' else col.upper() for col in df.columns]

# Görev 2:  ListComprehension yapısı kullanarak car_crashes verisinde isminde
# "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız
# Tüm değişkenlerin isimleri büyük harf olmalı.Tek bir list comprehension yapısı ile yapılmalı

# find bulamazsa -1 bulursa 0 donduruyor
import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

A = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]

B = [col.upper() + "_FLAG" if col.find("no") == -1 else col.upper() for col in df.columns]
C = [col.upper() + "_FLAG" if col.__contains__("no") == False else col.upper() for col in df.columns]

# Görev 3:  ListComprehension yapısıkullanarakaşağıdaverilendeğişkenisimlerindenFARKLI olandeğişkenlerinisimleriniseçinizveyeni birdataframeoluşturunuz

og_list = ["abbrev", "no_previous"]
new_columns = [col for col in df.columns if col not in og_list]
new_df = df[new_columns].head()
