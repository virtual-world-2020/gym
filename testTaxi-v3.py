import time

import gym
import numpy as np

env = gym.make("Taxi-v3") #创建出租车游戏环境
state = env.reset() #初始化环境
envspace = env.observation_space.n #状态空间的大小
actspace = env.action_space.n #动作空间的大小
print(actspace,envspace)

Q = np.zeros([envspace,actspace]) #创建一个Q-table

alpha = 0.5 #学习率
gamma = 0.2
for episode in range(1,2000):
    done = False
    reward = 0 #瞬时reward
    R_cum = 0 #累计reward
    state = env.reset() #状态初始化
    while done != True:
        action = np.argmax(Q[state]) # 选择当前状态下，Q值最大的行为
        state2,reward,done,info = env.step(action)
        Q[state,action] += alpha * (reward+gamma*np.max(Q[state2])-Q[state,action])
        R_cum +=reward
        state = state2
        # time.sleep(0.5)
        # print(reward,R_cum)
        # env.render()
    if episode % 50 == 0:
        print('episode:{};total reward:{}'.format(episode,R_cum))

print('The Q table is:{}'.format(Q))

# 测试阶段
state = env.reset()  # 状态初始化
conter = 0
reward = None
while conter<200:
    time.sleep(1) #暂停一秒，便于观察
    action = np.argmax(Q[state])
    state, reward, done, info = env.step(action)
    conter = conter +1
    env.render()
    if done:
        break
print("counter ==",conter)
print("R_cum ==",R_cum)
