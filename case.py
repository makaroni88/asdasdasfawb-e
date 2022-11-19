import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('menu.csv')
df.info()

#среднее количество всех пунктов меню сахара хлостерина протеина
d = df['Sugars'].mean()
d1 = df['Cholesterol'].mean()
d2 = df['Protein'].mean()
s = pd.Series(data = [d , d1 , d2],
index = ['сахар','хлостерин','протеин'])
s.plot(kind = 'barh')
plt.show()
print('Заметим что хлостерин превышает все границы задумайтесь о своём здоровие')
