import pandas as pd
import matplotlib.pyplot as plt

# csv 파일 읽기
df = pd.read_csv(r'e:\py\b.csv')

# 날짜 컬럼을 인덱스로 지정
df.index = pd.to_datetime(df['date'])

# 상관관계 파악
corr = df.corr()

# 날짜 범위 지정
start_date = '2016-01-01'
end_date = '2022-07-23'

# 범위내의 데이터만 검색
df = df.loc[start_date:end_date]

# 멀티축 그래프 생성
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Sea Temperature', color=color)
ax1.plot(df.index, df['temp'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # 보조 y축 생성
color = 'tab:blue'
ax2.set_ylabel('Average Wave Height', color=color)
ax2.plot(df.index, df['height'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # 그래프 출력 정렬
plt.title('Correlation between Sea Temperature and Average Wave Height')
plt.show()
